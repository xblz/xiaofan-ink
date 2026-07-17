# 实战 prompt:白板比文档更值钱

> 文章:`doc/whiteboard-vs-doc.md`
> 生成日期:2026-07-16
> 输入参考图:`.ip-dev/reference.jpg`(原始证件照,v1 阶段)
> 实际生成图:`doc/images/whiteboard-vs-doc/01-04.png`
> 注:v1 阶段用证件照直接生成,后续 v2 改用 `xiaofan-ink/assets/ip-reference/standard.png` 作参考(IP 一致性更好)

## 01 - 文档的陷阱

**对应图**: `doc/images/whiteboard-vs-doc/01-doc-trap.png`
**结构类型**: 概念隐喻
**小凡姿态**: 站着看被擦掉问号的完美文档

```text
Generate a 16:9 horizontal Chinese article illustration on pure white background. Style: casual whiteboard quick sketch, slightly shaky pen lines with visible gaps, broken strokes, not refined. Sparse red orange and blue Chinese handwritten annotations in warm-ink palette (black #1A1A1A, red #C0392B, orange #E67E22, blue #2C5F8D). The illustration shows Xiaofan (a young Asian man with short messy black bangs covering forehead, narrow single-eyelid eyes, thin lips, deadpan calm expression, hand-drawn line art) standing half-body next to a thick perfect document. An eraser is shown rubbing out question marks from the document, leaving clean blank spaces. Xiaofan looks at the erased spots with a deadpan slightly off-balance expression. He is the main action subject. Lots of white space. Do not draw a title in the corner. No cute, no mascot, no PPT style. Chinese handwritten labels: '完整 规整 自洽' in blue / '?' in red, getting erased / '擦掉' in orange.
```

## 02 - 白板的好处

**对应图**: `doc/images/whiteboard-vs-doc/02-whiteboard-better.png`
**结构类型**: 前后对比
**小凡姿态**: 站中间,身体前倾看白板

```text
Generate a 16:9 horizontal Chinese article illustration on pure white background. Style: casual whiteboard quick sketch, slightly shaky pen lines, not refined. Sparse annotations in warm-ink palette. The illustration shows a before-after comparison: on the left, a perfectly organized document (drawn with slightly more rigid lines, grayer, with bullet points neatly arranged). On the right, a messy whiteboard (drawn with very loose lines, with arrows pointing back and forth, question marks, the word '待定' scribbled). In the middle, Xiaofan (a young Asian man with short messy black bangs, narrow single-eyelid eyes, thin lips, deadpan calm expression, hand-drawn line art) is shown half-body, looking at the whiteboard side with a slightly off-balance leaning pose. He is the main action subject. Lots of white space. Do not draw a title in the corner. No cute, no mascot, no PPT style. Chinese handwritten labels: '文档' in gray / '白板' in orange / '?' in red / '待定' in red.
```

## 03 - 用草图表达

**对应图**: `doc/images/whiteboard-vs-doc/03-three-strokes.png`
**结构类型**: 隐喻
**小凡姿态**: 一只手画三笔,另一只手推文档

```text
Generate a 16:9 horizontal Chinese article illustration on pure white background. Style: casual whiteboard quick sketch, slightly shaky pen lines, not refined. Sparse annotations. The illustration shows Xiaofan (a young Asian man with short messy black bangs, narrow single-eyelid eyes, thin lips, deadpan calm expression, hand-drawn line art) half-body shown, one hand holding a pen and drawing three simple lines (a triangle, a circle, an arrow) in the air, the other hand pushing away a thick stack of documents. His expression is deadpan, slightly off-balance. The three lines he draws are loose and simple, the documents are pushed to one side, slightly disorganized. He is the main action subject. Lots of white space. Do not draw a title in the corner. No cute, no mascot, no PPT style. Chinese handwritten labels: '一段话' in blue / '三笔' in orange / '推开' in orange.
```

## 04 - 过程比结论值钱

**对应图**: `doc/images/whiteboard-vs-doc/04-process-wins.png`
**结构类型**: 隐喻
**小凡姿态**: 站在天平旁,一只手推天平,另一手指白板

```text
Generate a 16:9 horizontal Chinese article illustration on pure white background. Style: casual whiteboard quick sketch, slightly shaky pen lines, not refined. Sparse annotations. The illustration shows a strange low-tech seesaw balance. On the left side, a perfectly organized document stack (gray, heavy, drawn with more rigid lines). On the right side, a messy whiteboard (drawn with very loose lines, with arrows, question marks, the word '过程'). The right side is tilted UP (lighter, more dynamic), the left side is tilted DOWN (heavier). Xiaofan (a young Asian man with short messy black bangs, narrow single-eyelid eyes, thin lips, deadpan calm expression, hand-drawn line art) stands beside the balance, half-body, one hand pushing the right side up, the other hand pointing at the tilted board, deadpan expression slightly off-balance. He is the main action subject. Lots of white space. Do not draw a title in the corner. No cute, no mascot, no PPT style. Chinese handwritten labels: '文档' in gray / '白板' in orange / '过程 > 结论' in red.
```

## 实战复盘

### 优点

- IP 出现且承担核心动作 ✓
- 16:9 比例 ✓
- 纯白底 + 黑色手绘线稿 ✓
- 中文标注 ≤8 处 ✓
- 配色遵守 warm-ink 调色板 ✓
- 4 张图主题各异(陷阱/前后对比/隐喻/隐喻) ✓

### 不足

- **姿态变化不够**: 4 张图小凡主姿态都是"站+看/做",只覆盖 1.5 个维度。实际"3 维度变化"没做到。
- **物件变化单一**: 4 张图都用了"低科技物理隐喻"(被擦掉的文档/白板/压面机/天平),有反复刻风险。
- **小凡的脸一致性**: v1 阶段 4 张图基于原始证件照独立生成,脸之间可能有微妙差异。v2 阶段改用 `standard.png` 作参考可改善。

### 改进方向

- 实战重跑时,刻意用"非站"姿态:蹲在文档里挖问号 / 半个身子探出白板 / 卡在天平上 / 被什么绊住的瞬间
- 物件维度再加新隐喻池,避免每张都用"低科技机器"做隐喻
- 所有新图都用 `standard.png` 作 input_file_paths,而不是原始证件照

详见 `xiaofan-ink/references/composition-patterns.md` 的"实战反复刻陷阱"段。
