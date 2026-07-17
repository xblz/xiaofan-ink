# CHANGELOG

> xiaofan-ink 项目关键改动记录。每次有意义改动都更新一行(或一段)。
>
> 完整 git 历史见 `git log --oneline`。本文件只记**功能级别**的改动,小修小补不进。

---

## v1.7.1 — 2026-07-17(推送标题去《》)

v1.6 / v1.7 时代 resync 出来的草稿,标题都被脚本包了《》(中文文章标题常用格式)。

**问题**:
- 公众号推送 list 里看的是纯标题,加《》显得繁琐/装
- 公众号编辑器自己会处理标题样式,加《》反而干扰

**修复**:`xiaofan-ink/tools/articles-to-wechat.py` 的 `create_draft` 调用,把 `f"《{title}》"` 改成 `title`(直接用 front matter 的 title,不加包裹)。

### 同步结果

| | 草稿 ID | 推送标题 |
|--|--|--|
| 000 | `4Qs6oAKkTbuKncYKGGbmXKb-tAhKVrH0Ksv-yqdM5FYzT2AhE8pZHM7zSyLpB9SWW` | 我开了个公众号,叫"草稿本" |
| 001 | `4Qs6oAKkTbuKncYKGGbmXJ0L0IBrN3HhPKjln7aG20sxiDq1QNFy3p8yp9aEJ0Cm` | 5 年每日计划,我戒了 |
| 002 | `4Qs6oAKkTbuKncYKGGbmXBX-f9EgrjNyEUv2K1zVxJDy_WoCEVPmWENK8KEaNa4b` | 番茄钟 3 年,我放下了 |

### 用户后续

公众号后台 → 草稿箱 → 删 v1.7 时代那 3 个带《》 的旧草稿,留 v1.7.1 这 3 个干净的。

---

## v1.7 — 2026-07-17(品牌节奏调整 + 000 重写 + 全文档同步)

把"每周三 1 篇"推翻,改成"想写就写"。**公众号节奏从此不固定**。

### 核心调整:不固定更新频率

**原计划**:每周三 1 篇,固定时间,培养读者期待。
**新规则**:想写就写。可能 1 周 2 篇,也可能 1 个月 1 篇。

**为什么改**:固定频率 → 又走回"每日计划"老路 → 写不出硬憋 → 出水文。跟系列调性"过程 > 结论 / 草稿 > 作品"自相矛盾(在反思"每日计划"却又立"每周三"这种新 flag)。

### 1. 000 重写(用新模式)

- **标题**: 为什么开一个"草稿本"公众号 → **我开了个公众号,叫"草稿本"**(11 字,直接陈述,品牌植入)
- **digest**: 每周一篇,可能有时候是废稿 → **想写就写,可能有时候是废稿**("想写就写" 替代"每周一篇")
- **去 AI 味**:
  - "写完、改完、满意了才发" → "写完、改到自己满意了才发"(3 段式 → 2 段式)
  - "每日计划、番茄钟、GTD" → "每日计划、番茄钟"(减 1 items)
  - "死板冷静。不喊加油,不写'姐妹们冲'" → "死板冷静。不喊加油,不卖萌"
  - "我不教你 X,我只想说 Y" → "我只想说 Y"(去"不 X,只 Y" 模式)
  - 收尾从"下周三见" → "什么时候见,看心情"

### 2. 品牌初衷 + 核心三句话

所有 brand 文档加"初衷"段,把"为什么开这个号"讲清楚。**核心三句话**(整个号的灵魂,判断一切内容的标准):

1. **过程比结论值钱**
2. **草稿比作品诚实**
3. **死板冷静**

如果一篇东西写得像"成长博主" / "自律达人" / "干货文",那就删掉重写。

### 3. 全文档同步(去"每周三",加初衷 + 品牌定位)

| 文件 | 改动 |
|------|------|
| `doc/essays/README.md` | 加"系列初衷" + "节奏" 段,改"每周三" → "想写就写" |
| `doc/CREATION-PLAN.md` | 加 §0 创作初衷 + 核心三句话;§2 节奏表全改;§7 拍板表关闭;§8 长期视角按"篇数" 算 |
| `doc/SERIES-STATE.md` | 元信息"每周三" → "想写就写" |
| `brand/README.md` | 加"初衷" 段 + 核心三句话,改 3 个简介备选,改 §2 欢迎语引用 |
| `brand/welcome.md` | 关注后自动回复去"每周三";加"初衷" 关键词回复;改"关于" 回复;改"草稿本(备用)" |
| `brand/style-guide.md` | §5 头图文字"每周三更新" → "想写就写";§6.2 结尾"下周三见" → "看心情";首期封面建议更新 |
| `brand/menu.md` | 无需改(没提"每周三") |
| `xiaofan-ink/SKILL.md` | 无需改(生图 skill,跟写作节奏无关) |
| `xiaofan-ink/references/*` | 无需改 |
| `xiaofan-ink/assets/prompts/articles/001-why-i-dont-do-daily-plan.md` | 末尾"每周三" → "想写就写" |
| `README.md`(根) | 加"关联公众号" 一行;doc/essays 目录树加 000 |
| `NOTICE.md` | 无需改(讲 fork 关系) |

### 4. 同步结果

000 用新版本 resync 成功:
- 草稿 ID: `4Qs6oAKkTbuKncYKGGbmXDY_xEz56gMxM1uPoPXNwPLrtnNY_6A85G3EiJmyAYYf`
- 推送标题: 《我开了个公众号,叫"草稿本"》
- digest: 想写就写,可能有时候是废稿。这里是过程比结论值钱,草稿比作品诚实。

