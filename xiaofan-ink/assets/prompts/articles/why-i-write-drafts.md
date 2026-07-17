# 实战 3 — 为什么我开始主动写"废稿"

> 主题:写作方法反思(草稿/试错价值)/ 配图数:4
> 文章:`doc/why-i-write-drafts.md`
> 配图目录:`doc/images/why-i-write-drafts/`
> 实战日期:2026-07-17 / v1.0 表情库首次实战
>
> 模板详见 `xiaofan-ink/references/prompt-template.md`
> IP 描述段详见 `xiaofan-ink/assets/prompts/_standard-ip-description.md`
> 表情库详见 `xiaofan-ink/references/xiaofan-ip.md` 表情库段

---

## 全文 4 张配图速览

| 图 | 主题 | 结构类型 | 表情 | 核心物件 |
|---|---|---|---|---|
| 01 | 废稿堆 | 概念隐喻 | deadpan 默认 | 废稿山 + 一张写完一半的纸 |
| 02 | 三个被划掉的开头 | 角色状态 | **思考**(07-thoughtful) | 三个不同开头的纸(都划掉) |
| 03 | 推倒重来 | 概念隐喻 | **疲惫**(09-tired) | 折弯箭头(重来) + 初稿 + 第二稿 |
| 04 | 成本是废稿 | 概念隐喻 | deadpan 默认 | 废稿堆 + 薄薄成品 + 橙色箭头 |

表情分布:**2 默认 + 1 思考 + 1 疲惫**(同文 2 种不同表情,符合"最多 2-3 种"纪律)。

---

## 图 01 — 废稿堆

### IP 描述段(deadpan 默认)

```
Xiaofan (a young Asian man with short messy black bangs covering forehead, narrow single-eyelid eyes, thin lips, deadpan calm expression, hand-drawn line art) [姿态/动作/物件].
```

### 完整 prompt

```
Generate a 16:9 horizontal Chinese article illustration on pure white background. Style: casual hand-drawn line illustration. Xiaofan is a loose line-drawn self-portrait with recognizable features. The face must look like the same Xiaofan as the reference. Xiaofan must perform the core conceptual action, not decorate the scene. He is the main action subject. Lots of white space. Do not draw a title in the corner. No PPT, no flowchart, no commercial vector style, no realistic photo elements.

Theme: 废稿不是浪费 - 主动写"注定不会发"的稿子才是真正能写出好东西的路径。

Structure type: 概念隐喻

Core idea: 废稿堆里反而藏着好文章 - "废"和"成"不是对立关系,是试错过程。

Composition: A messy pile of crumpled paper sheets on the right side, some sheets have handwritten lines crossed out in red. Xiaofan is poking his upper body out from inside the paper pile, only his head and shoulders visible, one hand holding a half-written sheet that he just rescued, the other hand steadying himself on the edge of the pile. The rescued sheet is circled in orange with an arrow pointing to it.

Chinese handwritten labels: '废稿山' in black near the pile / '↑ 这张能成' in orange pointing to the rescued sheet / '已废' in red on crossed-out sheets

Constraints: Do not copy prior examples or reuse known case compositions; invent a fresh visual metaphor for this specific article. It should be clear but not instructional, interesting but not childish, strange but clean. Keep the main subject around 40-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. The image must look like a casual hand-drawn line illustration, NOT a polished commercial illustration.
```

### input_file_paths

```python
["xiaofan-ink/assets/ip-reference/standard.png"]
```

### 表情选 deadpan 默认的原因

入口段(文章开头),"我就是这样在做"是陈述状态,不需要情绪传递。用默认 deadpan 让"废稿堆"和"我从废稿里出来"形成视觉锚点,后续 3 张图再分梯度加情绪。

---

## 图 02 — 三个被划掉的开头

### IP 描述段(思考表情)

