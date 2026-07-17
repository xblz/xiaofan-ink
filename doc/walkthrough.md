# xiaofan-ink 完整使用 Walkthrough

> 这份文档用一篇示例文章,完整走一遍"读文章 → 提炼认知锚点 → 设计 shot list → 写 prompt → 生图 → QA → 交付"的流程,作为 xiaofan-ink skill 的实战参考。
>
> 阅读对象:用 xiaofan-ink 给中文文章配图的人(自己、Codex agent、其他人)。

---

## 0. 准备工作:先读什么 references

开始之前,先按需读这 4 份 references(不是一次全塞进上下文):

| 顺序 | 文件 | 用途 |
|---|---|---|
| 1 | `xiaofan-ink/references/style-dna.md` | 风格 DNA、调色板(温暖墨水感)、禁忌 |
| 2 | `xiaofan-ink/references/xiaofan-ip.md` | 小凡 IP 的外形、性格、动作库、备选装扮、**微表情库**、禁忌 |
| 3 | `xiaofan-ink/references/composition-patterns.md` | 8 种结构类型 + 反复刻规则 |
| 4 | `xiaofan-ink/references/prompt-template.md` | 生图 prompt 模板(英文)+ **表情选择 guidance** |

> **v1.0+ 新增能力**:小凡 IP 现在有 5 个微表情变体(思考/困惑/疲惫/惊讶/满足),实战时可在 IP 描述段里把 `deadpan calm expression` 替换为对应微表情词。默认 deadpan,同文最多 2-3 种不同表情。详见 `xiaofan-ip.md` 表情库段 + `prompt-template.md` 表情选择段。

QA 阶段再读 `xiaofan-ink/references/qa-checklist.md`。

---

## 1. 示例文章

挑一篇中等长度的中文方法论短文(约 400 字,有清晰的认知锚点),主题:**AI 时代做内容,不要平均用力**。

> **AI 时代做内容,不要平均用力**
>
> 很多人做内容,一上来就写,写完发,效果不好,就换平台,换话题。这种"平均用力"的做法,基本是没用的。
>
> 内容生产链上有两个断点。第一个断点是"从想法到表达":很多人脑子里有东西,但写不出来,或者写出来很乱。第二个断点是"从发出去到被人看到":就算写得好,如果发在一个不对的渠道,也没人看。这两个断点不解决,后面的工作全是浪费。
>
> 真正有效的是先想清楚三件事:这篇文章是给谁看的?解决他们什么问题?凭什么他们要看?想不清楚就别写,写出来也是垃圾。
>
> 好内容也不是一次性的。一份核心想法,可以拆成一篇长文、几个帖子、几张图、几段视频。不是内容多,是一份内容用了多次。这是杠杆。
>
> 努力是最低级的策略。真正有用的是选择(做什么/不做什么)、杠杆(用什么方法/工具放大效果)、节奏(什么时候做什么)。平均用力,是普通人最大的浪费。

---

## 2. 第一步:消化正文,提炼认知锚点

读完示例文章,先列出**认知锚点**(值得配图的核心判断/流程/状态/隐喻)。不要平均配图,优先选最有"画面感"的:

| # | 锚点 | 类型 | 视觉潜力 |
|---|---|---|---|
| 1 | 两个断点(想法→表达、发出去→被看到) | 流程 | ⭐⭐⭐ 强(可直接画两个断点+小凡卡在中间) |
| 2 | 三问自检(给谁看/解决啥/凭啥看) | 角色状态 | ⭐⭐ 中(可画小凡站在"自检机"前) |
| 3 | 一稿多用(长文/帖子/图/视频) | 概念隐喻 | ⭐⭐⭐ 强(可画一个东西变成多种形态) |
| 4 | 努力 vs 选择/杠杆/节奏 | 前后对比 / 方法分层 | ⭐⭐ 中(可画"努力"灰着,上面三层发光) |

文章短,**4 张就够**(默认 4-8 张,长文不超过 9 张)。

---

## 3. 第二步:shot list

给每张图写清楚 7 件事:**放在哪段后、主题、核心意思、结构类型、小凡在做什么、建议元素、建议中文标注**。

### Shot 01 — 两个断点

