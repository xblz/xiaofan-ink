#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ip-preflight.py — 小凡配图 preflight (v2.8.43)

用途: 把"记得检查"变成"脚本会拦"。

三个子命令:
  check-prompt <prompt.txt>   检查生图 prompt 是否带齐必要约束 (含 IP 的图必跑)
  check-essay  <slug>         检查成品图 (公众号 16:9 / 抖音 1:1) 的文件层规范
  crop-face    <img> [x1 y1 x2 y2]  裁切放大脸部, 辅助视觉验收

退出码: 0 = 通过 (可能有 WARN); 1 = 有阻断项 (FAIL)

背景: v2.8.42 事故 —— 为消灭粗黑眉加了「额头完全空白 + 头发后梳」,
把 IP 最核心的识别特征(尖角碎发刘海)删掉了, 用户驳回"IP 形象完全不对"。
本脚本把"刘海必写 / 禁填充用正向写法 / 眉眼正向描述 / 危险词"变成机械阻断项。
"""

import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

OK, WARN, FAIL = "PASS", "WARN", "FAIL"


# ---------------------------------------------------------------- 工具

def _read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _norm(text):
    """归一化: 压掉多余空白, 统一引号, 便于子串匹配"""
    t = re.sub(r"[ \t]+", " ", text)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t


def _has_all(text, groups):
    """groups: [[可选词...], [...]] —— 每组至少命中一个才算满足"""
    low = text.lower()
    for g in groups:
        if not any(w.lower() in low for w in g):
            return False
    return True


def _has_none(text, words):
    low = text.lower()
    return [w for w in words if w.lower() in low]


def _dangerous_positive(text, phrases):
    """
    危险正向词检测: 短语出现时, 前面一小段必须有 NOT / Never / no / without 之类否定词,
    否则说明是在"要求"渲染器做这件事 —— 阻断。

    例: prompt 写 "his hair is slicked back"        -> 阻断
         prompt 写 "NOT slicked back"               -> 放行
         prompt 写 "NOT cropped hair with the forehead exposed" -> 放行 (否定词可能隔得较远)
    """
    low = text.lower()
    hits = []
    for p in phrases:
        for m in re.finditer(re.escape(p.lower()), low):
            head = low[max(0, m.start() - 48):m.start()]
            if not re.search(r"\bnot\b|\bnever\b|\bno\b|without", head):
                hits.append((p, head.strip()[-32:]))
    return hits


# ---------------------------------------------------------------- check-prompt

def check_prompt(path, platform="auto"):
    text = _norm(_read(path))
    results = []

    def add(level, name, detail):
        results.append((level, name, detail))

    # ---- 1. IP 形态核心 (含 IP 的图) ----
    if not _has_all(text, [["fringe", "bangs"], ["forehead"]]):
        add(FAIL, "刘海约束缺失",
            "必须含 'spiky pointed fringe' + 'forehead'。IP 核心识别特征, 缺了直接重画")
    else:
        add(OK, "刘海约束", "已写")

    if not _has_all(text, [["thin black pencil lines", "nothing is filled", "not filled in"]]):
        add(FAIL, "禁填充正向段缺失",
            "抽象禁令 'Do NOT fill...' 实测失效, 必须写 'EVERYTHING is thin black pencil lines "
            "on white paper. NOTHING is filled in with solid colour.'")
    else:
        add(OK, "禁填充正向段", "已写")

    if not _has_all(text, [["overlapping black strokes", "hair density"]]):
        add(FAIL, "HAIR DENSITY 段缺失",
            "只写'别填充'会变成白发, 写'要有黑度'会变成实心块 —— 两句必须同时给")
    else:
        add(OK, "HAIR DENSITY", "已写")

    if not _has_all(text, [["eyebrows"], ["slanted strokes", "slant"]]):
        add(FAIL, "眉毛正向描述缺失",
            "不能写成禁令 (NO eyebrows at all 会连淡短眉一起砍掉)。"
            "要写 'extremely faint, thin, short slanted strokes, much lighter than the hair'")
    else:
        add(OK, "眉毛正向描述", "已写")

    if not _has_all(text, [["eyes"], ["slit", "inner corner"]]):
        add(FAIL, "眼睛正向描述缺失",
            "要写 'narrow slit-like eyes ... ONE tiny solid black dot at the INNER corner', "
            "否则会变成黑豆眼/动漫眼")
    else:
        add(OK, "眼睛正向描述", "已写")

    if not _has_all(text, [["hands"], ["knuckle", "separated fingers"]]):
        add(WARN, "手部描述可能缺失", "建议写 'visible knuckles and naturally separated fingers'")
    else:
        add(OK, "手部描述", "已写")

    # ---- 2. 危险词 ----
    danger = _dangerous_positive(text, [
        "slicked back", "combed back", "brushed back",
        "forehead exposed", "hair pulled back",
    ])
    if danger:
        for p, ctx in danger:
            add(FAIL, "危险正向词: 后梳类",
                f"'{p}' 出现在非否定语境 (…{ctx}…)。会让渲染器把刘海抹掉 —— IP 失真主因")
    else:
        add(OK, "无后梳类危险词", "已检查")

    bad = _has_none(text, [
        "NO eyebrows at all", "COMPLETELY BLANK", "no eyebrows at all",
        "completely blank white space",
    ])
    bad = sorted(set(bad))
    if bad:
        add(FAIL, "危险词: 无眉/空白额头禁令",
            f"出现 {bad} —— v2.8.42 事故的直接来源, 已在 v2.8.43 降级为非阻断项, 不要用")
    else:
        add(OK, "无无眉/空白额头禁令", "已检查")

    if _has_none(text, ["Do NOT fill", "do not fill"]):
        add(WARN, "用了已失效的抽象填充禁令",
            "'Do NOT fill...' 实测不管用。保留无害但要另加正向的 'EVERYTHING is thin black pencil lines'")
    else:
        add(OK, "未用抽象填充禁令", "已检查")

    # ---- 3. 风格 / 文字 ----
    if not _has_all(text, [["line quality"], ["flying-white", "flying white"]]):
        add(WARN, "线条质感段缺失",
            "建议加 'Line quality: loose and sketchy ... flying-white gaps ... "
            "NOT clean vector art, NOT polished commercial line illustration'")
    else:
        add(OK, "线条质感段", "已写")

    if "the only text in the entire image" not in text.lower():
        add(WARN, "文字锁定句缺失",
            "建议写 'The ONLY text in the entire image: XXX — 颜色 brush handwriting' "
            "+ 'No red circle, no arrows, no other marks.'")
    else:
        add(OK, "文字锁定句", "已写")

    if "absolutely no text" not in text.lower():
        add(WARN, "禁文字段缺失", "建议加 '⛔ ABSOLUTELY NO TEXT anywhere except the exact text stated above.'")
    else:
        add(OK, "禁文字段", "已写")

    if not _has_all(text, [["no captions", "no labels"], ["no annotations", "no callouts"]]):
        add(WARN, "禁批注段缺失", "建议加 'NO captions, NO labels, NO annotations, NO arrows pointing at things, NO callouts'")
    else:
        add(OK, "禁批注段", "已写")

    if "standard.png" not in text:
        add(WARN, "未引用 standard.png", "IP 识别靠 reference image, 建议写 'matching the IP reference standard.png'")
    else:
        add(OK, "引用 standard.png", "已写")

    # ---- 4. 平台比例 ----
    plat = platform
    if plat == "auto":
        plat = "douyin" if ("1:1" in text or "square" in text.lower()) else "wechat"
    if plat == "wechat":
        if not _has_all(text, [["full scene with environment"], ["in the scene"]]):
            add(FAIL, "公众号缺场景段",
                "公众号要 'Full scene with environment' + 'The person is IN the scene'. "
                "缺了会退回空壳符号型 (039 反模式)")
        else:
            add(OK, "公众号场景段", "已写")
        if "very large empty white space" in text.lower():
            add(FAIL, "公众号误用抖音留白",
                "'Very large empty white space' 是抖音适配层, 公众号用了会变空壳 (v2.8.41)")
    else:
        if not _has_all(text, [["40-60%", "40 - 60%"]]):
            add(WARN, "抖音缺主体占比", "建议写 'Subject occupies 40-60% of the frame'")
        else:
            add(OK, "抖音主体占比", "已写")
        if "very large empty white space" not in text.lower():
            add(WARN, "抖音缺大留白", "建议写 'Very large empty white space. Quiet and sparse.'")

    return results


# ---------------------------------------------------------------- check-essay

def _front_matter_images(md):
    m = re.search(r"^images:\s*\n((?:\s*-\s*\S+\s*\n)+)", md, re.M)
    if not m:
        return []
    return re.findall(r"-\s*(\S+)", m.group(1))


def check_essay(slug, platform="wechat"):
    results = []

    def add(level, name, detail):
        results.append((level, name, detail))

    if platform == "wechat":
        md_path = os.path.join(ROOT, "doc", "essays", f"{slug}.md")
        if not os.path.exists(md_path):
            cand = [f for f in os.listdir(os.path.join(ROOT, "doc", "essays"))
                    if f.startswith(slug + "-")]
            if not cand:
                add(FAIL, "找不到正文", f"doc/essays/{slug}.md 不存在")
                return results
            md_path = os.path.join(ROOT, "doc", "essays", cand[0])
        add(OK, "正文", os.path.relpath(md_path, ROOT))

        md = _read(md_path)
        imgs = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", md)
        front = _front_matter_images(md)

        if not imgs:
            add(FAIL, "img 引用数为 0", "正文里必须有 ![](), 否则图片上传了但正文无图 (039 事故)")
        elif len(imgs) != len(front):
            add(FAIL, "img 引用数 != images 列表数", f"{len(imgs)} vs {len(front)}")
        else:
            add(OK, "img 引用数", f"{len(imgs)} = images 列表数")

        names = [os.path.basename(i) for i in imgs]
        if names != front:
            add(FAIL, "basename 顺序不一致", f"{names} vs {front}")
        else:
            add(OK, "basename 顺序", "一致")

        base = os.path.dirname(md_path)
        for i in imgs:
            fp = os.path.normpath(os.path.join(base, i))
            if not os.path.exists(fp):
                add(FAIL, "配图文件缺失", fp)
                continue
            with open(fp, "rb") as f:
                head = f.read(2)
            if head != b"\xff\xd8":
                add(FAIL, "不是 JPEG 数据", f"{os.path.basename(fp)} head={head.hex()} (微信要 ffd8)")
            try:
                from PIL import Image
                w, h = Image.open(fp).size
                if (w, h) != (1376, 768):
                    add(FAIL, "尺寸不对", f"{os.path.basename(fp)} {w}x{h} (应 1376x768)")
                else:
                    add(OK, "配图格式", f"{os.path.basename(fp)} ffd8 {w}x{h}")
            except ImportError:
                add(WARN, "PIL 未安装", "跳过尺寸检查")
    else:
        d = os.path.join(ROOT, "doc", "douyin", f"{slug}")
        if not os.path.isdir(d):
            cand = [x for x in os.listdir(os.path.join(ROOT, "doc", "douyin"))
                    if x.startswith(slug + "-") and os.path.isdir(os.path.join(ROOT, "doc", "douyin", x))]
            if not cand:
                add(FAIL, "找不到目录", f"doc/douyin/{slug}-* 不存在")
                return results
            d = os.path.join(ROOT, "doc", "douyin", cand[0])
        add(OK, "目录", os.path.relpath(d, ROOT))
        pngs = sorted(f for f in os.listdir(d) if f.endswith(".png"))
        if not pngs:
            add(FAIL, "没有配图", "目录里没有 .png")
        for f in pngs:
            fp = os.path.join(d, f)
            with open(fp, "rb") as fh:
                head = fh.read(2)
            if head != b"\xff\xd8":
                add(FAIL, "不是 JPEG 数据", f"{f} head={head.hex()}")
            try:
                from PIL import Image
                w, h = Image.open(fp).size
                if (w, h) != (1080, 1080):
                    add(FAIL, "尺寸不对", f"{f} {w}x{h} (应 1080x1080)")
                else:
                    add(OK, "配图格式", f"{f} ffd8 {w}x{h}")
            except ImportError:
                add(WARN, "PIL 未安装", "跳过尺寸检查")

    return results


# ---------------------------------------------------------------- crop-face

def crop_face(path, box=None, out="/tmp/face.png"):
    from PIL import Image
    im = Image.open(path).convert("RGB")
    w, h = im.size
    if box:
        x1, y1, x2, y2 = [float(v) for v in box]
    else:
        x1, y1, x2, y2 = w * 0.33, h * 0.02, w * 0.60, h * 0.42
    crop = im.crop((int(x1), int(y1), int(x2), int(y2)))
    crop = crop.resize((860, 760))
    crop.save(out)
    print(f"✅ 裁切放大已保存: {out}  (源图 {w}x{h}, 裁切区域 {int(x1)},{int(y1)}-{int(x2)},{int(y2)})")
    print("   现在放大看: 刘海在不在 / 眉毛淡不淡 / 眼睛是不是黑豆 / 脸型 / 手")


# ---------------------------------------------------------------- 输出

def _print(results, title):
    print(f"\n=== {title} ===")
    fails = warns = 0
    for level, name, detail in results:
        icon = {OK: "✅", WARN: "⚠️ ", FAIL: "❌"}[level]
        if level == FAIL:
            fails += 1
        elif level == WARN:
            warns += 1
        print(f" {icon} {name}: {detail}")
    print(f"\n  阻断项 {fails} 个, 警告 {warns} 个")
    return fails


def main():
    ap = argparse.ArgumentParser(description="小凡配图 preflight (v2.8.43)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("check-prompt", help="检查生图 prompt")
    p.add_argument("file")
    p.add_argument("--platform", default="auto", choices=["auto", "wechat", "douyin"])

    e = sub.add_parser("check-essay", help="检查成品图")
    e.add_argument("slug")
    e.add_argument("--platform", default="wechat", choices=["wechat", "douyin"])

    c = sub.add_parser("crop-face", help="裁切放大脸部")
    c.add_argument("image")
    c.add_argument("box", nargs=4, type=float, default=None, metavar=("X1", "Y1", "X2", "Y2"))
    c.add_argument("-o", "--out", default="/tmp/face.png")

    args = ap.parse_args()

    if args.cmd == "check-prompt":
        fails = _print(check_prompt(args.file, args.platform), f"prompt 检查: {args.file}")
        sys.exit(1 if fails else 0)
    elif args.cmd == "check-essay":
        fails = _print(check_essay(args.slug, args.platform), f"成品检查: {args.slug}")
        sys.exit(1 if fails else 0)
    else:
        crop_face(args.image, args.box, args.out)


if __name__ == "__main__":
    main()