### 5. 文件变更(11 个)

- `doc/essays/000-grass-journal-intro.md`(重写)
- `doc/essays/README.md`(加初衷 + 节奏段)
- `doc/CREATION-PLAN.md`(加 §0 初衷 + 改 §2 节奏)
- `doc/SERIES-STATE.md`(元信息去"每周三")
- `brand/README.md`(加初衷段)
- `brand/welcome.md`(关注回复 + 关键词回复)
- `brand/style-guide.md`(头图 + 结尾)
- `xiaofan-ink/assets/prompts/articles/001-why-i-dont-do-daily-plan.md`(末尾)
- `README.md`(加关联公众号 + 000 目录树)
- `CHANGELOG.md`(本 entry)

### 6. 用户后续

- 公众号后台 → 草稿箱 → 删 v1.6 时代的 000 草稿(标题"为什么开一个'草稿本'公众号" 那个)
- 留 v1.7 时代的 000(标题"我开了个公众号,叫'草稿本'" 那个)
- 3 篇全齐:000 + 001 + 002,按 000 → 001 → 002 顺序发

---

## v1.6 — 2026-07-17(标题/摘要优化 + 开篇 000)

> ⚠️ 000 标题/正文/品牌定位已在 **v1.7 重写**;v1.6 时代草稿需在公众号后台手动删除。本 entry 保留为历史记录。

公众号上线前最后一波:把 001/002 的推送标题和摘要重写得更抓人,并新增开篇 000 收口品牌定位 + 联动 001。

### 1. 标题重写(短 + 数字 + 转折)

走"反共识 + 数字 + 短促"路线,8-12 字,不喊"震惊体"。

| | 旧 | 新 |
|--|--|--|
| 001 | 为什么我不再做每日计划 | **5 年每日计划,我戒了** |
| 002 | 专注力的边界 | **番茄钟 3 年,我放下了** |
| 000 | (新增) | **为什么开一个"草稿本"公众号** |

### 2. 摘要加 `digest` 字段(替代 title[:54])

旧版:脚本默认把 title 截 54 字当摘要,结果推送 list 里看到的就是重复的标题。

新版:front matter 加 `digest:` 字段(单独写),脚本优先用 digest,缺省才 fallback title。

| | digest |
|--|--|
| 001 | 列了 5 年,纸划满了,人空了。后来换:每天 3 件 + 明确"不做"。反而做得更多。 |
| 002 | 戴大耳机、开 25 分钟钟,3 年深度工作。直到 25 分钟结束,笔记本上什么都没写。被打断也行。 |
| 000 | 每周一篇,可能有时候是废稿。这里是过程比结论值钱,草稿比作品诚实。 |

公众号个人订阅号 digest 限制 54 字,3 个 digest 都控制住了。

### 3. 新增开篇 000(品牌定位 + 联动 001)

`doc/essays/000-grass-journal-intro.md`,核心诉求:"一炮打响"。

**结构**:
1. **钩子**: "我想开一个公众号,想了 3 个月" + 朋友一句话("现在谁还看 / 我每天都看")—— 反共识真实对话
2. **为什么不叫"作品集"**: 建立"草稿本" = 过程 > 结论 / 草稿 > 作品的承诺
3. **内容预告**: 工具反思 / 创作过程 / 一些小观察
4. **调性一句话**: 死板冷静 / 不卖萌 / 不喊口号
5. **联动 001**: "第一篇是「5 年每日计划,我戒了」" + "下一篇看心情" —— 跟"没计划"系列调性一致
6. **收尾**: "发了。下周三见。(也可能周三见,也可能周四,看心情。)" —— 留白 + 重复 motif

**去 AI 味**:
- 不写"我做了 X 年 X,后来放弃了"模板(001/002 已经用了,开篇再用会腻)
- 删 3 items 列表("不卖萌、不喊口号、不立 flag" → "不卖萌、不喊口号")
- 删 3 items 系列("看到的、想到的、想吐槽的" → "看到的、想吐槽的")
- 收尾用单句留白("发了。"),不写"欢迎大家多多支持"类陈词

**4 张配图 + 1 张 cover**(全部去 IP):
- `cover.png` — 撕下草稿纸的瞬间 + 留白给标题
- `01-first-draft.png` — 桌面刚撕的草稿 + 半杯咖啡
- `02-draft-pile.png` — 一堆废稿 + 撕下来的纸屑
- `03-draft-detail.png` — 撕下来的草稿纸 + 字(部分划掉)
- `04-empty-desk.png` — 空桌面 + 1 张草稿 + 半杯咖啡(收尾)

`02-draft-pile.png` 生成出来 5.2MB,超微信 1MB 内联图限制。`sips -Z 1000` 压到 778KB。

### 4. 同步结果

用 `digest` 字段 + 修复后的 `md_to_wechat_html` 重跑 000/001/002:

| | 草稿 ID | 推送标题 |
|--|--|--|
| 000 | `4Qs6oAKtTbuKncYKGGbmXJBYKDl5-Y5a54Y918kBwVdmwlytVtCnsNun1SokKfjt` | 《为什么开一个"草稿本"公众号》 |
| 001 | `4Qs6oAKtTbuKncYKGGbmXAJLREvkU4_6FeqgzCFxuscCPrDZuZ0Xb2ooUvZrcr6a` | 《5 年每日计划,我戒了》 |
| 002 | `4Qs6oAKkTbuKncYKGGbmXAoiiklrUFQGRfgPke633cFEVAXzmHqepH4jCQgSRhvp` | 《番茄钟 3 年,我放下了》 |

