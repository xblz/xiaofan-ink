# 生图提示词模板

> v2.8.43 基准(2026-10-26 重写)。
> 完整 IP 设计、调色板、反复刻规则分别见 `xiaofan-ip.md` / `style-dna.md` / `composition-patterns.md`。
> 标准 IP 描述段直接复制 `assets/prompts/_standard-ip-description.md` **v2.8.43 段**。
> 实战示例见 `assets/prompts/articles/` 和 `assets/prompts/skill-samples/`。

---

## ⛔ 模板使用规则 (先读)

1. **两套模板**: 公众号 16:9 / 抖音 1:1。**不要混用** —— 它们的留白要求和人物占比要求相反。
2. **IP 形态段必写**, 不是可选。参考图 (`standard.png`) 是主锚,但**只靠 reference 渲染器会自由发挥**。
   v2.8.42 事故就是"只靠 reference + 加禁令" → IP 被削成后梳大背头。
3. **禁填充用正向写法**。`Pure line drawing. Do NOT fill ... with solid black or grey.` **已实测失效** (头发变实心黑块 / 太浅像白发)。
4. **文字锁定写「整张图里唯一的文字」**, 不是「画面中标注 X」。
5. 生图前跑 `python3 xiaofan-ink/tools/ip-preflight.py check-prompt <prompt文件>`, 缺项会被拦。

---

## 模板 A: 公众号 (16:9) — 场景叙事 / 信息图解

> 公众号要**人物在场景里**, 不是浮在白底上的物件符号。
> 判据: **删掉人物后图还成立 = 空壳 = 重画。**

```text
Generate a 16:9 horizontal Chinese article illustration on pure white background.
Style: casual hand-drawn line illustration, loose sketchy strokes with visible flying-white gaps, lines not fully closed, like a sketch drawn on a whiteboard.
Full scene with environment: draw the room, the furniture, the table, the floor line, the background objects that make the scene real.
The person is IN the scene, not floating in white space. The person should be the main subject, drawn at a large scale, usually from the waist up or closer.
Detailed objects: draw them with real detail, not as plain geometric symbols.
Line quality: loose and sketchy, like a quick drawing on a whiteboard. Visible flying-white gaps inside strokes, lines that do not close, uneven pressure, a few overshooting strokes at the edges.
NOT clean vector art, NOT polished commercial line illustration, NOT thin uniform pen strokes, NOT digital perfect lines.
NOT manga, NOT anime, NOT comic book art, NOT photorealistic, NOT semi-realistic rendering.
NO large stylized anime eyes, NO sharp V-shaped anime jaw, NO exaggerated eyelashes.
EVERYTHING is thin black pencil lines on white paper. NOTHING is filled in with solid colour.
Hair is drawn with a few loose sketchy strokes that let the white paper show through the strands, never a solid black shape, never a black silhouette, never flat black.
Clothing, faces, furniture and objects are all outline only, no shading, no grey tone.
This is a rough sketch, not a finished illustration: NO cel shading, NO gradient, NO cross-hatching.

Xiaofan (a young Asian man, hand-drawn line art, matching the IP reference standard.png):
HAIR - most important, do not skip: black messy short hair. A spiky pointed fringe falls across the forehead, strands hanging down to just above the eyebrows, hair tips pointed, a few separate strands, drawn with a few quick sketchy strokes and some flying-white gaps. The fringe MUST be visible on the forehead. NOT slicked back, NOT combed back, NOT brushed back, NOT a pompadour, NOT cropped hair with the forehead exposed.
HAIR DENSITY - the hair must be built from MANY separate overlapping black strokes, short directional strand lines, so the hair reads clearly DARK like black hair, while individual strand lines and small white gaps stay visible inside it. It is textured line work, NOT a flat solid black fill, NOT a black silhouette, NOT pale grey hair, NOT white hair.
FACE - long oval face, clean jawline, slightly narrow chin.
EYES - narrow slit-like eyes. Each eye is ONE thin elongated line, slightly downward-slanting, with ONE tiny solid black dot at the INNER corner. The eye is a fine line only, drawn like a narrow closed slit. NO white of the eye, NO eyeball, NO visible sclera, NO round pupil, NO iris, NO big dark circle, NO open anime eye.
EYEBROWS - extremely faint, thin, short slanted strokes, like a light pencil trace, much lighter than the hair. Barely there, but present. NOT thick, NOT heavy, NOT solid black, NOT dark.
LIPS - thin, ONE short flat line.
SKIN - no skin tone, no shading, no blush. NO hatching on the cheeks, NO blush lines, NO contour shading.
HANDS - simple sketchy outlines drawn with a few loose lines, simplified, normal size in proportion to the body, with visible knuckles and naturally separated fingers. NO fingernails, NO knuckle wrinkles, NO skin folds, NO anatomical detail, NOT blobs, NOT mittens, NOT three-stroke placeholders, NOT a large foreground close-up.

{场景变量段: 谁 / 在哪 / 正在做什么 / 画面里的物件 / 视角}

{如果这张图要文字}
The ONLY text in the entire image: {文字} - {颜色} brush handwriting, {位置}.
No red circle, no arrows, no other marks.

⛔ ABSOLUTELY NO TEXT anywhere except the exact text stated above.
NO captions, NO labels, NO annotations, NO arrows pointing at things, NO callouts, NO explanation text, NO summary boxes.
NO writing of any kind on any object, no text on walls, no text on screens, no text on papers, no menu, no signage, no posters.
do NOT write any color codes, hex codes, hash symbols, or alphanumeric strings.
NO brand name, NO logo, NO watermark, NO signature, NO English text, NO pinyin.
```