```
Xiaofan (a young Asian man with short messy black bangs covering forehead, narrow single-eyelid eyes, thin lips, slightly raised right eyebrow, eyes looking down-left, mouth closed, hand-drawn line art) [姿态/动作/物件].
```

> 注意:加表情后,`deadpan calm expression` 必须删掉(避免和表情词冲突)。

### 完整 prompt

```
Generate a 16:9 horizontal Chinese article illustration on pure white background. Style: casual hand-drawn line illustration. Xiaofan is a loose line-drawn self-portrait with recognizable features. The face must look like the same Xiaofan as the reference. Xiaofan must perform the core conceptual action, not decorate the scene. He is the main action subject. Lots of white space. Do not draw a title in the corner. No PPT, no flowchart, no commercial vector style, no realistic photo elements.

Theme: 三个不同开头的稿子 - 试错帮我排除了两条死路,留下一个真方向。

Structure type: 角色状态

Core idea: 三个被划掉的开头不是失败,是"试错帮我排除了死路"。

Composition: Three different opening drafts are laid out side by side, each on a separate sheet of paper, each crossed out with a big red X. Below the three sheets, an orange bracket groups them together with a label. Xiaofan is standing in the middle position, head lowered looking at the three sheets, one hand pointing at the first sheet's X, the other hand at his chin. He is examining the three failed attempts.

Chinese handwritten labels: '3 个开头 → 1 个留下' in orange under the bracket / 'X' in red on each crossed-out sheet / '排除 2 条死路' in blue near Xiaofan's hand

Constraints: Do not copy prior examples or reuse known case compositions; invent a fresh visual metaphor for this specific article. It should be clear but not instructional, interesting but not childish, strange but clean. Keep the main subject around 40-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. The image must look like a casual hand-drawn line illustration, NOT a polished commercial illustration.
```

### input_file_paths

```python
["xiaofan-ink/assets/ip-reference/standard.png"]
```

### 表情选思考的原因

文章第 2 段讲"找哪里没想清楚 / 哪条路是错的",是审视和归因的状态。思考表情(右眉微挑 + 眼斜看)传递"我在找原因",跟"3 个开头被划掉"配合得当。

---

## 图 03 — 推倒重来

### IP 描述段(疲惫表情)

```
Xiaofan (a young Asian man with short messy black bangs covering forehead, narrow single-eyelid eyes, thin lips, drooping brows, eyes half-closed, mouth loose, hand-drawn line art) [姿态/动作/物件].
```

### 完整 prompt

```
Generate a 16:9 horizontal Chinese article illustration on pure white background. Style: casual hand-drawn line illustration. Xiaofan is a loose line-drawn self-portrait with recognizable features. The face must look like the same Xiaofan as the reference. Xiaofan must perform the core conceptual action, not decorate the scene. He is the main action subject. Lots of white space. Do not draw a title in the corner. No PPT, no flowchart, no commercial vector style, no realistic photo elements.

Theme: 推倒重来 - 写到一半发现结构错了,推倒的稿子不浪费。

Structure type: 概念隐喻

Core idea: 推倒重来的"废稿"不是浪费时间,是排除错误方向的必经之路。

Composition: A bent arrow path in the middle, going from left to right then curving sharply upward to represent 'redirection'. Below the arrow is a crumpled first draft. To the right is a fresh second draft sheet. Xiaofan is squatting at the bend point of the arrow, one hand steadying the bend, the other hand gesturing a small circular 'restart' symbol. His face looks tired from many failed attempts.

Chinese handwritten labels: '第一稿 已废' in red on the crumpled paper / '第二稿 重写' in blue on the new sheet / '↺' in orange near Xiaofan's other hand / '反复试错' in orange next to the bend

Constraints: Do not copy prior examples or reuse known case compositions; invent a fresh visual metaphor for this specific article. It should be clear but not instructional, interesting but not childish, strange but clean. Keep the main subject around 40-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. The image must look like a casual hand-drawn line illustration, NOT a polished commercial illustration.
```