### 5. 文件变更

- `doc/essays/000-grass-journal-intro.md`(新增)
- `doc/essays/images/000-grass-journal-intro/*`(新增 5 张)
- `doc/essays/001-why-i-dont-do-daily-plan.md`(标题 + digest)
- `doc/essays/002-focus-boundary.md`(标题 + digest)
- `xiaofan-ink/tools/articles-to-wechat.py`(加 digest 字段读取)
- `CHANGELOG.md`

### 6. 公众号发布顺序建议

1. **000(开篇)周三发**: 一炮打响,定调
2. **001(每日计划)下周三发**: 预告过,读者有预期
3. **002(番茄钟)再下周三发**: 跟 001 配对,讲"工具反思"

### 7. 用户后续

公众号后台 → 草稿箱 → 6 个草稿:
- v1.5 时代 2 个(标题/摘要都是老的)
- v1.5.1/1.5.2 时代 4 个(标题/摘要有 1.5.2 版)
- v1.6 时代 3 个(标题/摘要最新版,**这个先用**)

建议:全删 6 个旧草稿,只留 v1.6 的 000/001/002,然后按上面发布顺序发。

---

## v1.5.2 — 2026-07-17(去 AI 味重写 + 排版升级 + 修图)

修 4 个 1.5.1 留下来的问题:封面不贴内容、图片显示 bug、排版糙、文章 AI 痕迹重。

### 1. 文章去 AI 味(humanizer)

001/002 重写。用维基百科 24 种 AI 模式逐个排查,主要修复:

| 模式 | 001 改动 | 002 改动 |
|------|---------|---------|
| `**X**` 加粗结尾(机械强调) | 删 2 处 | 删 3 处 |
| "X 但 Y" 模板句 | "听起来很怪,但..." → "我也说不清为什么" | "专注像麻醉——你..." → "那 25 分钟我'在场'了吗?在场了" |
| 排比/对仗过工整 | 拆 1 处三段式 | 拆 2 处排比("憋气"重复) |
| "真正的成本不是 X,是 Y" | 不需要 | 改成 "我后来想,真正消耗我的可能不是..." |
| 模板收尾 | 改成"没列。嗯。" | 改成"在。嗯,反正'在'也不是什么必须一直保持的状态" |
| 缺第一人称 + 不确定 | 加 "我想不起来了" / "可能是因为" | 加 "我'在场'了吗" / "可能" |

**另外**:001 里的"专注像麻醉"在 001/002 都用了,会重复。改后 001 不再用这个比喻,002 改成更具体的"在场 / 没留下痕迹"。

### 2. 修图片显示 bug

001 的 markdown 引用 `images/001-.../01.png`,但实际文件叫 `01-paper-sunk.png`(002 的引用风格)。结果是图片在草稿里不显示,只看到 alt 文字。

**两处修复**:
1. **markdown 改对**:001 的 4 张图引用全部改成实际文件名(`01-paper-sunk.png` 等)
2. **脚本加 stem 前缀 fallback**:`sync_essay` 里的 `image_url_map` 多存几份,包括 `01.png` 这种短名形式,让 01.png → 01-paper-sunk.png 自动命中

以后写文章引用图时,既可以写全名也可以写短名。

### 3. 排版升级(md_to_wechat_html 重写)

旧版:手写 regex 解析,样式糙,不能处理 markdown 复杂结构。

**新版**:
- 用 `markdown` 库(3.10)+ `BeautifulSoup` + `lxml` 解析
- 走"markdown → HTML → bs4 后处理"两步,样式按 `brand/style-guide.md` 调色板/字号规范
- 关键样式:
  - 正文 17px / 行距 1.85 / 字间距 0.3px(公众号屏幕小,行距要够松)
  - H1(文章标题) 24px 加粗
  - H2(段落小标题) 18px 加粗 + 3px 红色左竖线(强调色)
  - 引用块 米色 #F4EFE6 底 + 3px 红色左竖线
  - 配图 居中、max-width 100%、无圆角无阴影(白底手绘感)
  - `<strong>` 默认红色 #C0392B(强调色,`accent` 参数可调)
  - 整段包 `<section>` + 移动端友好字体栈
- 去掉 `smarty` 扩展,避免把直引号 `"` 改成花引号 `""`(style-guide 规定用「」)
- 去掉 bs4 默认的 `<html><body>` 包装

### 4. 封面去 IP 化(顺手做)

旧 cover 还有小凡 IP,跟"封面 ≠ IP"的认知不一致。重新生成:

- **001 cover** —— 一张写满计划的纸,5 个 √ + 3 个 X + 1 个 ?,无角色
- **002 cover** —— 番茄钟 + 大红斜线 + 箭头 + "also 也行",无角色

封面留给标题位置更多,信息密度更高(看图就知道文章在讲什么)。

### 同步结果

用修复后的脚本重跑 001 + 002:
- 001 草稿 ID: `4Qs6oAKtTbuKncYKGGbmXB_8dRiEZZY3FYccTX0FK5_zCaiQaYAqIYr1v1bac9eh`
- 002 草稿 ID: `4Qs6oAKtTbuKncYKGGbmXJ6Gg-SSz1Dfkjfl8g8LlGohn__tKodgAyTxoDUk1Hsa`