- **位置**:第二段"内容生产链上有两个断点"之后
- **主题**:内容生产链上的两处断点
- **核心意思**:写作链路上有"想法→表达"和"发出去→被看到"两处会卡住,卡住了后面全白干
- **结构类型**:Workflow + 角色状态
- **小凡在做什么**:卡在两个断点之间,左手抓左边断掉的传送带,右手伸向右边断掉的传送带,试图把两边接上,表情死板
- **建议元素**:低科技传送带(像纸带)+ 两个明显缺口 + 小凡卡在中间 + 1 根断掉的绳子
- **建议中文标注**:`断点 1` / `断点 2` / `想法` / `表达` / `渠道`

### Shot 02 — 三问自检

- **位置**:第三段"真正有效的是先想清楚三件事"之后
- **主题**:写之前的三问自检
- **核心意思**:不先问清三个问题就别动笔,问了再写
- **结构类型**:角色状态 + 方法分层
- **小凡在做什么**:站在一台奇怪的"自检机"前,一只手按按钮,另一只手掰三档开关,死板脸看着机器
- **建议元素**:三档开关(像老式收音机调台)+ 三个小圆灯 + 一本提问清单 + 旁边一把被锁住的笔
- **建议中文标注**:`给谁看?` / `解决啥?` / `凭啥看?` / `想清楚再写`

### Shot 03 — 一稿多用

- **位置**:第四段"好内容也不是一次性的"之后
- **核心意思**:一份核心内容可以拆成多种形式发,这是杠杆
- **结构类型**:概念隐喻
- **小凡在做什么**:用一台怪压面机/打印机,把一个纸团压成/印出几个不同形状的产出,死板脸操作
- **建议元素**:一个纸团作为"原料" → 怪机器 → 4 个不同形状的产出(长条/方块/小卡/折叠)
- **建议中文标注**:`一份核心` / `长文` / `帖子` / `图` / `视频`

### Shot 04 — 选择 / 杠杆 / 节奏

- **位置**:最后一段"努力是最低级的策略"之后
- **核心意思**:替代"努力"的三个更高维度策略
- **结构类型**:方法分层
- **小凡在做什么**:站在三层奇怪工位旁,最底层"努力"是灰的,上面三层是亮的,小凡一只手扶着第一层,另一只手往最上层搬东西
- **建议元素**:三层堆叠的盒子/工位(底层灰,上三层带光)+ 三个中文标签
- **建议中文标注**:`努力` (灰) / `选择` / `杠杆` / `节奏`

---

## 4. 第三步:每张图的 prompt

把 shot list 转成英文 prompt(基于 `prompt-template.md` 的模板)。每张图都要包含完整 IP 描述 + 配色 HEX。