### input_file_paths

```python
["xiaofan-ink/assets/ip-reference/standard.png"]
```

### 表情选疲惫的原因

文章第 3 段讲"反复试错的累" — 推倒重来本身就是累的,疲惫表情(眉尾下垂 + 眼半闭)传递"我做这事做了很久"的潜台词,比 deadpan 更准确。

---

## 图 04 — 成本是废稿

### IP 描述段(deadpan 默认)

```
Xiaofan (a young Asian man with short messy black bangs covering forehead, narrow single-eyelid eyes, thin lips, deadpan calm expression, hand-drawn line art) [姿态/动作/物件].
```

### 完整 prompt

```
Generate a 16:9 horizontal Chinese article illustration on pure white background. Style: casual hand-drawn line illustration. Xiaofan is a loose line-drawn self-portrait with recognizable features. The face must look like the same Xiaofan as the reference. Xiaofan must perform the core conceptual action, not decorate the scene. He is the main action subject. Lots of white space. Do not draw a title in the corner. No PPT, no flowchart, no commercial vector style, no realistic photo elements.

Theme: 真正的成本在废稿 - 写完一篇文章,真正的工作量在排除的废稿,不是留下的成品。

Structure type: 概念隐喻

Core idea: 成品只是废稿的 1/N - 写一篇文章真正的工作量是排除的废稿数量。

Composition: On the left, a thick tall stack of messy draft sheets (representing drafts). On the right, a thin small stack of clean finished pages. Between them, an orange arrow points from the drafts to the finished pages with a label. Xiaofan is standing next to the draft stack, one hand touching the stack, the other hand open palm facing up, looking at the draft stack with a deadpan expression.

Chinese handwritten labels: '成本在这里' in orange on the draft stack / '留下 20%' in blue on the finished pages / '<< 真正的工作量' in orange on the arrow / '?' near the open hand

Constraints: Do not copy prior examples or reuse known case compositions; invent a fresh visual metaphor for this specific article. It should be clear but not instructional, interesting but not childish, strange but clean. Keep the main subject around 40-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. The image must look like a casual hand-drawn line illustration, NOT a polished commercial illustration.
```

### input_file_paths

```python
["xiaofan-ink/assets/ip-reference/standard.png"]
```

### 表情选 deadpan 默认的原因

收束段(文章结尾),要回到"冷静陈述结论"的状态。疲惫已经用过,如果结尾再疲惫就成了"抱怨",反而削弱结论的"清冷理性"deadpan 调。回到 deadpan 让整篇情绪节奏:平 → 思考 → 疲惫 → 平(回到默认),形成"→ 思考 → 试错 → →" 的平静呼吸,而不是越走越高。

---

## 表情使用复盘

按 v1.0 表情库纪律,本文用了 2 种不同表情(思考 + 疲惫)+ 2 种默认(deadpan),共 4 个状态切换。情绪节奏合理:

```
01 deadpan(平视) → 02 思考(找原因) → 03 疲惫(试错累) → 04 deadpan(冷静收束)
```

如果把 04 改成"满足"(做完),会变成"我成功完成了这篇"的得意调,反而违背 deadpan 气质。**收束段保持默认是正确的选择**。

---

## 可能的反复刻陷阱(预先标记)

实战生成时,留意以下点:

1. **图 01 废稿堆**:小凡从废稿山"探出"的姿态要明确 — 不是站在旁边,头和肩要真的从纸堆里冒出来。如果出来的姿态不明显,要重出。
2. **图 02 三个开头**:三个纸要并排且"都划掉"的视觉一致,不能只划一个。橙色括号是视觉关键,不能漏。
3. **图 03 推倒重来**:折弯箭头方向要清晰(左→右→上),不能画成直线。疲惫表情要让"我做了很久"传达到位。
4. **图 04 成本是废稿**:废稿堆要明显比成品厚 3-5 倍,这是"成本"的视觉关键。