### 文件变更

- `doc/essays/001-why-i-dont-do-daily-plan.md`(重写 + 修图引用)
- `doc/essays/002-focus-boundary.md`(重写)
- `xiaofan-ink/tools/articles-to-wechat.py`(重写 md_to_wechat_html + 加图片 fallback)
- `doc/essays/images/001-why-i-dont-do-daily-plan/cover.png`(去 IP 重出)
- `doc/essays/images/002-focus-boundary/cover.png`(去 IP 重出)

### 用户后续

公众号后台 → 草稿箱 → 找到新草稿(标题一样,看创建时间)→ 预览 → 群发/定时。
旧草稿(共 4 个:1.5 时代 2 个 + 1.5.1 时代 2 个)需要手动删除。

---

## v1.5.1 — 2026-07-17(中文编码修复 + 专门封面图)

修 v1.5 的 2 个问题:

### Bug 1:中文乱码

requests `json=payload` 默认 `ensure_ascii=True`,把中文转成 `\uXXXX` 转义字符串。公众号编辑器里看到 `\u300a\u4e3a\u4ec0...` 这种乱码。

**修复**:`create_draft` 改用 `data=json.dumps(payload, ensure_ascii=False).encode('utf-8')` + 显式 `Content-Type: application/json; charset=utf-8` 头。

### Bug 2:没有专门封面图

v1.5 默认用第一张配图(01-paper-sunk.png)作封面,导致"封面"跟"正文图 1"重复。

**修复**:
1. 脚本加 cover.png 优先检测(支持 `cover.png` / `cover.jpg` / `00-cover.png`)
2. 用 `image_synthesize` 为 001 + 002 各生成 1 张专门封面图,存到 `doc/essays/images/00X-*/cover.png`
3. cover 设计:留白更多(给标题位置),核心元素简化,视觉冲击强

**新增 cover 图**:
- `doc/essays/images/001-why-i-dont-do-daily-plan/cover.png`(小凡从纸堆探出 + 一手举笔)
- `doc/essays/images/002-focus-boundary/cover.png`(小凡卡在钟形罩里 + 大耳机 + 番茄钟)

**重新同步**:用修复后的脚本重跑 001 + 002,生成新草稿(中文正常,封面是 cover.png)。用户需要在公众号后台**删除旧草稿**。

---

## v1.5 — 2026-07-17(公众号 API 自动化)

为"小凡的草稿本"公众号接 API 自动化,实现从 essay 到草稿箱的端到端同步。

**新增 `xiaofan-ink/tools/` 目录**:
- `articles-to-wechat.py` — 主脚本(11KB,~330 行)
  - 读 `doc/essays/00X-*.md` + front matter
  - 读配图目录 `doc/essays/images/00X-*/`
  - 获取/缓存 access_token(2 小时过期)
  - 上传所有配图到"图文消息内图片"API(获取微信 URL)
  - markdown → 微信公众号兼容 HTML(图片用微信 URL 替换)
  - 上传第一张图作封面(永久素材,thumb_media_id)
  - 创建草稿(draft/add)
  - 返回 draft_media_id,公众号后台手动群发/定时
- `config.example.json` — 配置模板(填 AppID/AppSecret,git 跟踪)
- `config.json` — **本地凭证文件(包含真实 AppID/AppSecret,gitignored)**
- `.token_cache.json` — access_token 缓存(gitignored)
- `README.md` — 使用说明 + 故障排查

**微信 API 集成要点**:
- API 基础 URL: `api.weixin.qq.com/cgi-bin/*`
- access_token: 2 小时过期,本地缓存自动复用
- 图片上传:图文消息内图片 API(`media/uploadimg`)返回 URL,永久素材 API(`material/add_material`)返回 media_id
- 草稿创建: `draft/add` API,content 字段是 HTML(不是 markdown)

**公众号凭证**:
- AppID: `wxa1b727ef169d0b3e`(本地 `config.json`)
- AppSecret: 本地 `config.json` 保存,git 忽略
- 状态:已申请、已加白名单、API 连接测试通过
- 公众号类型:个人订阅号(每天可群发 1 次,需要手动)

**实战验证**:
- 001 essay 同步成功(草稿 ID: `4Qs6oAKtTbuKncYKGGbmXF8noMWHjrkPyB5GlIKLbz9dB3wV6yFl6dIVEvENvCJF`)
- 002 essay 同步成功(草稿 ID: `4Qs6oAKtTbuKncYKGGbmXDThxtITnZwYu0gteQuou0Cezn0xqmWuk8Shida1JxHe`)
- SERIES-STATE 状态更新:两篇都是 "✅ 草稿已创建(待手动群发)"

**front matter 修复**:
- `n: 001` → `n: "001"`(加引号)让 yaml 保留为字符串
- `date: 2026-07-17` → `date: "2026-07-17"` 同理
- 避免 yaml 把 "001" 解析成 int 1 导致前导 0 丢失

**`.gitignore` 新增**:
```
xiaofan-ink/tools/config.json
xiaofan-ink/tools/.token_cache.json
```

**安全纪律**:
- 真实 AppID/AppSecret 永远不进 git
- 凭证丢失/泄露:立刻去公众号后台"重置 AppSecret"
- 跑脚本前确认 `config.json` 没被 commit

**后续可选扩展**:
- 公众号 API 自动化群发(需要高级群发权限,个人订阅号没有)
- 多平台同步(知乎/小红书/Newsletter)
- 自动定时发布(Cron + 脚本)
- 数据看板(阅读/在看)

