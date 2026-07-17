# 生图提示词模板

> v0.8 基准,基于"线稿版的我"风格(参考 1a25ff2 实战 1 的 IP 形象)。
> 完整 IP 设计、调色板、反复刻规则分别见 `xiaofan-ip.md` / `style-dna.md` / `composition-patterns.md`。
> 标准 IP 描述段直接复制 `assets/prompts/_standard-ip-description.md`。
> 实战示例见 `assets/prompts/articles/` 和 `assets/prompts/skill-samples/`。

---

## 模板(每张图单独生成)

每个 prompt 由以下几段拼接而成,变量用 `{}` 标记:

### 1. 风格 + IP 描述(固定段,直接复制)

```text
Generate a 16:9 horizontal Chinese article illustration on pure white background. Style: casual hand-drawn line illustration. Xiaofan is a loose line-drawn self-portrait with recognizable features. The face must look like the same Xiaofan as the reference. Xiaofan must perform the core conceptual action, not decorate the scene. He is the main action subject. Lots of white space. Do not draw a title in the corner. No PPT, no flowchart, no commercial vector style, no realistic photo elements.
```

### 2. 主题 / 结构 / 核心意思(变量段)

```text
Theme:
{正文配图主题}

Structure type:
{结构类型:Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜}

Core idea:
{这张图要表达的核心意思}
```

### 3. 构图(变量段)

```text
Composition:
{具体画面:小凡在哪里、正在做什么、主要物件是什么、信息如何流动}
```

### 4. 中文标注(变量段)

```text
Chinese handwritten labels:
{标注词1} in {颜色} / {标注词2} in {颜色} / {标注词3} in {颜色} / ...
```

颜色只用 warm-ink 4 色:黑 (#1A1A1A) / 红 (#C0392B) / 橙 (#E67E22) / 蓝 (#2C5F8D)。每张图 1-2 种标注色,不要超过 3 种。

### 5. 约束(固定段,直接复制)

```text
Constraints:
Do not copy prior examples or reuse known case compositions; invent a fresh visual metaphor for this specific article. It should be clear but not instructional, interesting but not childish, strange but clean. Keep the main subject around 40-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. The image must look like a casual hand-drawn line illustration, NOT a polished commercial illustration.
```

---

## input_file_paths(必传)

每张图生成时,必须传 `xiaofan-ink/assets/ip-reference/standard.png` 作参考输入。**不要用原始证件照**(已移到 `.ip-dev/legacy-examples/`,且 `standard.png` 是更稳定的"线稿版的我"基准)。

```python
input_file_paths = ["xiaofan-ink/assets/ip-reference/standard.png"]
```

---

## 完整 prompt 示例(实战 1 第一张)

```text
Generate a 16:9 horizontal Chinese article illustration on pure white background. Style: casual hand-drawn line illustration. Xiaofan is a loose line-drawn self-portrait with recognizable features. The face must look like the same Xiaofan as the reference. Xiaofan must perform the core conceptual action, not decorate the scene. He is the main action subject. Lots of white space. Do not draw a title in the corner. No PPT, no flowchart, no commercial vector style, no realistic photo elements.

Theme: 文档的陷阱 - 完美规整的文档把'还没想清楚'的部分抹掉了。

Structure type: 概念隐喻

Core idea: 完整规整的文档把最有价值的"还没想清楚"部分擦掉了。

Composition: A thick perfect document lying open. Xiaofan is half-squatting INSIDE the document, his upper body sticking up out of it like he fell into it, one hand reaching out holding a question mark he just rescued from being erased, the other hand steadying himself on the document edge. He looks at the erased spots with a deadpan expression.

Chinese handwritten labels: '完整 规整 自洽' in blue / '?' in red, being rescued / '擦掉' in orange

Constraints: Do not copy prior examples or reuse known case compositions; invent a fresh visual metaphor for this specific article. It should be clear but not instructional, interesting but not childish, strange but clean. Keep the main subject around 40-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. The image must look like a casual hand-drawn line illustration, NOT a polished commercial illustration.
```

---

## 图像编辑提示(图像生成后微调用)

### 去掉错误标题或标签

```text
Edit the provided image. Remove only the handwritten label "{要删除的文字}" and its underline. Fill that area with the same clean white background, matching the surrounding blank paper. Preserve everything else exactly: characters, body, labels, paths, line style, composition, aspect ratio, and image quality. Do not add any new text or objects.
```

### 让小凡更"做事"(修复"小凡只是装饰"的失败)

```text
Regenerate this illustration with the same core meaning and simple layout, but make Xiaofan more central to the conceptual action. Xiaofan should be doing the strange work that explains the idea, not standing beside the diagram. Keep the same loose line-drawn style.
```

---

## 实战 prompt 模板(实战生成时,直接复制这个模板 + 填变量)

```text
Generate a 16:9 horizontal Chinese article illustration on pure white background. Style: casual hand-drawn line illustration. Xiaofan is a loose line-drawn self-portrait with recognizable features. The face must look like the same Xiaofan as the reference. Xiaofan must perform the core conceptual action, not decorate the scene. He is the main action subject. Lots of white space. Do not draw a title in the corner. No PPT, no flowchart, no commercial vector style, no realistic photo elements.

Theme: {主题}

Structure type: {结构类型}

Core idea: {核心意思}

Composition: {构图}

Chinese handwritten labels: {标注} in {颜色} / ...

Constraints: Do not copy prior examples or reuse known case compositions; invent a fresh visual metaphor for this specific article. It should be clear but not instructional, interesting but not childish, strange but clean. Keep the main subject around 40-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. The image must look like a casual hand-drawn line illustration, NOT a polished commercial illustration.
```

实战时:复制这个模板,填 5 个变量(Theme/Structure type/Core idea/Composition/Chinese labels),传 `standard.png` 作参考。
