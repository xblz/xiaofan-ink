# 040 配图 · 我搜了 1 个东西, 搜了 8 次

> 生成: 2026-10-26 · 模型: matrix generate_image 2K 16:9
> 全部 1376×768 · ffd8 JPEG + .png 后缀
> **v2.8.43 重画**: 00 / 02 / 03 三张含 IP 的图全部重画 (原 v3 版本 IP 形象失真, 备份在 `v3/`)

## 5 张图

| 文件 | 形态 | 内容 | IP | 文字 |
|---|---|---|---|---|
| `00-cover.png` | **场景叙事型** | 餐桌前低头双手举手机, 长袖衬衫, 窗帘+窗外树+马克杯+笔记本+眼镜+盘子 | ✅ 正面可见 | 8 次 (橙) |
| `01-history.png` | **物件特写型** | 手举手机, 搜索框「停车」+ 8 条空行 + 1 条红框, 桌面/书架/台灯/绿植/窗外天际线 | no | 停车 (灰) |
| `02-drawers.png` | **信息图解型** | 红框「IMG_0472」+ 4 分支(对话框/相框/笔记本/信封) + 2 红勾 2 橙叉 + 4 条连线, 书桌场景 + 拿笔背影 | 背影 | IMG_0472 (蓝) |
| `03-floor.png` | **场景叙事型** | 蹲在客厅地毯上把散落的照片拢成一堆, 手机放在旁边, 长袖, 沙发/靠垫/落地灯/书架/绿植 | ✅ 正面可见 | 800 张 (灰) |
| `04-quote.png` | 纯文字 | 两行 punchline | no | 我从来没搜不到过它 / 只是没给它起过名字 |

**IP 密度 2/5** (00 + 03), 位置在 00 和 03 — 满足 v2.8.18 防失联硬规则, 且 02 用背影人物做锚点。

## 形态说明 (v2.8.41 公众号专用)

这 5 张**不是** 039 那种"空壳符号型"。三种成熟形态都用了:

- 场景叙事型 (00 / 03) — 参照 019-03 (1007 阅读)
- 信息图解型 (02) — 参照 015-01 (1007 阅读)
- 物件特写型 (01) — 参照 019-02

**判据检查: 删掉人物后图还成立吗?** 00 / 03 删掉人物就只剩一个空房间, 不成立 ✅

## ⛔ v2.8.43: IP 形象失真事故与修正 (本轮核心)

### 出了什么事

v3 版本(修完形态、没修 IP)的 00 / 03 两张图, 用户反馈 **"IP 形象完全不对"**。

回查仓库文档 + 对比历史高分配图后定位: **不是渲染器的锅, 是规范自己把 IP 改坏了。**

`xiaofan-ink/references/xiaofan-ip.md` 写得很清楚:

> - **碎短发**:黑色,**有刘海覆盖额头** …
> - **眉毛**:不刻意画,或用**非常淡的短斜线**
> - **眼睛**:细长,常用一笔短弧 + 一个点
> - **脸型**:偏长椭圆,下颌线干净

对照 `assets/ip-reference/standard.png` 和 `019-mute-moments/03-thinking-morning.png` (1007 阅读, 唯一被用户确认"没问题"的 IP 大图) 也是同一套特征。

**但 v2.8.42 的「眉毛专项」把刘海和眉毛一起干掉了。**

| 规范条款 | 本意 | 实际后果 |
|---|---|---|
| `NO eyebrows at all` + "额头是空白纸" | 禁粗黑眉 | 连**淡短眉**也禁了 → 无眉脸 |
| "改正面微侧 + **头发后梳**露出额头" | 让禁令生效 | **抹掉刘海** → IP 从碎发少年变成背头成熟男 |
| "眼睛 = 一笔短弧 + 一个平黑点 (2%)" | 禁动漫眼 | 渲染器画成**两个黑豆眼**, 比动漫眼更失真 |
| `手只画 3-4 strokes, fingers together` (v2.8.37) | 线稿手 | 锁死了标准图里**有体积、有指节、手指分开**的手 |

### 历史判断的修正

**「眉毛/眼睛细节 = 读者敏感点」是错的。**

038 反馈"形象不是很像" → v2.8.37 加五官禁写 → 之后所有图变"短弧+点+无眉+无刘海"。
但 **019-03 (1007 阅读) 是刘海 + 眉毛 + 细长眼, 用户从未反馈 IP 不像**。

**结论: 对公众号读者来说, 眉毛和眼睛的细节不构成"像不像"的判断依据;
发型(刘海)、脸型、线条质感才是。**
以后遇到"脸不像", **先查发型和脸型, 不要先去砍五官**。

### v2.8.43 新的 IP 描述段 (已写入规范)