---

## v1.4 — 2026-07-17(公众号"小凡的草稿本" brand 资源)

为微信公众号申请做准备,建立完整 brand 资源库,跟 xiaofan-ink skill 内容库解耦。

**新增 `brand/` 目录**:
- `brand/README.md` — 公众号基础信息 + 简介(主用 / 备选 1 / 备选 2)
- `brand/avatar.png` — 头像(1:1 撕下草稿纸 + 小凡简笔 + 暖色 highlight,圆形裁切友好)
- `brand/welcome.md` — 关注欢迎语 + 6 个关键词自动回复(目录/草稿/投稿/关于/ip/草稿本)
- `brand/menu.md` — 公众号自定义菜单(3 个一级菜单设计:草稿本/草稿碎片/关于小凡)
- `brand/style-guide.md` — 视觉规范(配色/字体/排版/封面/头图/不做的事)

**公众号"小凡的草稿本"基本定位**:
- 名:`小凡的草稿本`(6 字,跟 001 主题"写废稿"呼应)
- 简介(主用):`过程比结论值钱的实验。写点工具反思、节奏、专注,跟"小凡"一起想。`
- 调性:deadpan 冷静 / 反思 / 冷幽默 / 不卖萌 / 不喊口号
- 关联仓库:xiaofan-ink(本仓库)
- 关联系列:《小凡墨水周记》(`doc/essays/`)
- 更新:每周三 1 篇(~~v1.7 改为"想写就写"~~)
- 类型:个人订阅号

**整体项目结构更新**:
- 顶层 `README.md` 目录树增加 `brand/` 段,标注"v1.4+ 公众号 brand 资源"
- `doc/essays/README.md` 顶部加"关联公众号:小凡的草稿本",末尾加"发布到公众号"小节
- 实战 1/2/3 顶部"非 essays 正式系列"注保留
- 实战样本职责继续划清

**后续可扩展**:
- 公众号 API 自动化推送(把 `doc/essays/00X-*.md` 推到公众号草稿箱)
- 公众号菜单"最新文章"自动同步脚本
- 关注自动回复 + 关键词回复上线

---

## v1.3 — 2026-07-17(系列第 2 篇 + 托管创作规则升级)

### CREATION-PLAN 规则升级

- **主题由 agent 自主决定**:用户只给"创作一篇"触发,agent 从角度池+历史避重里选(默认走 B 模式)
- **图片不固定张数**:按认知锚点数量决定(3-6 张灵活),不再固定 4 张
- **用户参与减少**:不参与选主题,只审稿+决定发布到哪里(发布平台后续可托管)

### 系列第 2 篇(《专注力的边界》)

- 文章:`doc/essays/002-focus-boundary.md`(约 600 字,5 段)
- 5 张配图:`doc/essays/images/002-focus-boundary/01-05.png`
- 实战 prompt 库:`xiaofan-ink/assets/prompts/articles/002-focus-boundary.md`

### 第 2 篇轮换记录

- 表情:3 default + 1 confused + 1 satisfied (3 种,5 张图)✓ 符合 SERIES-STATE
- 装扮:1/5 用(咖啡杯,只在图 04)
- 姿态:5 different(卡钟形罩 / 坐空桌 / 卡门槛 / 端咖啡 / 站桌)
- 物件:钟形玻璃罩 / 番茄钟 / 笔记本 / 门 / 白板(全部新)

### 主题配对策略

002 跟 001 形成"反思时间管理"姐妹篇:
- 001:列计划(节奏类)
- 002:深度专注(专注类)
- 角度不同但主题相邻,形成系列内部连贯性

### takeaway(给下一篇用)

- 满足表情 prompt 措辞仍然不够明显(连续 2 篇问题),第三次验证:下次"嘴角上扬"组合"半闭眼"或"almost-smile"
- 卡门槛类的"门/框/边界"姿态,身体位置要明显在中间,脚不要伸出去
- 端杯子时让小凡放松(肘撑桌)比"教学性按笔记本"更自然

---

## v1.2 — 2026-07-17(长期创作计划 + 系列首发)

建立《小凡墨水周记》正式系列,把仓库从"skill 验证库"升级到"长期创作内容库"。

**新增文档**:
- `doc/CREATION-PLAN.md` — 长期创作规范(系列定位/节奏/结构/流程/决策/基础设施/长期视角)
- `doc/SERIES-STATE.md` — 防重复数据库 + 三维轮换状态跟踪(姿态/装扮/物件已用未用清单)
- `doc/essays/README.md` — 系列说明,跟实战样本划清职责

**新增目录**:
- `doc/essays/` — 正式发布内容(从 001 开始)
- `doc/essays/images/00X-<slug>/` — 配图(同号子目录)

**新增内容**(系列第 1 篇):
- `doc/essays/001-why-i-dont-do-daily-plan.md` — 《为什么我不再做每日计划》(约 600 字,4 段)
- `doc/essays/images/001-why-i-dont-do-daily-plan/01-04.png` — 4 张配图
- `xiaofan-ink/assets/prompts/articles/001-why-i-dont-do-daily-plan.md` — 实战 prompt 库

