"""
公众号文章敏感词 / 品牌名 / 违规项检查。

在 sync_essay 前调用, 输出命中列表, 默认 warn-only 模式不阻断。
v2.5 新增, 配合 v1.5 brand 资源使用。
"""

# 默认避雷的消费品牌名(易被投诉)
DEFAULT_AVOID_BRANDS = [
    # 珠宝
    "周大福", "老凤祥", "中国黄金", "老庙", "菜百", "六福", "周生生", "金至尊",
    "周大生", "潮宏基", "Tiffany", "Cartier", "BVLGARI", "宝格丽", "谢瑞麟",
    "周大福珠宝", "老庙黄金", "周生生珠宝",
    # 餐饮
    "海底捞", "喜茶", "奈雪的茶", "蜜雪冰城",
    # 其他消费品
    "茅台", "五粮液", "可口可乐", "百事可乐", "星巴克", "瑞幸",
]

# 公众号违规引导(易触发审核)
VIOLATION_GUIDES = [
    "扫码关注", "扫码进群", "扫码加", "加微信", "加我微信", "私聊我",
    "联系方式", "电话联系", "商务合作", "广告合作", "商务接洽",
    "二维码", "联系方式见", "电话见", "V 信", "vx", "wechat:", "wx:",
]

# 医疗夸大(易被标记违规)
MEDICAL_EXAGGERATION = [
    "治愈", "根治", "100% 有效", "100% 治愈", "无副作用", "包治百病",
    "立竿见影", "彻底根治", "永不复发", "祖传秘方", "药到病除",
    "纯天然无添加", "老中医", "祖传", "秘方",
]

# 金融夸大
FINANCIAL_EXAGGERATION = [
    "稳赚不赔", "稳赚", "必涨", "必跌", "翻倍", "一夜暴富", "无风险",
    "年化收益 100%", "保本高收益", "内幕消息", "内部消息", "保证收益",
    "零风险", "100% 收益", "翻 10 倍", "十倍股",
]

# 政治敏感(基础列表, 可扩展)
POLITICAL_SENSITIVE = [
    # 留给用户维护
]


def check_text(text, custom_brands=None):
    """
    检查文本中的敏感词/品牌名/违规项。
    返回: list of (category, word, suggestion) tuples
    """
    if not text:
        return []
    hits = []

    # 品牌名
    avoid_brands = list(DEFAULT_AVOID_BRANDS)
    if custom_brands:
        avoid_brands.extend(custom_brands)
    for brand in avoid_brands:
        if brand in text:
            hits.append(("品牌名(避雷)", brand, "用通用描述代替, 如'某品牌/另一家'"))

    # 违规引导
    for word in VIOLATION_GUIDES:
        if word in text:
            hits.append(("违规引导", word, "删除, 公众号禁止私域引流"))

    # 医疗夸大
    for word in MEDICAL_EXAGGERATION:
        if word in text:
            hits.append(("医疗夸大", word, "删除或改写, 公众号对医疗内容审核严"))

    # 金融夸大
    for word in FINANCIAL_EXAGGERATION:
        if word in text:
            hits.append(("金融夸大", word, "删除或改写, 公众号对投资建议审核严"))

    # 政治敏感
    for word in POLITICAL_SENSITIVE:
        if word in text:
            hits.append(("政治敏感", word, "请人工复核"))

    return hits


def check_essay_file(essay_path, custom_brands=None):
    """
    检查单个 essay 文件(front matter + body)。
    返回: list of (category, word, suggestion) tuples
    """
    from pathlib import Path
    p = Path(essay_path)
    if not p.exists():
        return []
    content = p.read_text(encoding="utf-8")
    return check_text(content, custom_brands=custom_brands)


def print_report(hits, target="文章"):
    """打印检查报告。"""
    if not hits:
        print(f"   ✅ {target} 无敏感词命中")
        return True
    print(f"   ⚠️  {target} 命中 {len(hits)} 项:")
    for category, word, suggestion in hits:
        print(f"      [{category}] '{word}'")
        print(f"        → 建议: {suggestion}")
    return False


if __name__ == "__main__":
    import sys
    from pathlib import Path

    if len(sys.argv) < 2:
        print("用法: python3 sensitive-check.py <essay.md>")
        sys.exit(1)

    essay_path = Path(sys.argv[1])
    hits = check_essay_file(essay_path)
    print(f"🔍 检查: {essay_path.name}")
    if print_report(hits, target="essay"):
        sys.exit(0)
    sys.exit(2)  # 命中返回非零
