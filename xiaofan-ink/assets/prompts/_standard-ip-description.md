# 小凡 IP 标准描述(v0.8 基准)

> 这是基于 1a25ff2 (v0.4 实战 1) 的"线稿版的我"风格基准,所有实战 prompt 的 IP 描述段都应该引用这个标准。
> 详细 IP 设计原理见 `xiaofan-ink/references/xiaofan-ip.md`。
> 风格调色板见 `xiaofan-ink/references/style-dna.md`。
> 反复刻规则见 `xiaofan-ink/references/composition-patterns.md`。

---

## 核心原则

- **线稿版的我,不是极简 stick figure**:保留详细面部特征(细长眼/脸型/刘海/薄唇),**不能简化成两点+一横**
- **白板感靠"线条松散"实现**,不靠"面部极简"实现
- **接受颜色填色**(在物件、标注、衣物等地方可以有少量色块)

## 视觉特征(头部, v2.8.30 简化)

> **核心**: 整体五官能看出是 IP 即可,不强制每个特征都在文字描述里写一遍。reference image `standard.png` 是主参考。

- 碎短发:有刘海覆盖额头,黑色,几笔速写
- 脸型:偏长椭圆,下颌线干净
- 眼睛:细长(两笔短弧即可)
- 头像偏大(略大于身体),保证"线稿版的我"识别度

> 实战 prompt 里**不强制**每次都列这些 — 用"matching the IP reference standard.png" 替代细节列出。

## 身体

- 细线条小人,手绘速写感
- 上身简单 T 恤或衬衫(简笔几笔)
- 腿是简单线条,不要肌肉感
- 站/蹲/卡住/探出/坐 等姿态都要"做事中",不摆拍
- 头像:身体 ≈ 1:3 ~ 1:4(头略大,不是日漫 Q 版那种极端大头)

## 线条风格

- 黑色线稿为主
- 线条松动、有轻微飞白、不闭合
- 像"白板随手画的草图"质感,但**保留详细面部特征**
- 不用颜色填肤色,只有少量颜色用于中文标注和小物件

## 颜色(温暖墨水感调色板)