**第 1 篇轮换记录**(严格执行 SERIES-STATE 防反复刻):
- 表情:2 默认 + 1 困惑 + 1 满足(实战 3 用了思考/疲惫,本次换困惑/满足)
- 装扮:1/4 用(咖啡杯,实战 2 用过耳机/工具包/笔记本,实战 3 没用)
- 姿态:4 种全部为新(卡纸堆 / 洞里伸手 / 蹲角落 / 站回头)
- 物件:纸堆 / 洞 / 桌(实战 1-3 没用过)

**实战样本划清职责**:
- `doc/whiteboard-vs-doc.md` / `doc/why-i-quit-gtd.md` / `doc/why-i-write-drafts.md` 顶部加"状态:skill 实战验证样本,非《`essays/`》正式系列"
- 这 3 篇继续作为 skill 能力展示,但不计入正式系列

**系列元决定**(拍板项,~~部分 v1.7 调整~~):
- 系列名:《小凡墨水周记》
- 频率:每周 1 篇(每周三) → **v1.7 改为"想写就写"**
- 长度:600-1000 字
- 配图:4 张(~~v1.3 改为"不固定 3-6 张"~~)
- 视觉:warm-ink 4 色,小凡 deadpan 默认 + 1-2 种微表情

**第 1 篇 takeaway(给下一篇用)**:
- 收尾用满足时 prompt 措辞要更明显("slight 1-2mm mouth upturn" 不够,改 "slight 3-4mm mouth upturn" 或加 "almost-smile")
- "试图接" + "困惑" 组合容易让 body 跟 face 不连戏,要么统一方向要么去掉意图
- 桌面/桌子的"满"会挤压小凡,小物件(杯/瓶/小盒)效果更好

---

## v1.1 — 2026-07-17(实战 3 — 表情库首篇实战)

基于 v1.0 新增的"微表情库",写第三篇实战示例文章,验证表情库在实战中的效果。

**新增文章 + 配图**:
- `doc/why-i-write-drafts.md` — 第三篇实战文章(约 600 字)
  - 主题:为什么我开始主动写"废稿"(写作方法反思)
  - 4 段配 4 张图,1 个结论
- `doc/images/why-i-write-drafts/01-draft-pile.png` — 废稿堆(deadpan 默认)
- `doc/images/why-i-write-drafts/02-three-openings.png` — 三个被划掉的开头(思考表情)
- `doc/images/why-i-write-drafts/03-rewrite.png` — 推倒重来(疲惫表情)
- `doc/images/why-i-write-drafts/04-real-cost.png` — 成本是废稿(deadpan 默认)

**新增实战 prompt 库**:
- `xiaofan-ink/assets/prompts/articles/why-i-write-drafts.md`
  - 4 张图各自的 5 段 prompt(Theme/Structure type/Core idea/Composition/Chinese labels)
  - 表情选词理由 + 表情使用复盘
  - 反复刻陷阱预标记

**表情使用复盘**:
- 4 张图用了 **2 默认 + 1 思考 + 1 疲惫**
- 情绪节奏:平 → 思考 → 疲惫 → 平(完整呼吸)
- 4 张图全部一次过,无重出
- 表情库设计验证成功:微表情在 deadpan 底色上有效传递 1 度情绪,又不破坏"白板随手画"清冷气质

**实战结论**:
- 表情库使用纪律(同文最多 2-3 种 + 一旦加表情必须删掉 deadpan)在实战中可操作
- prompt 替换词(`slightly raised right eyebrow, eyes looking down-left` 等)直接生效,没额外 trigger 错误风格
- 表情库和备选装扮(本篇未用)可独立/叠加使用,互不冲突

**walkthrough 扩展**:
- `doc/walkthrough.md` 顶部"准备工作"段加表情库提示
- 新增"7.6 表情库怎么用?"FAQ 段
- 新增"8. 附录 B:实战案例集"section,含实战 1/2/3 三篇对比表 + 实战 3 表情库实战细节
- 实战案例集定位:作为后续实战的参考,展示表情库如何从 v0.5 反复刻陷阱 → v0.6 改进 → v1.0 表情库的战绩

---

## v1.0 — 2026-07-17(微表情库)

基于 deadpan 底色,加 5 个微表情变体,让"小凡-读者"的情感连接更具体。

**新增 5 张表情变体**(`xiaofan-ink/assets/ip-reference/variants/`):
- `07-thoughtful.png` — 思考(右眉微挑 / 眼斜看 / 嘴闭)
- `08-confused.png` — 困惑(眉心微聚 / 眼微眯 / 嘴微松)
- `09-tired.png` — 疲惫(眉尾下垂 / 眼半闭 / 嘴松)
- `10-surprised.png` — 惊讶(眉上挑 / 眼睁大 1.2x / 嘴微张)
- `11-satisfied.png` — 满足(嘴角微扬 1-2mm / 眼微眯 / 眉平)

**风格校准**:
- 5 张全部用 standard.png 作 input_file_paths,跟现有 01-06 outfit 变体完全一致
- 全部保持纯线稿无填色,跟 standard.png / head-think.png 等核心参考图风格一致
- 表情都是 deadpan 底色上的 1 度微变化,**不是大表情** — 不会触发"日漫/吉祥物/表情包"错误风格

**文档更新**:
- `xiaofan-ink/references/xiaofan-ip.md` — 新增"表情库(可选用)"section
  - 列出 5 个微表情及适用场景
  - 强调"微表情,不是夸张五官"
  - 强调"表情库和备选装扮可叠加,但一张图最多 1 表情 + 1 装扮"
- `xiaofan-ink/assets/prompts/_standard-ip-description.md` — 新增"表情选项(可选用)"section
  - 表情-prompt 用词对照表(英文 prompt 替换词)
  - 提供带表情的 IP 描述段示例