## 模板 B: 抖音 (1:1) — 图解型 + 大量留白

> 抖音是**图解型**, 主体小、留白大、纯白底。
> **跟模板 A 的差异只在风格段后半 + 比例要求, IP 段和禁填充段完全一样。**

```text
Generate a square 1:1 Chinese social-media illustration on pure white background.
Style: casual hand-drawn line illustration, loose sketchy strokes with slight flying-white gaps, lines not fully closed, minimal composition.
Subject occupies 40-60% of the frame. Very large empty white space. Quiet and sparse.
Line quality: loose and sketchy, like a quick drawing on a whiteboard. Visible flying-white gaps inside strokes, lines that do not close, uneven pressure, a few overshooting strokes at the edges.
NOT clean vector art, NOT polished commercial line illustration, NOT thin uniform pen strokes, NOT digital perfect lines.
NOT manga, NOT anime, NOT comic book art, NOT photorealistic, NOT semi-realistic rendering.
NO large stylized anime eyes, NO sharp V-shaped anime jaw, NO exaggerated eyelashes.
EVERYTHING is thin black pencil lines on white paper. NOTHING is filled in with solid colour.
Hair is drawn with a few loose sketchy strokes that let the white paper show through the strands, never a solid black shape, never a black silhouette, never flat black.
Clothing, faces, furniture and objects are all outline only, no shading, no grey tone.
This is a rough sketch, not a finished illustration: NO cel shading, NO gradient, NO cross-hatching.

Xiaofan (a young Asian man, hand-drawn line art, matching the IP reference standard.png):
{跟模板 A 的 IP 段完全一样, 直接复制}

{场景变量段}

{如果这张图要文字}
The ONLY text in the entire image: {文字} - {颜色} brush handwriting, {位置}.
No red circle, no arrows, no other marks.

⛔ ABSOLUTELY NO TEXT anywhere except the exact text stated above.
NO captions, NO labels, NO annotations, NO arrows pointing at things, NO callouts, NO explanation text, NO summary boxes.
NO writing of any kind on any object, no text on walls, no text on screens, no text on papers, no menu, no signage, no posters.
do NOT write any color codes, hex codes, hash symbols, or alphanumeric strings.
NO brand name, NO logo, NO watermark, NO signature, NO English text, NO pinyin.
```

---

## ⛔ 绝对不要写进 prompt 的东西 (会触发错误风格)