### 04.1 Shot 01 — 两个断点

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines with visible gaps, broken strokes, and overshoots — like a casual whiteboard quick sketch, never refined or vector-like. Lots of empty white space. Sparse red/orange/blue handwritten Chinese annotations (warm-ink palette: black #1A1A1A, red #C0392B, orange #E67E22, blue #2C5F8D). No gradients, no shadows, no paper texture, no complex background, no commercial vector style, no PPT infographic look, no cute mascot poster, no children's illustration, no realistic UI.

Recurring IP character required:
Xiaofan (Chinese: 小凡), a young Asian man with short messy black bangs covering the forehead, narrow single-eyelid or inner-fold eyes, thin lips, oval slightly long face, clean jawline. Always rendered in loose hand-drawn black line art, like a quick sketch. Expression is deadpan, calm, slightly cold, like a quiet system operator caught mid-thought. Xiaofan must perform the core conceptual action, not decorate the scene. Make Xiaofan serious, deadpan, slightly off-balance, never cute, never mascot-like, never realistic.

Theme:
内容生产链上的两个断点 — 想法→表达、发出去→被看到,卡住了后面全白干。

Structure type:
Workflow + 角色状态 (two-breakpoint bottleneck)

Core idea:
写作链路上有"想法→表达"和"发出去→被看到"两处会卡住,卡住了后面全白干。

Composition:
Xiaofan is half-body shown, stuck in the middle between two low-tech paper conveyor belts. Each conveyor has a clearly visible gap (the two breakpoints). Xiaofan's left hand holds the broken end of the left conveyor's rope, his right hand reaches toward the right conveyor's broken rope, as if trying to reconnect them. His expression is deadpan, slightly off-balance. Left of the left breakpoint: a small cluster of loose papers (ideas). Right of the right breakpoint: a small icon group representing audience / channels.

Suggested elements:
纸带传送带 (low-tech paper conveyor) / 2 个明显缺口 / 1 根断掉的绳子 / 散落的纸片 / 观众/渠道小图标

Chinese handwritten labels:
`断点 1` (red) / `断点 2` (red) / `想法` (blue) / `表达` (blue) / `渠道` (orange)

Color use (warm-ink palette):
Black (#1A1A1A) for main line art and Xiaofan. Orange (#E67E22) for the two conveyor directions. Red (#C0392B) only for the breakpoint labels. Blue (#2C5F8D) for the idea/expression/channel labels.

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. Do not write a title in the top-left corner. Do not make it a formal diagram. Do not copy prior examples or reuse known case compositions. Invent a fresh visual metaphor for this specific article.
```

### 04.2 Shot 02 — 三问自检

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Visual DNA:
[same as Shot 01]

Recurring IP character required:
[same as Shot 01]

Theme:
写之前的三问自检 — 不先问清三个问题就别动笔。

Structure type:
角色状态 + 方法分层 (pre-flight self-check before writing)

Core idea:
不先问清三个问题就别动笔,问了再写。

Composition:
Xiaofan is half-body shown, standing in front of a strange low-tech "self-check machine". The machine has three round indicator lights (off, off, off), a three-position toggle switch (like an old radio dial), and a small notebook on top. Xiaofan's left hand presses a big red button on the machine, his right hand flips the three-position switch. His expression is deadpan, slightly squinting. To one side, a pen is locked inside a small glass box (waiting for the three questions to be answered first).

Suggested elements:
三档开关 / 3 个小圆灯 / 1 本提问清单 / 1 把被锁住的笔 / 1 个红色大按钮

Chinese handwritten labels:
`给谁看?` (blue) / `解决啥?` (blue) / `凭啥看?` (blue) / `想清楚再写` (red)

Color use (warm-ink palette):
Black for line art. Blue for the three questions (cold/system state). Red for the conclusion label. Use at most 2 colors of annotations.

Constraints:
[same as Shot 01]
```

### 04.3 Shot 03 — 一稿多用

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Visual DNA:
[same as Shot 01]

Recurring IP character required:
[same as Shot 01]

Theme:
一份核心内容可以拆成多种形式发,这是杠杆。

Structure type:
概念隐喻 (one source, many forms)

Core idea:
一份核心想法拆成长文、帖子、图、视频,这是内容的杠杆。

Composition:
On the left, a single crumpled paper ball labeled "一份核心" in orange. In the middle, a strange low-tech hand press / press machine. Xiaofan is half-body shown, standing behind the press, both hands pushing the lever down, deadpan face. On the right, four different shaped outputs come out of the press: a long strip, a square card, a small square block, a folded paper. Each output has a small label in a different color.

Suggested elements:
1 个纸团(原料)/ 1 台怪压面机/ 4 个不同形状的产出

Chinese handwritten labels:
`一份核心` (orange) / `长文` (blue) / `帖子` (blue) / `图` (blue) / `视频` (blue)

Color use (warm-ink palette):
Black for line art. Orange for the "core source" label and the press direction. Blue for the four output forms.

Constraints:
[same as Shot 01]
```

### 04.4 Shot 04 — 选择 / 杠杆 / 节奏

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Visual DNA:
[same as Shot 01]

Recurring IP character required:
[same as Shot 01]

Theme:
替代"努力"的三个更高维度策略:选择、杠杆、节奏。

Structure type:
方法分层 (three-layer strategy, bottom layer dimmed)

Core idea:
用更高维度的策略替代低级的"努力"。

Composition:
Xiaofan is half-body shown, standing next to a three-layer stacked workstation. The bottom layer is dimmed/grayed (labeled "努力"). The middle layer is clearly outlined (labeled "选择"). The top layer is slightly emphasized (labeled "杠杆"), and a small clock icon floats above the top (labeled "节奏"). Xiaofan's left hand props up the bottom layer, his right hand reaches up to place something on the top layer. His expression is deadpan, slightly off-balance.

Suggested elements:
3 层堆叠盒子(底层灰,上 3 层亮)/ 1 个小时钟 / 小光晕

Chinese handwritten labels:
`努力` (gray, dim) / `选择` (blue) / `杠杆` (blue) / `节奏` (orange)

Color use (warm-ink palette):
Black for line art. The bottom layer intentionally dimmer/grayer (low contrast). Blue for the middle two strategy layers. Orange for "节奏" (the highest level, most emphasis).

Constraints:
[same as Shot 01]
```

---

## 5. 第四步:生图 + QA

每张图用内置 `image_gen`(或外部图像模型)单独生成,**不要把多张图拼在一起**。

生成后,过 `qa-checklist.md` 的必过项:

- [ ] 16:9 横版
- [ ] 纯白背景
- [ ] 有小凡
- [ ] 小凡承担核心动作(去掉小凡图就不成立)
- [ ] 重新发明的隐喻(没复用近期构图)
- [ ] 画面怪诞、有创意
- [ ] 主体 40%-60% 画面,至少 35% 留白
- [ ] 中文标注 ≤8 处,每处 2-8 字
- [ ] 橙色只用于主路径,红色只用于重点,蓝色只用于辅助

如果失败信号出现,优先**重生成**;细节问题(比如某个标注字错了)用图像编辑 prompt 局部改:

```text
Edit the provided image. Remove only the handwritten label "断点 1" and its underline. Fill that area with the same clean white background. Preserve everything else exactly.
```

---

## 6. 第五步:交付

保存到 workspace 的:

```text
assets/<article-slug>-illustrations/
```

按顺序命名:

```text
01-two-breakpoints.png
02-three-questions.png
03-one-source-many-shapes.png
04-three-strategy-layers.png
```

最终交付给用户的信息:

- 生成了 4 张
- 每张图的用途 + 在文章里的位置
- 保存路径
- 哪些图最稳、哪些是可选(给用户回退空间)

不要长篇解释风格理论,让图自己说话。

---

## 7. 常见问题

### 7.0 Prompt 库在哪?

`xiaofan-ink/assets/prompts/` 目录下:

- `articles/` — 实战验证过的 prompt(比如 `whiteboard-vs-doc.md`),直接复用
- `skill-samples/` — 6 张 skill 样例图的 prompt(已通过 QA 的"做什么可以"参考库)
- 实战时优先复制 `articles/` 下的对应文章 prompt,改主题/结构/标注即可,不要从零写

### 7.1 文章里没有明显认知锚点怎么办?

只写 1-3 张图,或者干脆不配图。一张不配图的文章,比强行配 6 张烂图要好。

### 7.2 同一篇文章,4 张图怎么避免"反复刻"?

- 姿态变化:站 / 蹲 / 探出 / 卡住 / 回头看画外
- 物件变化:传送带 / 机器 / 压面机 / 堆叠盒子
- 视角变化:正面 / 侧面 / 半俯视

至少 3 个维度变化。详见 `composition-patterns.md` 的"反复刻规则"段。

### 7.3 小凡的脸和参考照片不像怎么办?

重出。这是 IP 风格的难点,图像模型对"真人转手绘 IP"的理解不稳定。一般重出 2-3 次就能稳定。

### 7.4 中文标注字错了怎么办?

- 错 1-2 个:用图像编辑 prompt 局部改
- 错多了:重出,并减少标注数量(≤5 处)

### 7.5 怎么判断一张图算"合格"?

第一眼应该是"有点怪",然后 1 秒内看懂结构。如果第一眼像教程页/PowerPoint,就重出。

### 7.6 表情库怎么用?(v1.0+)

默认用 `deadpan calm expression`(绝大多数场景用这个)。如果这张图需要 1 度情绪传递,可在 IP 描述段里把 deadpan 词替换为对应微表情词,例如:

- `slightly raised right eyebrow, eyes looking down-left, mouth closed` — 思考
- `drooping brows, eyes half-closed, mouth loose` — 疲惫
- 完整表情表见 `xiaofan-ink/assets/prompts/_standard-ip-description.md` 表情选项段

**纪律**:同文最多 2-3 种不同表情;一旦加表情,IP 描述段里 `deadpan calm expression` 必须删掉(避免和表情词冲突)。实战示例见附录 B 实战 3。

---

## 8. 附录 B:实战案例集

xiaofan-ink 已经在实战中验证过 3 篇文章(每篇 4 张配图),作为后续实战的参考案例:

| # | 文章 | 主题 | 表情分布 | 关键 takeaway |
|---|------|------|----------|---------------|
| 1 | `doc/whiteboard-vs-doc.md` | 思维工具选择(白板 vs 文档) | 全 deadpan | 反复刻陷阱:姿态都"站" / 物件都"低科技机器" |
| 2 | `doc/why-i-quit-gtd.md` | 工具反思(为什么不用 GTD 了) | 全 deadpan + 3/4 用备选装扮 | 改进:姿态"非站"(蹲/探出/坐/卡住)+ 备选装扮实战 |
| 3 | `doc/why-i-write-drafts.md` | 写作方法反思(为什么写"废稿") | **2 默认 + 1 思考 + 1 疲惫** | 首次用表情库,验证微表情不影响 deadpan 底色 |

### 实战 3 — why-i-write-drafts(v1.0 表情库首篇实战)

> 完整文章:`doc/why-i-write-drafts.md`
> 完整 prompt 库(含 4 张图完整 5 段 prompt + 表情选词理由 + 反复刻陷阱预标记):`xiaofan-ink/assets/prompts/articles/why-i-write-drafts.md`
> 实现时间:v1.1 / 2026-07-17

#### 表情选型决策

| 图 | 表情 | 选这个表情的理由 |
|---|---|---|
| 01 废稿堆 | deadpan | 入口段"我就是这样在做",陈述状态不需要情绪 |
| 02 三个开头 | **思考**(07-thoughtful) | "找哪条路是错的"是审视和归因 |
| 03 推倒重来 | **疲惫**(09-tired) | "反复试错的累"比 deadpan 更准确 |
| 04 成本是废稿 | deadpan | 收束段回到冷静陈述结论,deadpan 让结论有清冷理性 |

**情绪节奏**:平 → 思考 → 疲惫 → 平(完整呼吸),没有越走越高。

#### 表情库使用纪律(实战验证有效)

- **同文最多 2-3 种不同表情**(本文用了 2 种 + 2 个默认,符合纪律)
- **一旦加表情,IP 描述段里 `deadpan calm expression` 必须删掉**(避免和表情词冲突)
- **表情和备选装扮可独立/叠加使用**(本文未用装扮,纯靠表情切换节奏)
- **不要每张图都加表情**(入口和收束段用默认,中间段再用表情,避免变表情包轮播)

#### 表情使用 prompt 模式(可直接复用)

```python
# 实战 3 的 input_file_paths(必传 standard.png)
input_file_paths = ["xiaofan-ink/assets/ip-reference/standard.png"]

# 图 02 思考表情 IP 描述段
ip_description = """Xiaofan (a young Asian man with short messy black bangs covering forehead, narrow single-eyelid eyes, thin lips, slightly raised right eyebrow, eyes looking down-left, mouth closed, hand-drawn line art) [姿态/动作/物件]."""

# 图 03 疲惫表情 IP 描述段
ip_description = """Xiaofan (a young Asian man with short messy black bangs covering forehead, narrow single-eyelid eyes, thin lips, drooping brows, eyes half-closed, mouth loose, hand-drawn line art) [姿态/动作/物件]."""
```

#### 实战 takeaway(给后续实战参考)

- **表情库是 v1.0 才加入的,实战 3 是首篇实战**
- **4 张图全部一次过,无重出** — 微表情没破坏 deadpan 底色,prompt 替换词直接生效
- **表情库在实战中是默认能力**:默认 deadpan,需要时加 1-2 种微表情,情绪节奏"平 → X → Y → 平"
- **同文 2 种不同表情已经够用** — 不需要 5 种都用上,微表情要克制

#### 实战 1 / 2 关键 takeaway(简版)

- **实战 1(whiteboard-vs-doc)**:首次实战,4 张图全用 deadpan,但暴露两个反复刻陷阱 — 姿态都"站" / 物件都"低科技机器"
- **实战 2(why-i-quit-gtd)**:刻意改掉实战 1 的反复刻陷阱,4 张图覆盖 4 种不同姿态(蹲/探出/坐/卡住)+ 3/4 张用备选装扮(耳机/工具包+笔/笔记本)
- **实战 3(why-i-write-drafts)**:在实战 1/2 基础上,加入 v1.0 表情库,完成"姿态/装扮/表情"三维度全覆盖

---

## 附录:配色速查

| 概念 | HEX | RGB | 用途 |
|---|---|---|---|
| 黑色 (ink) | `#1A1A1A` | (26, 26, 26) | 主体线稿、小凡 |
| 红色 (alert) | `#C0392B` | (192, 57, 43) | 重点、问题、结果 |
| 橙色 (path) | `#E67E22` | (230, 126, 34) | 主流程、路径、箭头 |
| 蓝色 (note) | `#2C5F8D` | (44, 95, 141) | 补充说明、系统状态 |

(详见 `xiaofan-ink/references/style-dna.md`)