- `xiaofan-ink/references/prompt-template.md` — 新增"表情选择(可选用)"section
  - 明确"默认 deadpan 即可,什么时候用表情"
  - 表情使用纪律(同文最多 2-3 种 + 一旦加表情必须删掉 deadpan)
  - 3 个实战示例(默认 / 思考 / 满足)

**表情使用纪律**:
- 默认一律 deadpan,不要每张图都加情绪
- 同一篇文章里,多张图最多 2-3 种不同表情
- 一旦加表情,IP 描述段里 `deadpan calm expression` 必须删掉,避免和表情词冲突

**为什么是 v1.0**:
- 之前 v0.x 阶段是"个人用、私有项目阶段"
- v1.0 是"表情库建立完整"的里程碑 — IP 三维度全部到位(姿态/装扮/表情)
- 后续如果公开,从 v1.x 继续

---

## v0.9 — 2026-07-17(prompt 库对齐"线稿版的我"基准)

基于 v0.8 确立的"线稿版的我"IP 风格,统一重写 prompt 库。

**新增**:
- `xiaofan-ink/assets/prompts/_standard-ip-description.md` — 小凡 IP 标准描述(头部/身体/线条/颜色/标准 prompt 段)
  - 明确"线稿版的我,不是极简 stick figure"
  - 列出反面描述(不要写进 prompt 的:minimalist/whiteboard quick sketch/no color fill 等)
  - 列出标准 prompt 段(开头 + IP 描述),后续所有实战 prompt 引用

**重写**:
- `xiaofan-ink/references/prompt-template.md` — 主模板
  - 拆分为 5 段(风格+IP/变量/构图/标注/约束)
  - 明确"必须用 standard.png 作 input_file_paths"
  - 引用标准 IP 描述
- `xiaofan-ink/assets/prompts/articles/whiteboard-vs-doc.md` — 实战 1 prompt
  - 改用 standard.png(原 reference.jpg)
  - 引用标准 IP 描述
- `xiaofan-ink/assets/prompts/articles/why-i-quit-gtd.md` — 实战 2 prompt
  - 改用 5 段结构(跟实战 1 对齐)
  - 引用标准 IP 描述
- `xiaofan-ink/assets/prompts/skill-samples/all-6-samples.md` — 6 样例 prompt
  - 改用 standard.png
  - 改用 5 段结构
  - 引用标准 IP 描述

**统一原则**:
- 所有实战 prompt 用同一开头段("Generate a 16:9 ... casual hand-drawn line illustration ...")
- 所有实战 prompt 用同一 IP 描述段("Xiaofan is a loose line-drawn self-portrait with recognizable features ...")
- 所有实战 prompt 引用 standard.png
- 配色统一 warm-ink 4 色(黑/红/橙/蓝)

## v0.8 — 2026-07-17(IP 形象回滚到 1a25ff2 v0.4 基准)

**问题发现**:
- 用户在仔细看 `02-two-breakpoints.png` 时发现左上角有真实证件照(图像模型复粘贴),这暴露了 v0.5/v0.6 出的 6 张样例图都是"日漫精致线稿"风格
- 进一步发现 v0.5/v0.6 出的图虽然"日漫",但有详细面部特征(像"我"),新出的 14 张反而偏"白板极简"或"无颜色填色",识别度变差
- 用户认为 `1a25ff2` (v0.4 实战 1) 的 IP 形象最适合,作为基准

**回滚 IP 形象(用 `git show` 从历史 commit 提取到当前路径)**:
- 实战 1 4 张 (`doc/images/whiteboard-vs-doc/`) → 从 `1a25ff2` 恢复
- 实战 2 4 张 (`doc/images/why-i-quit-gtd/`) → 从 `431c634` 恢复(本来就一致)
- 6 张样例 (`xiaofan-ink/assets/examples/`) → 从 `d341621` 恢复
- 3 张 IP 定稿 + `standard.png` → 保持 v0.5 版本(没被改过)
- 6 张备选装扮 (`variants/`) → 保持 v0.6 版本(没被改过)

**保留所有其他优化**:
- v0.5 全面优化(配色、CHANGELOG、prompt 库、备选装扮、实战复盘)
- v0.6 实战第二篇
- v0.7 目录结构清理(`doc/images/` 子目录、`prompts/` 子目录改名等)
- v0.2 配色方案(温暖墨水感 4 色 HEX)
- v0.3 walkthrough 文档
- v0.4 实战第一篇(用回滚后的图)

**教训记录**:
- 图像模型对"详细面部"会自动触发"商业插画/日漫"风格,对"极简面部"会失去识别度
- "白板速写感 + 像用户"在当前 prompt 策略下无法同时达到
- **后续实践**:接受"线稿版的我 + 颜色填色"作为 IP 风格基准,不追求极致白板速写

## v0.6 — 2026-07-17(13 张图重出 + 实战第二篇 + 新备选)

- **13 张旧图 v1 → v2 重出**:
  - 3 张 IP 定稿图(`head-think` / `halfbody-climb` / `scene-stuck`):基于 `standard.png` 重出,脸一致性提升
  - 6 张样例图(`01-chaos-to-focus` 到 `06-trust-bridge`):基于 `standard.png` 重出
  - 4 张实战第一篇(`01-doc-trap` 到 `04-process-wins`):基于 `standard.png` 重出 + **刻意"非站"姿态**(蹲/探出/坐/卡住)
