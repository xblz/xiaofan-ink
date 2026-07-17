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

## 视觉特征(头部)

- 碎短发:有刘海覆盖额头,黑色,几笔速写
- 脸型:偏长椭圆,下颌线干净
- 眼睛:细长,单眼皮或内双,眼神平静偏冷(两笔短弧)
- 唇:薄唇,中性(短横)
- 表情:空、呆、冷静、认真(deadpan),无明显笑容
- 头像偏大(略大于身体),保证"线稿版的我"识别度

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

## 表情选项(可选用,默认用 deadpan 即可)

实战 prompt 的 IP 描述段里,默认 `deadpan calm expression`。如果当前图需要 1 度情绪传递,可在 IP 描述段里替换为以下微表情词(都是 deadpan 底色上的轻微变化,**不要大表情**):

| 情绪 | prompt 用词 | 适用场景 | 参考图 |
|------|------------|----------|--------|
| 默认(冷静) | `deadpan calm expression` | 绝大多数场景 | `standard.png` |
| 思考 | `slightly raised right eyebrow, eyes looking down-left, mouth closed` | 想 / 琢磨 / 找原因 | `variants/07-thoughtful.png` |
| 困惑 | `slightly furrowed brows, eyes half-closed, mouth slightly relaxed` | 看不懂 / 不确定 / 卡住 | `variants/08-confused.png` |
| 疲惫 | `drooping brows, eyes half-closed, mouth loose` | 累 / 加班 / 反复试错 | `variants/09-tired.png` |
| 惊讶 | `raised brows, eyes 1.2x wider, mouth slightly open but no wider than a finger` | 发现 / 醒悟 / 突然想到(不要震惊大嘴) | `variants/10-surprised.png` |
| 满足 | `slight 1-2mm mouth upturn, half-closed eyes, level brows` | 做完 / 完成 / 收工(不要咧嘴笑) | `variants/11-satisfied.png` |

**表情使用纪律**:
- 默认一律用 `deadpan calm expression`,不要每张图都加情绪
- 同一篇文章里,多张图最多用 2-3 种不同表情(其余保持 deadpan),避免小凡变成"表情包轮播"
- 表情和备选装扮可叠加,但一张图最多 1 表情 + 1 装扮

## 实战 prompt 标准 IP 描述段(直接复制)

```
Xiaofan (a young Asian man with short messy black bangs covering forehead, narrow single-eyelid eyes, thin lips, deadpan calm expression, hand-drawn line art) [姿态/动作/物件].
```

带表情的 IP 描述段示例:

```
Xiaofan (a young Asian man with short messy black bangs covering forehead, narrow single-eyelid eyes, thin lips, slightly furrowed brows, eyes half-closed, mouth slightly relaxed, hand-drawn line art) [姿态/动作/物件].
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