| ❌ 不要写 | 原因 | ✅ 改写成 |
|---|---|---|
| `Pure line drawing. Do NOT fill ... with solid black or grey.` | 抽象禁令, 实测不管用 | 模板里的 `EVERYTHING is thin black pencil lines...` + `HAIR DENSITY` |
| `NO eyebrows at all` | 连淡短眉也砍了 | `EYEBROWS - extremely faint, thin, short slanted strokes` |
| `The area between hairline and eyes must be BLANK` | 逼出"后梳露额头", 抹掉刘海 | `The fringe MUST be visible on the forehead` |
| `hair is slicked back` / `brushed back` / `forehead exposed` | 直接删掉 IP 核心识别特征 | `NOT slicked back, NOT combed back...` |
| `one hand with only 3-4 loose sketchy strokes, fingers together` | 把手画僵成卡通手 | `HANDS - ... visible knuckles and naturally separated fingers` |
| `minimalist black hand-drawn line art` | 触发极简 | `casual hand-drawn line illustration` |
| `loose sketch, not refined` 单独使用 | 触发极简 stick figure | `loose sketchy strokes with visible flying-white gaps` |
| `absurd` / `crazy` / `weird` | 触发日漫 Q 版 | 删掉 |
| `with handwritten annotations around it` | **教渲染器画批注** (v2.8.39 根因) | 删掉, 用 `The ONLY text in the entire image:` |

---

## input_file_paths (必传)

每张图生成时,必须传 `xiaofan-ink/assets/ip-reference/standard.png` 作参考输入。**不要用原始证件照**。

```python
input_file_paths = ["xiaofan-ink/assets/ip-reference/standard.png"]
```

> ⚠️ **reference 是主锚, 不是"低频校准"** —— SKILL.md 早期写的"只作低频视觉校准"是错的, v2.8.42 事故的直接原因之一。
> **但 reference 不能单独用**: 必须同时写 IP 形态段, 否则渲染器自由发挥。

---

## 表情选择 (可选用, 默认不写)

> 详细表情库见 `xiaofan-ink/references/xiaofan-ip.md` 表情库段。

**默认**:不写表情词,靠 standard.png reference 自然呈现。

**什么时候用表情**:
- 核心意思是"小凡在某个情绪中" (如:突然想通、做完收工) → 补充微表情词
- 核心意思是"小凡在做某件事" (如:搬素材、拉线、卡住) → 保持 deadpan,不要乱加情绪

**纪律**: 同文最多 2-3 种不同表情;表情和装扮可叠加,一张图最多 1 表情 + 1 装扮。

> ⚠️ **加表情 ≠ 可以省 IP 形态段。** 表情是叠加项, 刘海/眉/眼/脸型是底色, 永远都要写。

---

## 图像编辑提示 (生成后微调用)

### 去掉错误标题或标签

```text
Edit the provided image. Remove only the handwritten label "{要删除的文字}" and its underline. Fill that area with the same clean white background, matching the surrounding blank paper. Preserve everything else exactly: characters, body, labels, paths, line style, composition, aspect ratio, and image quality. Do not add any new text or objects.
```

### 让小凡更"做事" (修复"小凡只是装饰")

```text
Regenerate this illustration with the same core meaning and simple layout, but make Xiaofan more central to the conceptual action. Xiaofan should be doing the strange work that explains the idea, not standing beside the diagram. Keep the same loose line-drawn style.
```

### 修 IP 形象 (刘海缺失 / 眉眼失真) —— 局部修复

```text
Edit only the face and hair of the person in this illustration. Restore the spiky pointed fringe hanging across the forehead to just above the eyebrows, keep the long oval face and clean jawline, draw the eyes as narrow slit-like fine lines with one tiny solid black dot at the inner corner, and make the eyebrows extremely faint thin short slanted strokes much lighter than the hair. Keep everything else in the image exactly as it is: the body, the pose, the environment, the objects, the text, the colors, the line quality.
```

---

## 实战:复制模板 → 填变量 → 跑 preflight

```bash
# 1. 复制模板 A (公众号) 或模板 B (抖音) 到一个 .txt
# 2. 填变量段
# 3. 自检 (缺项会被拦)
python3 xiaofan-ink/tools/ip-preflight.py check-prompt 你的prompt.txt
```

preflight 会检查: 刘海约束 / 禁填充正向段 / HAIR DENSITY / 眉眼正向描述 / 文字锁定句 / 危险词(后梳、无眉禁令、抽象填充禁令) / 比例要求是否跟平台匹配。
