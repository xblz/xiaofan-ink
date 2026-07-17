#!/usr/bin/env python3
"""
articles-to-wechat.py — 把 xiaofan-ink essays 同步到微信公众号草稿箱

用法:
    python articles-to-wechat.py 001                    # 同步 001 到草稿
    python articles-to-wechat.py 001-why-i-dont-do-daily-plan.md  # 同步指定文件
    python articles-to-wechat.py --list                 # 列出所有 essays
    python articles-to-wechat.py --test                 # 测试 API 连接
    python articles-to-wechat.py --all                  # 同步所有 essays(慎用)

需要:
    - config.json(同目录,放 AppID/AppSecret,gitignored)
    - requests(pip install requests)
    - pyyaml(pip install pyyaml,读 front matter)

微信公众号 API 限制:
    - 个人订阅号:草稿箱可用,群发每天 1 次(高级群发要认证订阅号)
    - access_token 2 小时过期,自动缓存
    - 图片上传有大小限制(图文消息内图片:1MB;永久素材图:2MB)
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ 需要安装 requests: pip install requests")
    sys.exit(1)

try:
    import yaml
except ImportError:
    print("⚠️  pyyaml 未装,front matter 用正则解析(也能用)")
    yaml = None

try:
    import markdown as _markdown
    from bs4 import BeautifulSoup as _BeautifulSoup
except ImportError:
    print("❌ 需要安装 markdown + beautifulsoup4 + lxml:")
    print("   pip install markdown beautifulsoup4 lxml")
    sys.exit(1)


# ---------- 路径配置 ----------

SCRIPT_DIR = Path(__file__).parent.resolve()
REPO_ROOT = SCRIPT_DIR.parent.parent  # xiaofan-ink/tools/ → repo root
CONFIG_PATH = SCRIPT_DIR / "config.json"
ESSAYS_DIR = REPO_ROOT / "doc" / "essays"
TOKEN_CACHE_PATH = SCRIPT_DIR / ".token_cache.json"


# ---------- 工具函数 ----------

def load_config():
    """加载本地 config.json(包含 AppID/AppSecret,gitignored)"""
    if not CONFIG_PATH.exists():
        print(f"❌ 找不到配置文件: {CONFIG_PATH}")
        print("   请先复制 config.example.json → config.json 并填入真实凭证")
        sys.exit(1)
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def save_token_cache(token, expires_at):
    """缓存 access_token 到本地文件(避免每次重新获取)"""
    with open(TOKEN_CACHE_PATH, "w", encoding="utf-8") as f:
        json.dump({"access_token": token, "expires_at": expires_at}, f)


def load_token_cache():
    """读取缓存的 access_token,过期返回 None"""
    if not TOKEN_CACHE_PATH.exists():
        return None
    try:
        with open(TOKEN_CACHE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        if data["expires_at"] > time.time() + 60:  # 留 60 秒缓冲
            return data["access_token"]
    except (json.JSONDecodeError, KeyError):
        pass
    return None


def parse_front_matter(md_text):
    """解析 markdown 顶部的 YAML front matter,返回 (meta_dict, body)"""
    if not md_text.startswith("---"):
        return {}, md_text
    parts = md_text.split("---", 2)
    if len(parts) < 3:
        return {}, md_text
    fm_text = parts[1].strip()
    body = parts[2].strip()
    if yaml:
        try:
            meta = yaml.safe_load(fm_text) or {}
            # 关键修复:yaml 会把 "001" 解析成 int 1,这里强制保留为字符串
            for k in ("n", "date", "slug"):
                if k in meta and not isinstance(meta[k], str):
                    meta[k] = str(meta[k])
            return meta, body
        except yaml.YAMLError:
            pass
    # 降级:简单 key: value 解析
    meta = {}
    for line in fm_text.split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, body


def md_to_wechat_html(md_text, image_url_map, accent="#C0392B"):
    """
    把 markdown 转成微信公众号兼容的 HTML。

    走 markdown 库 + bs4 后处理两步:
    1. markdown.markdown() 转出标准 HTML
    2. bs4 遍历每个元素,套上 brand style-guide 里的样式

    样式参考 brand/style-guide.md:
    - 调色板: 墨 #1A1A1A / 红 #C0392B / 橙 #E67E22 / 蓝 #2C5F8D / 米 #F4EFE6 / 灰 #666666
    - 字号: H1 24px / H2 18px / 正文 16-17px
    - 行距: 1.85(公众号屏幕小,行距要够松才不累)
    - 引用块: 米色底 + 红色左竖线
    - 配图: 居中,不加圆角/阴影

    image_url_map: 本地相对路径 → 微信返回的 url(由 sync_essay 注入)
    accent: 强调色(strong / blockquote 左边线 / h2 装饰),默认红
    """
    # 1. markdown → HTML
    # 注:不加 smarty,避免把直引号 " 改成花引号 "(style-guide 规定用「」)
    html = _markdown.markdown(
        md_text,
        extensions=["extra", "sane_lists"],
    )

    # 2. bs4 遍历套样式
    soup = _BeautifulSoup(html, "lxml")

    # 2.1 图片: 把本地路径换成微信 URL
    for img in soup.find_all("img"):
        src = img.get("src", "")
        # 微信编辑器的 img 必须用 https:// 开头,缺省 protocol 的本地路径不显示
        if src in image_url_map:
            img["src"] = image_url_map[src]
        img["style"] = (
            "max-width: 100%; height: auto; display: block; "
            "margin: 20px auto; border-radius: 0; box-shadow: none;"
        )
        if not img.get("alt"):
            img["alt"] = ""

    # 2.2 段落
    for p in soup.find_all("p"):
        p["style"] = (
            "margin: 14px 0; line-height: 1.85; font-size: 17px; "
            "color: #1A1A1A; letter-spacing: 0.3px;"
        )

    # 2.3 标题(H1 文章主标题 / H2 段落小标题)
    for h1 in soup.find_all("h1"):
        h1.name = "p"  # 公众号 H1 样式不可控,用大号 p
        h1["style"] = (
            f"font-size: 24px; font-weight: bold; color: #1A1A1A; "
            f"line-height: 1.5; margin: 24px 0 20px; padding: 0;"
        )
    for h2 in soup.find_all("h2"):
        h2.name = "p"
        h2["style"] = (
            f"font-size: 18px; font-weight: bold; color: #1A1A1A; "
            f"line-height: 1.6; margin: 28px 0 14px; "
            f"padding-left: 10px; border-left: 3px solid {accent};"
        )

    # 2.4 引用块: 米色底 + 红色左竖线
    for bq in soup.find_all("blockquote"):
        bq["style"] = (
            f"background: #F4EFE6; border-left: 3px solid {accent}; "
            f"padding: 14px 16px; margin: 20px 0; "
            f"color: #1A1A1A; border-radius: 0;"
        )
        for child_p in bq.find_all("p"):
            child_p["style"] = (
                "margin: 8px 0; line-height: 1.85; font-size: 16px; "
                "color: #1A1A1A;"
            )

    # 2.5 水平线
    for hr in soup.find_all("hr"):
        hr["style"] = (
            "border: none; border-top: 1px solid #E5E5E5; "
            "margin: 32px 0;"
        )

    # 2.6 行内元素
    for strong in soup.find_all("strong"):
        strong["style"] = f"color: {accent}; font-weight: bold;"
    for em in soup.find_all("em"):
        em["style"] = "font-style: italic; color: #1A1A1A;"
    for code in soup.find_all("code"):
        code["style"] = (
            "background: #F4F4F4; padding: 1px 6px; "
            "border-radius: 3px; font-size: 15px; "
            "color: #1A1A1A; font-family: monospace;"
        )
    for a in soup.find_all("a"):
        a["style"] = f"color: {accent}; text-decoration: none;"

    # 3. 拼接:bs4 输出 + 整段 section style(保证移动端阅读体验)
    section_style = (
        "max-width: 100%; padding: 0 4px; "
        "font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', "
        "'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;"
    )
    # 拿 body 的 inner 内容(去掉 <html><body> 包装,bs4 给加的)
    if soup.body:
        body_html = soup.body.decode_contents()
    else:
        body_html = str(soup)
    return f"<section style='{section_style}'>{body_html}</section>"


# ---------- 微信 API 调用 ----------

def get_access_token(config):
    """获取 access_token,优先用缓存"""
    cached = load_token_cache()
    if cached:
        return cached
    url = "https://api.weixin.qq.com/cgi-bin/token"
    params = {
        "grant_type": "client_credential",
        "appid": config["appid"],
        "secret": config["appsecret"],
    }
    r = requests.get(url, params=params, timeout=30)
    data = r.json()
    if "access_token" not in data:
        raise RuntimeError(f"获取 access_token 失败: {data}")
    token = data["access_token"]
    expires_in = data.get("expires_in", 7200)
    expires_at = time.time() + expires_in
    save_token_cache(token, expires_at)
    return token


def upload_image_for_content(token, file_path):
    """上传图文消息内图片(用于 content HTML 里的 <img>),返回微信 URL"""
    url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg"
    params = {"access_token": token}
    with open(file_path, "rb") as f:
        files = {"media": f}
        r = requests.post(url, params=params, files=files, timeout=60)
    data = r.json()
    if "url" not in data:
        raise RuntimeError(f"上传图片失败 {file_path}: {data}")
    return data["url"]


def upload_thumb_media(token, file_path):
    """上传永久素材(用于封面 thumb_media_id),返回 media_id"""
    url = "https://api.weixin.qq.com/cgi-bin/material/add_material"
    params = {"access_token": token, "type": "image"}
    with open(file_path, "rb") as f:
        files = {"media": f}
        r = requests.post(url, params=params, files=files, timeout=60)
    data = r.json()
    if "media_id" not in data:
        raise RuntimeError(f"上传封面失败 {file_path}: {data}")
    return data["media_id"]


def create_draft(token, articles):
    """创建草稿(draft/add),返回 draft media_id。
    关键:微信公众号 API 期望 UTF-8 JSON,requests 默认 ensure_ascii=True
    会把中文转成 \\uXXXX,导致公众号编辑器里看到乱码。所以要手动序列化。
    """
    import json as _json
    url = "https://api.weixin.qq.com/cgi-bin/draft/add"
    params = {"access_token": token}
    payload = {"articles": articles}
    r = requests.post(
        url,
        params=params,
        data=_json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        timeout=60,
    )
    data = r.json()
    if "media_id" not in data:
        raise RuntimeError(f"创建草稿失败: {data}")
    return data["media_id"]


# ---------- 主流程 ----------

def test_connection(config):
    """测试 API 连接"""
    print("🔗 测试 API 连接...")
    try:
        token = get_access_token(config)
        print(f"✅ access_token 获取成功")
        print(f"   前 10 字符: {token[:10]}...")
        return True
    except Exception as e:
        print(f"❌ 连接失败: {e}")
        return False


def list_essays():
    """列出所有 essays"""
    if not ESSAYS_DIR.exists():
        print(f"❌ 找不到 essays 目录: {ESSAYS_DIR}")
        return
    essays = sorted(ESSAYS_DIR.glob("00*-*.md"))
    if not essays:
        print("📭 没有 essays(还没有发布的文章)")
        return
    print(f"📚 找到 {len(essays)} 篇 essays:\n")
    for f in essays:
        meta, _ = parse_front_matter(f.read_text(encoding="utf-8"))
        n = meta.get("n", "?")
        title = meta.get("title", "(无标题)")
        print(f"  [{n}] {f.name}")
        print(f"      {title}")
        print()


def find_essay_by_slug(slug):
    """根据 slug 或 n 找 essay 文件"""
    if not ESSAYS_DIR.exists():
        return None
    # slug 形如 "001" 或 "001-why-i-dont-do-daily-plan"
    essays = sorted(ESSAYS_DIR.glob("00*-*.md"))
    for f in essays:
        if f.stem == slug or f.stem.startswith(slug + "-") or f.stem.startswith(slug):
            return f
    return None


def sync_essay(config, slug):
    """同步指定 essay 到草稿箱"""
    essay_path = find_essay_by_slug(slug)
    if not essay_path:
        print(f"❌ 找不到 essay: {slug}")
        print("   用 --list 看所有 essays")
        return False

    print(f"📄 读取 essay: {essay_path.name}")
    md_text = essay_path.read_text(encoding="utf-8")
    meta, body = parse_front_matter(md_text)
    title = meta.get("title", essay_path.stem)
    n = meta.get("n", "000")

    # 找配图目录
    images_dir = ESSAYS_DIR / "images" / essay_path.stem
    if not images_dir.exists():
        print(f"❌ 配图目录不存在: {images_dir}")
        return False

    # 收集所有图(按文件名排序)
    image_files = sorted(images_dir.glob("*.png")) + sorted(images_dir.glob("*.jpg")) + sorted(images_dir.glob("*.jpeg"))
    if not image_files:
        print(f"❌ 配图目录为空: {images_dir}")
        return False
    print(f"🖼️  找到 {len(image_files)} 张配图")

    # 1. 获取 access_token
    print("\n🔑 获取 access_token...")
    token = get_access_token(config)

    # 强制 n 为字符串(yaml 会把 "001" 解析成 int 1)
    n = str(n)
    title = str(title)

    # 2. 上传所有配图到"图文消息内图片",获取微信 URL
    print("\n📤 上传配图到图文消息内图片 API...")
    image_url_map = {}  # 本地路径 → 微信 URL
    for img in image_files:
        local_relpath = f"images/{essay_path.stem}/{img.name}"  # 对应 markdown 里的引用
        print(f"   上传 {img.name}...", end=" ")
        try:
            wechat_url = upload_image_for_content(token, img)
            # 多种 key 都存一份,容忍 markdown 引用风格差异
            image_url_map[local_relpath] = wechat_url
            image_url_map[f"./images/{essay_path.stem}/{img.name}"] = wechat_url
            image_url_map[img.name] = wechat_url
            # stem 前缀(去掉 -xxx 后缀),让 `01.png` 也能命中 `01-paper-sunk.png`
            stem = img.stem.split("-")[0]
            image_url_map[f"images/{essay_path.stem}/{stem}.png"] = wechat_url
            image_url_map[f"images/{essay_path.stem}/{stem}.jpg"] = wechat_url
            image_url_map[f"{stem}.png"] = wechat_url
            print(f"✅ {wechat_url[:50]}...")
        except Exception as e:
            print(f"❌ {e}")
            return False

    # 3. markdown 转 HTML(图替换)
    print("\n🔄 markdown → HTML...")
    html = md_to_wechat_html(body, image_url_map)

    # 4. 上传封面(优先 cover.png,否则用第一张配图)
    print("\n🖼️  上传封面...")
    cover_candidates = [
        images_dir / "cover.png",
        images_dir / "cover.jpg",
        images_dir / "00-cover.png",
    ]
    cover_path = next((p for p in cover_candidates if p.exists()), image_files[0])
    print(f"   用 {cover_path.name} 作封面")
    try:
        thumb_media_id = upload_thumb_media(token, cover_path)
        print(f"   thumb_media_id: {thumb_media_id}")
    except Exception as e:
        print(f"❌ 上传封面失败: {e}")
        return False

    # 5. 创建草稿
    print("\n📝 创建草稿...")
    # 摘要优先级: front matter 的 digest 字段 > title[:54]
    # 公众号个人订阅号 digest 最多 54 字,超出会被静默截断
    digest = meta.get("digest") or title[:54]
    if len(digest) > 54:
        digest = digest[:54]
    # 标题不加《》包裹 —— v1.7.1 调整
    # 原:f"《{title}》"
    # 公众号编辑器自己会处理标题样式,推送 list 里看的就是纯标题,
    # 加《》反而显得繁琐/装。
    article = {
        "title": title,
        "author": config.get("author", "小凡"),
        "digest": digest,
        "content": html,
        "content_source_url": meta.get("source_url", ""),
        "thumb_media_id": thumb_media_id,
        "need_open_comment": 0,  # 关闭评论
        "only_fans_can_comment": 0,
    }
    try:
        draft_media_id = create_draft(token, [article])
        print(f"✅ 草稿创建成功")
        print(f"   draft_media_id: {draft_media_id}")
    except Exception as e:
        print(f"❌ 创建草稿失败: {e}")
        return False

    print(f"\n🎉 同步完成!")
    print(f"   📱 公众号后台 → 草稿箱 → 找到 [{n}] {title} → 群发/定时发布")
    return True


def main():
    parser = argparse.ArgumentParser(description="把 xiaofan-ink essays 同步到微信公众号草稿箱")
    parser.add_argument("slug", nargs="?", help="Essay 编号或文件名(如 001)")
    parser.add_argument("--list", action="store_true", help="列出所有 essays")
    parser.add_argument("--test", action="store_true", help="测试 API 连接")
    parser.add_argument("--all", action="store_true", help="同步所有 essays(慎用)")
    args = parser.parse_args()

    if args.list:
        list_essays()
        return

    config = load_config()

    if args.test:
        test_connection(config)
        return

    if args.all:
        essays = sorted(ESSAYS_DIR.glob("00*-*.md"))
        print(f"🔁 同步所有 {len(essays)} 篇 essays\n")
        for f in essays:
            print(f"\n{'='*60}")
            print(f"[{f.stem}]")
            print(f"{'='*60}")
            sync_essay(config, f.stem)
            print()
        return

    if not args.slug:
        parser.print_help()
        return

    sync_essay(config, args.slug)


if __name__ == "__main__":
    main()