- **3 张新备选装扮**(`xiaofan-ink/assets/ip-reference/variants/`):
  - `04-headphones.png`(大耳机 — 专注/逃避场景)
  - `05-coffee.png`(咖啡杯 — 慢节奏/思考场景)
  - `06-notebook.png`(小笔记本 — 记录/反思场景)
  - `xiaofan-ip.md` 备选装扮段扩充
- **第二篇实战文章**:`doc/why-i-quit-gtd.md` + 4 张配图(`gtd-01-04.png`)
  - 主题:为什么我不再用 GTD 了(工具反思)
  - 验证 v0.5 改进:姿态全部"非站" + 3/4 用备选装扮
  - 4 张图核心物件都不同(GTD 机器/清单山/3 张纸/坏 GTD 机器)
- **实战 prompt 库扩充**:
  - 新增 `articles/why-i-quit-gtd.md`(v2 实战 prompt + 实战复盘)
  - 对比第一篇实战:姿态 1.5 维 → 4 维,备选 0/4 → 3/4

## v0.5 — 2026-07-17(全面优化迭代)

全部 7 项优化一次性合并(根据用户优先级判断:全部一起做)。

- **P0 IP 一致性**: 新增 `xiaofan-ink/assets/ip-reference/standard.png`(标准像,从 `head-think.png` 复制)。后续所有新图用 standard.png 作 input_file_paths,不再直接用原始证件照。13 张旧图(v1)保留,在 prompts 文件里标注。
- **P1 实战 prompt 库**: 新建 `xiaofan-ink/assets/prompts/` 目录,分 `articles/` 和 `skill-samples/` 两类。实战文章的 4 个 prompt + 6 张样例图 prompt 都存档,后续直接复用。
- **P2 反复刻规则实战验证**: `composition-patterns.md` 加"实战反复刻陷阱"段,记录第一篇实战(白板 vs 文档)的两个反复刻陷阱(姿态都偏站 / 物件都偏低科技机器)+ 避免方法。
- **P3 CHANGELOG**: 创建本文件。
- **P4 IP 备选装扮**: `xiaofan-ip.md` 加"备选装扮"段(眼镜/白板笔/工具包)。生成 3 张备选图到 `xiaofan-ink/assets/ip-reference/variants/`。
- **P5 文档瘦身**: README 简化(去安装段/相关项目段);NOTICE 简化(去 fork 声明,保留原作者版权)。
- **P6 中文字体**: `style-dna.md` 加一行"中文标注倾向手写体"。

## v0.4 — 2026-07-16(实战示例文章)

- 新增 `doc/whiteboard-vs-doc.md` — 一篇中文思维方法短文(约 500 字)
- 新增 `doc/images/01-04.png` — 4 张用 xiaofan-ink 生成的 16:9 配图
  - 01-doc-trap.png / 02-whiteboard-better.png / 03-three-strokes.png / 04-process-wins.png
- 主题契合 xiaofan-ink 审美(白板草图感)

## v0.3 — 2026-07-16(walkthrough + 配色引用同步)

- 同步最新配色方案引用到顶层文档(SKILL / README / qa-checklist 各加一行)
- 新增 `doc/walkthrough.md` — xiaofan-ink 完整使用 walkthrough(从文章到配图的完整流程示例)
- 包含:准备工作 / 示例文章 / 锚点提炼 / shot list / 完整英文 prompt / QA / 交付 / 常见问题 / 配色速查

## v0.2 — 2026-07-16(配色方案升级)

- 配色方案升级:概念色 → 温暖墨水感具体 HEX
- `style-dna.md` 加调色板表(4 色 HEX + RGB + 用途)
  - 黑色 (ink) `#1A1A1A` / 红色 (alert) `#C0392B` / 橙色 (path) `#E67E22` / 蓝色 (note) `#2C5F8D`
- `prompt-template.md` 同步英文 Color use 段

## v0.1 — 2026-07-16(fork + IP 替换)

- 从 [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) fork
- 视觉 IP 从原作者的"小黑"替换为"小凡"(基于真人面部特征风格化转译)
- 项目名 `ian-xiaohei-illustrations` → `xiaofan-ink`(小凡墨水)
- 同步 GitHub 仓库名为 `xiaofan-ink`,本地 `.git/config` 同步
- `references/xiaohei-ip.md` 改名为 `xiaofan-ip.md` 并重写
- 同步更新 `prompt-template.md` / `composition-patterns.md` / `qa-checklist.md` / `SKILL.md` / `openai.yaml` / `README.md` / `NOTICE.md` / `examples/prompts.md`(已移到 `.ip-dev/legacy-examples/legacy-prompts.md`)
- 暂存原 14 张样例图到 `.ip-dev/legacy-examples/`(gitignored)
- 新增 6 张小凡样例图到 `xiaofan-ink/assets/examples/`(覆盖 6 种结构类型)
- 新增 3 张小凡 IP 定稿图到 `xiaofan-ink/assets/ip-reference/`(头部/半身/场景)
- `.gitignore` 加 `.ip-dev/` 排除开发期临时文件

---

## 版本约定

- **v0.x**: 个人用、私有项目阶段,版本号从 0.1 开始
- 每次有"功能级别"的改动(加新文件 / 改核心 references / 加新 IP 元素)升级小版本
- 修小 bug / 改文案 / 优化单张图,**不进** CHANGELOG,只进 git log
- 公开版本(如果未来要公开)从 v1.0 开始