- 黑色 (#1A1A1A) — 主体线稿、小凡
- 红色 (#C0392B) — 重点批注、问题、结果
- 橙色 (#E67E22) — 主流程、路径、箭头
- 蓝色 (#2C5F8D) — 补充说明、系统状态
- 每次 1-2 种标注色,不要超过 3 种

## 参考输入图

- 始终用 `xiaofan-ink/assets/ip-reference/standard.png` 作 input_file_paths
- 不要用原始证件照(已从 .ip-dev/legacy-examples/ 移走)

## 表情选项(可选用,默认保持中性即可)

实战 prompt 的 IP 描述段里,**默认不写表情** — 靠 standard.png reference 自然呈现。如果当前图需要 1 度情绪传递,可在 IP 描述段里**选择性补充**(都是微表情,不要大表情):

| 情绪 | prompt 用词(可选) | 适用场景 | 参考图 |
|------|---------------------|----------|--------|
| **默认** | (不写) | 绝大多数场景 — 靠 standard.png 自然呈现 | `standard.png` |
| 思考 | `slightly raised right eyebrow, eyes looking down-left, mouth closed` | 想 / 琢磨 / 找原因 | `variants/07-thoughtful.png` |
| 困惑 | `slightly furrowed brows, eyes half-closed, mouth slightly relaxed` | 看不懂 / 不确定 / 卡住 | `variants/08-confused.png` |
| 疲惫 | `drooping brows, eyes half-closed, mouth loose` | 累 / 加班 / 反复试错 | `variants/09-tired.png` |
| 惊讶 | `raised brows, eyes 1.2x wider, mouth slightly open but no wider than a finger` | 发现 / 醒悟 / 突然想到(不要震惊大嘴) | `variants/10-surprised.png` |
| 满足 | `slight 1-2mm mouth upturn, half-closed eyes, level brows` | 做完 / 完成 / 收工(不要咧嘴笑) | `variants/11-satisfied.png` |

**表情使用纪律 (v2.8.30 简化)**:
- **默认不写表情**,靠 standard.png reference 自然呈现
- 一篇文章里,多张图最多用 2-3 种不同表情(其余不写),避免"表情包轮播"
- 表情和备选装扮可叠加,但一张图最多 1 表情 + 1 装扮

## 实战 prompt 标准 IP 描述段(直接复制)

> **v2.8.30 简化**: IP 整体五官匹配靠 reference image (`standard.png` 作 input_file_paths), prompt 文字描述不再反复强调"窄单眼皮 / 死板冷静"等细节。**整体五官能看出是同一个 IP 即可**,不强制每个 prompt 都列出五官特征。

```
Xiaofan (a young Asian man matching the IP reference standard.png, hand-drawn line art) [姿态/动作/物件].
```

如果某些关键场景需要强调表情或五官,可在 IP 描述段里补充(都是微表情,不是大表情):

```
Xiaofan (a young Asian man matching the IP reference standard.png, [slightly furrowed brows, eyes half-closed, mouth slightly relaxed if needs thought/tired/confused/satisfied], hand-drawn line art) [姿态/动作/物件].
```

## 反面描述(不要写进 prompt,会触发错误风格)

- ❌ "minimalist black hand-drawn line art" — 触发极简
- ❌ "whiteboard quick sketch drawn in 30 seconds" — 触发极简 stick
- ❌ "no skin tone or color fill" — 触发去颜色填色(本 IP 接受颜色)
- ❌ "loose sketch, not refined" 单独使用 — 触发极简
- ❌ "absurd" / "crazy" / "weird" — 触发日漫 Q 版

## 实战 prompt 标准开头段(直接复制)

```
Generate a 16:9 horizontal Chinese article illustration on pure white background. Style: casual hand-drawn line illustration. Xiaofan is a loose line-drawn self-portrait with recognizable features. The face must look like the same Xiaofan as the reference. Xiaofan must perform the core conceptual action, not decorate the scene. He is the main action subject. Lots of white space. Do not draw a title in the corner. No PPT, no flowchart, no commercial vector style, no realistic photo elements.
```

---

# ⛔ 文字污染专项 (v2.8.36 新增)

> 起源: 一次配图生成, prompt 只要求一处文字, 渲染器**自己多加了「药房」「安静」两处招牌文字**。
> 这是继 033 渲染色号 / 035 衣服纯黑 / 039「了」→「弓」之后的**第 4 次"API 成功 ≠ 画面正确"**。
> **跟体裁无关** —— 公众号配图同样会中招: 药店 → 加「药房」, 公司 → 加公司名, 便利店 → 加 slogan, 货架 → 加价签。

## 触发条件

**场景里有"看起来该有招牌/标签/文字"的地方**, 渲染器就会自己补上。

## 每次必加的负向约束

```
⛔ ABSOLUTELY NO TEXT except the single line specified below.
NO signs, NO labels, NO shop name, NO shelf tags, NO banners, NO posters,
NO characters written on walls, pillars, shelves or on the boxes.
Every box is a completely blank empty rectangle with a plain white face.
NO writing of any kind on any object.
```

**关键是最后一句** —— 逐个物体点名(`boxes` / `walls` / `pillars` / `shelves`),
只写 "NO text" 不够, 渲染器会找补。

## 文字数量必须显式锁定

```
EXACTLY ONE line of text in the whole image, [位置], [颜色] brush handwriting: [内容]
```

用 **EXACTLY ONE** 而不是 "one line only" —— 后者会被理解成"至少一处, 允许多处"。

## 颜色也要锁死

如果只需要某一种颜色的字, 就要**明确排除其他颜色**, 否则渲染器会"贴心地"用别的颜色补几处平衡构图:

```
Color: strictly black ink lines, plus exactly ONE piece of text in light grey only.
No blue, no orange, nothing else is coloured anywhere in the image.
```

## 验收清单 (每张图逐条查)

- [ ] 有没有我没要求的文字?
- [ ] 有没有我没要求的颜色?
- [ ] 物体上有没有"想象中的标签"(价签/瓶身/包装)?
- [ ] 该有的那一处, 文字内容**逐字**对了吗? (「12」不能变成「I2」)

> 最后一条尤其重要: 数字是渲染器最容易错的地方, 逐字核对, 不要看个大概。

---

# ⛔ 五官失真专项 (v2.8.37 新增)

> **来源**: 公众号 038 (2026-10-12) 首版 2 张 IP 图, 用户反馈"形象和我们 IP 不是很像"。
> **性质**: 和文字污染同一类的坑 —— **渲染器会"贴心地"补全它认为该有的东西**。文字那个坑是补字, 这个坑是补五官。

## 触发条件

**含 IP 的图, 只要用户或自己觉得"脸不太像", 就立刻加下面这段。**

## 根因: 日系动漫脸三件套

`standard.png` 里小凡的眼睛是 **一笔短弧 + 一个点**。渲染器把这理解成"画一双眼睛", 于是自动套上动漫脸的标配:

| standard.png (正确) | 渲染器会补成 (错) |
|---|---|
| 一笔短弧 + 一个点 | 眼白 + 瞳孔 + 眼睑线 + 睫毛 |
| 眉毛不画 / 极淡短斜线 | 粗黑清晰的两道 |
| 偏长椭圆脸 | 偏圆脸 |
| 只有黑线 | 脸颊 / 脖子 / 耳朵粉红填充 |

**关键**: `Pure line drawing. Do NOT fill any clothing, hair or object with solid black or grey.` 这条**管不住它**。
它管的是"不要大色块填充", 但五官内部的**结构性细节**(眼白/瞳孔)不算"fill", 渲染器照画不误。

## 每次必加的负向约束

```
Match the EXACT facial construction of the character in the reference image:
eyes are ONE single thin short horizontal arc plus ONE small dot, nothing more.
NO eyebrows at all. Mouth is ONE short thin flat line.
Long oval face with a clean jawline.

NO eye whites, NO pupils, NO irises, NO eyelid lines, NO eyelashes.
NO thick or dark eyebrows. NO anime style, NO manga style,
NO polished or symmetrical face.
NO skin tone, NO blush, NO shading on the face.
```

> 前四行是**正面描述**(告诉它眼睛应该长什么样), 后五行是**负向禁写**。
> **两边都要写** —— 只写"要什么"不够, "不要什么"才是拦住动漫脸的关键。

## 非 IP 元素也要注意

手部同样会跑偏: 不指定就会画成**卡通手**(手指圆润带体积感)。要线稿手就写死:

```
one single relaxed human hand drawn with only 3-4 loose sketchy strokes,
fingers together and slightly curled
```

> ⚠️ **v2.8.43 降级**: 上面这条把 `standard.png` 里**有体积、有指节、手指分开**的手锁成了僵硬卡通手。
> **改用 v2.8.43 的 `HANDS — drawn as real hands with visible knuckles and naturally
> separated fingers, not blobs, not mittens, not three-stroke placeholders.`**

## 验收清单 (加进每张含 IP 图的检查)

跟文字污染清单一起查:

- [ ] 眼睛是"一笔短弧+一点", 还是画出了**眼白和瞳孔**?
- [ ] 眉毛是不是**粗黑两道**? (应该是几乎没有)
- [ ] 脸颊 / 脖子 / 耳朵有没有**粉红填充**?
- [ ] 脸型偏长椭圆, 还是偏圆?
- [ ] 手上有没有出现**卡通体积感**(圆润带阴影)?

> 放大看脸。整图看容易漏 —— 1:1 缩略图下"动漫眼"和"短弧+点"几乎分辨不出, 必须裁切放大。

---

# ⛔ 风格段自我诱发专项 (v2.8.39 新增)

> **来源**: 抖音 045/046 (2026-10-13) 首版, 6 张里 5 张被渲染器塞进没要求的箭头和文字。
> **性质**: 文字污染的**上游根因** —— 不是约束写得不够, 是**风格段自己在教它画批注**。

## 根因

v2.8.7 定的抖音 STYLE 开头段里有这么一句:

```
Diagrammatic composition: one core object or action, with handwritten annotations around it,
red brush-circle highlighting key words.
```

**这句话本身就是"请在图里加批注"的指令。**

渲染器忠实地执行了 —— 于是每张图都自动配齐:
- 红色 brush 圈
- 橙色箭头指向主体
- 蓝色补充说明批注
- 各种"看起来该有的"标签

**加上 `⛔ ABSOLUTELY NO TEXT` 这条负向约束, 跟正向的"with handwritten annotations"直接打架。**
正向指令具体、形象、有画面感; 负向指令抽象、约束性。**模型跟正向走。**

## 045/046 首版实测 (12 张里 7 张污染)

| 图 | 要求 | 实际 |
|---|---|---|
| 045-00 | 只有「退回」 | 多了「退回消息」「状态确认」×2「用户例」「操作流程」「发送方向」「应用端」「接收反馈」「系统提示」「返回路径」 |
| 045-01 | 只有「地址不全」 | 脸变动漫眼 + 腮红, 但文字 OK |
| 045-02 | 只有「驿站」 | 脸变动漫眼, 多了红圈和橙箭头 |
| 045-03 | 只有「第 4 段, 空格」 | ✅ 通过 (纯物件格, 无 IP) |
| 045-04 | 只有「3 天」 | ✅ 通过 (纯物件格, 无 IP) |
| 046-00 | 只有「转让」 | 「转让」被拆成竖排两行 + 多了一整圈批注 + 脸颊红点 |
| 046-03 | 只有「1 个手机号」 | 多出「空锅」「冷锅」「注册」「准备」 |

**规律很清楚: 纯物件格几乎不受影响, 含 IP 的格和留白少的格最容易被带偏。**

## 修正后的 STYLE 段 (v2.8.39, 直接复制)

```
Generate a square 1:1 Chinese social-media illustration on pure white background.
Style: casual hand-drawn line illustration, loose sketchy strokes with slight
flying-white gaps, lines not fully closed, minimal composition.
Subject occupies 40-60% of the frame. Very large empty white space. Quiet and sparse.
Chinese handwritten text ONLY where explicitly stated below. Nowhere else.
⛔ ABSOLUTELY NO TEXT anywhere except the exact text stated below.
NO captions, NO labels, NO annotations, NO arrows pointing at things,
NO callouts, NO explanation text, NO summary boxes.
NO writing of any kind on any object, no text on walls, no text on screens,
no text on papers, no menu, no signage.
do NOT write any color codes, hex codes, hash symbols, or alphanumeric strings.
NO brand name, NO logo, NO watermark, NO signature, NO English text, NO pinyin.
```

**关键改动**:
1. **删掉** `with handwritten annotations around it` 和 `red brush-circle highlighting key words`
2. **删掉** `Diagrammatic composition`
3. 新增 `NO captions, NO labels, NO annotations, NO arrows pointing at things, NO callouts, NO explanation text, NO summary boxes` —— **逐个点名**, 跟 v2.8.36「逐个物体点名」同一个道理
4. 加 `Very large empty white space. Quiet and sparse.` —— 留白本身就是抑制

## 每格文字锁定的正确写法

不要写「画面中标注 X」, 要写「**整张图里唯一的文字**」:

```
The ONLY text in the entire image: 地址不全 — red brush handwriting, inside that one bubble.
No red circle, no arrows, no other marks.
```

**`No red circle, no arrows, no other marks` 这行必须跟** — 明确否认画面里那些"看起来该有的"元素。

## 新的验收优先级

v2.8.36/37 的清单不变, 但**先查这一条**:

- [ ] **风格段里有没有"教它画批注"的句子?** (有就先改 STYLE, 不要靠单格约束去对抗)
- [ ] 有没有我没要求的箭头?
- [ ] 有没有我没要求的圈注?
- [ ] 指定的文字是不是**竖排/换行**了? (046-00 「转让」被拆成两行)

> 最后一条: 中文两三个字被拆成竖排, 视觉上极像"更多文字", 是这批最隐蔽的问题。

## 与 v2.8.36/37 的关系

| 版本 | 管什么 | 层级 |
|---|---|---|
| v2.8.36 | 场景里有"看起来该有字"的地方 → 负向禁写 | 单图约束 |
| v2.8.37 | 含 IP 的图 → 五官补全 | 单图约束 |
| **v2.8.39** | **风格段自己在教它画批注** | **风格段本身** ← 根因层 |

**教训: 负向约束写在单格里, 抵不过风格段里的正向指令。**
**风格段每一句都要问"这句会不会诱导出我不要的东西"。**

---

# ⛔ 平台适配层拆分 (v2.8.41 新增)

> **起源**: 公众号 039 (2026-10-19) 5 张配图被用户反馈"看着太单调, 不符合公众号 IP 相关的内容"。
> **真根因**: v2.8.39 修好了"禁批注", 但**把整个风格段整段搬到了公众号**, 连带把抖音专属的"大留白/极简"也搬过来了。

## v2.8.39 风格段其实是两层东西

| 层 | 内容 | 适用范围 | 能不能删 |
|---|---|---|---|
| **根因层** | `⛔ ABSOLUTELY NO TEXT except...`<br>`NO captions, NO labels, NO annotations, NO arrows pointing at things, NO callouts` | **两端通用** | ❌ 不能删 |
| **适配层** | `Subject occupies 40-60%`<br>`Very large empty white space. Quiet and sparse.` | **仅抖音** | ⚠️ 公众号**必须换掉** |

**根因层**解决的是"渲染器自己补箭头和文字"(v2.8.39 实测: 12 张里 7 张污染)。
**适配层**解决的是"抖音图解型要大量留白"(v2.8.7 用户 8/25 拍板)。

**公众号的形态要求跟抖音根本不同** —— 公众号要的是**场景叙事 + 信息图解**, 不是极简物件符号。

## 公众号配图 (16:9) 风格段 — v2.8.41 专用

```
Generate a 16:9 horizontal Chinese article illustration on pure white background.
Style: casual hand-drawn line illustration, loose sketchy strokes with visible
flying-white gaps, lines not fully closed, like a sketch drawn on a whiteboard.
Full scene with environment: draw the room, the furniture, the table, the floor line,
the background objects that make the scene real.
The person is IN the scene, not floating in white space. The person should be the
main subject, drawn at a large scale, usually from the waist up or closer.
Detailed objects: draw them with real detail, not as plain geometric symbols.
⛔ ABSOLUTELY NO TEXT anywhere except the exact text stated below.
NO captions, NO labels, NO annotations, NO arrows pointing at things,
NO callouts, NO explanation text, NO summary boxes.
NO writing of any kind on any object, no text on walls, no text on screens,
no text on papers, no menu, no signage, no posters.
do NOT write any color codes, hex codes, hash symbols, or alphanumeric strings.
NO brand name, NO logo, NO watermark, NO signature, NO English text, NO pinyin.
```

**跟抖音版的关键差异**:

| | 抖音 (1:1) | 公众号 (16:9) |
|---|---|---|
| 留白 | `Very large empty white space` | ❌ 不写, 要画满场景 |
| 主体 | `40-60%` | **大比例, 半身以上** |
| 环境 | 不要求 | **必须画**(沙发/桌面/地面线/背景物) |
| 物件 | 图解符号 | **有真实细节的物件** |
| 人物 | 按场景决定 | **在场景里, 不是浮在白底上** |

## 公众号配图的三种成熟形态 (照着抄)

**A. 场景叙事型** (019-03, 1007 阅读)
- 环境 + 人物在场景里 + 物件
- 例:沙发 + 靠垫 + 地面线, 人物坐在沙发上
- 人物占画面 **50-65%**

**B. 信息图解型** (015-01, 1007 阅读)
- 手绘框 + 分支线 + 橙色箭头 + 红色对勾
- 例:红框标题 + 6 个分支框 + 3 个对勾 + 2 个橙箭头

**C. 物件特写型** (019-02)
- 详细物件 + 局部红圈
- 例:完整手机界面画到朋友圈条目 + 底部图标 + 「1001」红圈

**❌ 反模式: 空壳符号型 (039 犯的)**
- 物件退化成几何符号(圆角矩形 = 按钮 / 圆角矩形 = 气泡)
- 人物缩成小头像浮在纯白里
- 没有环境、没有细节
- → 用户反馈"太单调"

**判据: 如果把这张图的任何一个人物删掉, 图还成立, 那就是空壳。**
公众号配图要**人物和场景不可分割**。

## §3.6 硬规则要一起落实 (039 犯了 2 条)

1. **人物拿手机时正拿** —— 屏幕朝自己脸, 读者看到**手机背面 + 人物脸**
   (039 画成屏幕朝读者, 违规)
2. **季节规则** —— 10 月杭州 = 春秋过渡 = **长袖薄衫 / 卫衣**
   (039 prompt 完全没写服装, 违规)

## 验收清单加 3 条

- [ ] **有人物和场景吗? 人物和场景能分开吗?** 能分开 = 空壳 = 重画
- [ ] 人物占画面 50% 以上吗?
- [ ] 拿手机的图画成正拿(背面朝读者)吗?
- [ ] 服装写了具体季节词吗?

---

# ⚠️ 眉毛专项 (v2.8.42 新增 → v2.8.43 整体降级为「非阻断项」)

> **来源**: 公众号 040 (2026-10-26) 首版 2 张含 IP 图, 裁切放大后发现**两道清晰粗黑眉毛**。
> **性质**: v2.8.37 的漏网项。v2.8.37 禁了眼白/瞳孔/睫毛/动漫脸, 但**没单独禁眉毛**。
>
> **⚠️ v2.8.43 结论: 下面这套禁令整体降级为「非阻断项」, 不要照抄。**
> 它在 040 v3 没稳定生效, 反而逼出了更严重的偏差 —— **把头发后梳、额头全露,
> 直接抹掉了 IP 的核心识别特征(刘海)**, 用户反馈"IP 形象完全不对"。
> 正确做法见文末 **v2.8.43**。
> **历史 019-03 (1007 阅读) 明确带眉毛, 用户从未反馈眉毛不对** ——
> 眉毛不是公众号读者的敏感点, **发型和脸型才是**。

## v2.8.37 漏了什么

v2.8.37 的禁写列表:

```
NO eye whites, NO pupils, NO irises, NO eyelid lines, NO eyelashes.
NO thick or dark eyebrows. NO anime style, NO manga style,
```

**`NO thick or dark eyebrows` 只禁了"粗的、深的"** —— 渲染器就画成**细短但清晰的眉毛**, 照样有。

**结果: 整图看完全正常, 裁切放大才发现。**

## v2.8.42 必加段 (放 prompt 最前面)

```
=== ABSOLUTE FACE RULES — FOLLOW EXACTLY, THESE OVERRIDE ANYTHING ELSE ===
The area between the hairline and the eyes must be COMPLETELY BLANK white space.
There must be NO eyebrows at all. Not thick ones, not thin ones, not faint short
strokes, not angled lines, not curved marks. Nothing. The forehead is empty paper.
Eyes: ONE single thin short horizontal arc, plus ONE tiny FLAT SOLID BLACK dot
(like a grain of rice, no bigger than 2% of the eye width).
That dot is FLAT SOLID BLACK. It has NO highlight, NO white glint, NO glossy shine,
NO reflection, NO inner ring, NO iris ring, NO pupil circle, NO gradient.
NO eye whites. NO pupils. NO irises. NO eyelid lines. NO eyelashes.
NO glossy eyes, NO shiny eyes, NO wet eyes, NO sparkling eyes, NO large dark pupils.
```

**三处关键改动**:

1. **放最前面**, 不是 IP 段末尾 —— 风格段长, 末尾的约束权重不够
2. **改描述式为禁令式** —— "额头是空白纸" 比 "NO thick or dark eyebrows" 有效得多
3. **点的规格量化** —— "FLAT SOLID BLACK, 2% of eye width, NO highlight" 拦住带高光的假瞳孔

## 眼睛那个"点"也会跑偏

v2.8.37 禁了瞳孔/虹膜, 但没规定**那个点本身该多大、多实**。
040-00 首版把点画成了**带高光的立体瞳孔** —— 看着像 `standard.png` 的点, 但高光让它变成眼睛。

**判据: 那个点应该像句号, 不像珠子。**

## 验收纪律再次确认

**整图验收 100% 漏眉毛。** 必须裁切放大脸:

```python
im.crop((脸左上x, 脸左上y, 脸右下x, 脸右下y)).resize((840, 760)).save('/tmp/face.png')
```

- [ ] 额头 (发际线到眼睛之间) 有没有**淡短斜线**的眉毛? (不是"完全空白" —— 见 v2.8.43)
- [ ] 眼睛是"一笔短弧 + **眼尾**一个小点", 点里没有高光?
- [ ] 眉毛是"很淡的短斜线", 而不是"一道都没有"? (全无 = 另一个方向的偏差)

## 附带: 姿态不能重复

040 首版两张含 IP 的都是"低头看手机" —— 违反 v2.8.34 姿态动态化。
重画时把 00-cover 改成**侧身转头看手机**(不是低头), 03-floor 保持低头滑动。

**场景叙事型天然容易撞姿态**(都是"某人拿手机"), 所以要主动错开:低头 / 侧身 / 躺 / 站 / 坐地上。

> ⛔ **上面「规矩」已被 v2.8.43 推翻** —— 见文末。正确结论是「刘海不能动」。

---

# ⛔ IP 形象失真专项 (v2.8.43 新增 · 最高优先级)

> **来源**: 公众号 040 (2026-10-26) v3, 用户反馈"IP 形象完全不对"。
> **性质**: 不是渲染器的锅 —— **是规范自己把 IP 改坏了**。
> v2.8.37 / v2.8.42 两条禁令累积起来, 把 IP 的识别特征一个一个删掉了。

## 根因: 过度矫正, 四处删除

v2.8.42 叫「眉毛专项」, 实际效果是:

| 规范条款 | 本意 | 实际后果 |
|---|---|---|
| `NO eyebrows at all` + "额头是空白纸" | 禁粗黑眉 | 连带把**淡短眉**也禁了 → 变成无眉脸 |
| "改正面微侧 + **头发后梳**露出额头" | 让禁令生效 | **抹掉刘海** → IP 从碎发少年变成背头成熟男 |
| "眼睛 = 一笔短弧 + 一个平黑点 (2%)" | 禁动漫眼 | 渲染器画成**两个黑豆眼**, 比动漫眼更失真 |
| `手只画 3-4 loose strokes, fingers together` (v2.8.37) | 线稿手 | 锁死了 `standard.png` 里**有体积、有指节、手指分开**的手 |

## 基准: 以 standard.png + 019-03 为准, 不以禁令为准

重新核对 `assets/ip-reference/standard.png` 和
`doc/essays/images/019-mute-moments/03-thinking-morning.png`
(1007 阅读, 唯一被用户确认"没问题"的 IP 大图), 正确形态是:

- **刘海: 尖角碎发垂到眉骨上方** —— 核心识别特征, 一撮撮, 发梢是尖的, 几笔速写带飞白
- **眉毛: 淡、短、斜线** —— 有, 但很淡 (标准图和 019-03 都有)
- **眼睛: 细长**, 一笔细弧 + **眼尾**一个小实心点 (不是黑豆眼)
- **脸型: 偏长椭圆**, 下颌线干净, 下巴略窄
- **唇: 薄**, 一笔短横
- **手: 有体积感, 有指节, 手指自然分开**
- **线条: 松、飞白、不闭合** —— 白板草图感, 不是干净的矢量线

## v2.8.43 公众号 IP 描述段 (直接复制)

```
Xiaofan (a young Asian man, hand-drawn line art, matching the IP reference standard.png):

HAIR — most important, do not skip: black messy short hair. A spiky pointed fringe
falls across the forehead, strands hanging down to just above the eyebrows, hair tips
pointed, a few separate strands, drawn with a few quick sketchy strokes and some
flying-white gaps. The fringe MUST be visible on the forehead.
NOT slicked back, NOT combed back, NOT brushed back, NOT a pompadour,
NOT cropped hair with the forehead exposed.

FACE — long oval face, clean jawline, slightly narrow chin.

EYES — narrow slit-like eyes. Each eye is ONE thin elongated line, slightly
downward-slanting, with ONE tiny solid black dot at the INNER corner. The eye is a
fine line only, drawn like a narrow closed slit.
NO white of the eye, NO eyeball, NO visible sclera, NO round pupil, NO iris,
NO big dark circle, NO open anime eye.

EYEBROWS — extremely faint, thin, short slanted strokes, like a light pencil trace,
much lighter than the hair. Barely there, but present.
NOT thick, NOT heavy, NOT solid black, NOT dark.

LIPS — thin, ONE short flat line.

SKIN — no skin tone, no shading, no blush.
NO hatching on the cheeks, NO blush lines, NO contour shading.

HANDS — simple sketchy outlines drawn with a few loose lines, simplified, normal size
in proportion to the body, with visible knuckles and naturally separated fingers.
NO fingernails, NO knuckle wrinkles, NO skin folds, NO anatomical detail,
NOT blobs, NOT mittens, NOT three-stroke placeholders, NOT a large foreground close-up.
```

## v2.8.43 禁填充段 (放风格段**最前面**, 替代抽象禁令)

> **⛔ 别再用 `Pure line drawing. Do NOT fill any clothing, hair or object with solid black or grey.`**
> 这条抽象禁令实测不管用 —— 040 重画 4 轮, 头发先变实心黑块, 改完又太浅像白发。

**改成正向描述 (实测有效)**:

```
EVERYTHING is thin black pencil lines on white paper. NOTHING is filled in with solid colour.
Hair is drawn with a few loose sketchy strokes that let the white paper show through the strands,
never a solid black shape, never a black silhouette, never flat black.
Clothing, faces, furniture and objects are all outline only, no shading, no grey tone.
This is a rough sketch, not a finished illustration: NO cel shading, NO gradient, NO cross-hatching.
```

**再加这一段 —— "黑"和"线稿质感"必须同时给**:

```
HAIR DENSITY - the hair must be built from MANY separate overlapping black strokes, short
directional strand lines, so the hair reads clearly DARK like black hair, while individual
strand lines and small white gaps stay visible inside it. It is textured line work,
NOT a flat solid black fill, NOT a black silhouette, NOT pale grey hair, NOT white hair.
```

> 只说"别填充" → 头发变白发; 只说"要有黑度" → 头发变实心块。**两句话必须写在一起。**

## v2.8.43 线条质感段 (放风格段里, 两端通用)

```
Line quality: loose and sketchy, like a quick drawing on a whiteboard.
Visible flying-white gaps inside strokes, lines that do not close, uneven pressure,
a few overshooting strokes at the edges.
NOT clean vector art, NOT polished commercial line illustration,
NOT thin uniform pen strokes, NOT digital perfect lines.
```

**为什么单列这一段**: 040 v3 线条太干净太矢量, 观感从"白板草图"变成"商业线稿插画"。
这不是五官问题, 但**观感差异比五官更刺眼** —— 019-03 那张之所以像, 一半功劳在飞白和松线。

## 验收清单 (改写)

**先查这 3 条, 任何一条不过就重画:**

- [ ] **刘海在不在?** 额头上有没有一撮撮尖角碎发垂到眉骨? (后梳 = 直接重画)
- [ ] **眉毛是不是"淡短斜线"?** 全无眉毛也算不过 —— 那是另一个方向的偏差
- [ ] **眼睛是细弧 + 内眼角小点, 还是两个黑豆?**

**再看这 3 条:**

- [ ] 脸型偏长椭圆, 下巴不方不圆?
- [ ] 手有指节, 手指是分开的?
- [ ] 线条有飞白和不闭合, 不是干净矢量线? 头发是**黑**的但不是实心块?

> **裁切放大依然要做** —— 整图验收 100% 漏眉毛 (v2.8.42 实测结论, 保留)。
> 但**放大是为了确认"淡短眉"而不是"没有眉"**。

## 附带发现: 信息图解型的连线是隐藏坑

040 的 02 四个分支图标全画对了, 但**连接线断了** —— 图还是废的。

**验收信息图解型要专门看: 每条连接线是不是完整画出来了, 且真的接到两边的框上。**
prompt 里要写死: `ALL FOUR connector lines are drawn, complete and visible, each one actually touching both its small frame and the red frame.`

## 历史判断的修正 (重要)

**「眉毛/眼睛细节 = 读者敏感点」这个判断是错的。**

038 反馈"形象不是很像" → v2.8.37 加了五官禁写 → 之后所有图变成"短弧+点+无眉+无刘海"。
但 **019-03 (1007 阅读) 是刘海 + 眉毛 + 细长眼, 用户从未反馈 IP 不像**。

结论: **对公众号读者来说, 眉毛和眼睛的细节不构成"像不像"的判断依据;
发型(刘海)、脸型、线条质感才是。**
砍掉后两者换来的"无眉", 收益远小于损失。

**以后遇到"脸不像", 先查发型和脸型, 不要先去砍五官。**