- 刘海改成**正向必写**: `A spiky pointed fringe falls across the forehead … The fringe MUST be visible on the forehead` + 一串否定式 (`NOT slicked back, NOT combed back …`)
- 眉毛从禁令改成**正向**: `extremely faint, thin, short slanted strokes … much lighter than the hair`
- 眼睛从"短弧+平黑点"改成**细长眼缝**: `ONE thin elongated line … with ONE tiny solid black dot at the INNER corner. NO white of the eye, NO eyeball, NO round pupil`
- 手从"3-4 笔"改成**有指节、手指分开**
- 新增**线条质感段**: `loose and sketchy … flying-white gaps … lines that do not close … NOT clean vector art, NOT polished commercial line illustration`

### 第二轮才暴露的问题: 填充

刘海/眉毛修回来后, 三张图的**头发全被填成实心黑块**(第 1 轮), 修完又太浅像白发(第 2 轮), 第 3 轮才对。

根因: `Pure line drawing. Do NOT fill any clothing, hair or object with solid black or grey.` **这条抽象禁令管不住**。

修法(跟 v2.8.39「风格段自我诱发」同一个道理 —— **正向具体描述压过抽象禁令**):

```
EVERYTHING is thin black pencil lines on white paper. NOTHING is filled in with solid colour.
Hair is drawn with a few loose sketchy strokes that let the white paper show through the strands,
never a solid black shape, never a black silhouette, never flat black.
...
HAIR DENSITY - the hair must be built from MANY separate overlapping black strokes, short
directional strand lines, so the hair reads clearly DARK like black hair, while individual
strand lines and small white gaps stay visible inside it.
```

**"黑"和"线稿质感"要同时给**, 只给一头就会跑到另一个极端。

## 验收记录

### v3 轮 (形态修完, IP 失真)

| 轮次 | 图 | 问题 | 处理 |
|---|---|---|---|
| v1 | 00 | 粗黑眉毛 + 眼睛点带高光 (立体瞳孔) | 重画 |
| v1 | 03 | 眉毛 (细短但清晰) | 重画 |
| v2 | 00 | 眉毛仍在 (侧脸时刘海末梢被当眉毛) | 重画 |
| v2 | 03 | ✅ 眉毛消失, 眼睛短弧+平黑点 | 保留 |
| v3 | 00 | ✅ 眉毛消失, **正面微侧 + 刘海后梳露出额头** | 保留 |

> v3 的"后梳"就是**事故根因** —— 为了消灭眉毛, 把 IP 最核心的识别特征删了。

### v2.8.43 轮 (IP 修正)

| 轮次 | 图 | 问题 | 处理 |
|---|---|---|---|
| r1 | 00 | 刘海/眉毛回来了 ✅, 但**头发实心黑块** | 重画 |
| r1 | 03 | 同上 | 重画 |
| r1 | 02 | **头发实心黑块** + 手过度写实 | 重画 |
| r2 | 00 | 头发**太浅, 像白发** | 重画 |
| r2 | 02 | 头发**又是实心黑块** | 重画 |
| r2 | 03 | ✅ 头发黑度对, 但**粗黑眉 + 黑豆眼 (日漫脸)** | 重画 |
| r3 | 00 | ✅ 淡短眉 + 细长弧线加内眼角小点 | **保留** |
| r3 | 03 | ❌ 同样问题 | 重画 |
| r4 | 03 | ✅ 眉眼通过 | **保留** |
| r3 | 02 | ❌ 4 条分支连线断了 + 衣服排线脏 | 重画 |
| r4 | 02 | ✅ 四条连线完整, 衣服干净 | **保留** |

**最终 5/5 通过。** 裁切放大验脸 2 次 (第三轮 00/03, 第四轮 03)。

## 落实的 style-guide §3.6 硬规则

- ✅ **手机正拿** — 00 / 03 屏幕朝自己, 读者看到手机背面 + 人物脸
- ✅ **季节** — 10 月杭州 = 春秋过渡, 两张 IP 图都写了 `long-sleeve shirt`
- ✅ **IP 出现频率** — 2/5, 位置 00 + 03, 加 02 背影锚点
- ✅ **不画具体 app 内容** — 屏幕没有界面
- ✅ **无英文** — IMG_0472 是文件名不是英文单词

## 踩坑记录

**教训一: 过度矫正比不矫正更糟。**
为了消灭一个次要特征(眉毛), 代价是删掉核心识别特征(刘海)。
**每次加禁令前先问: 这条禁令会不会连带干掉别的东西?**

**教训二: 抽象禁令管不住填充, 正向描述才行。**
`Do NOT fill ... with solid black` 管不住; `Hair is drawn with many overlapping strokes that let white paper show through` 才管住。

**教训三: "黑"和"线稿质感"必须同时给。**
只说"别填充" → 头发变白发; 只说"要有黑度" → 头发变实心块。
**两句话要写在一起。**

**教训四: 连线/连接线是信息图解型的隐藏坑。**
02 的四个分支图标画对了, 但连接线断了, 图还是废的。
**验收信息图解型要专门看连线是否完整、是否真的接到两边。**
