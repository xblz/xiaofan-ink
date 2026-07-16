# 小凡墨水 / Xiaofan Ink

> 把中文文章里的判断、流程、状态和隐喻,变成一张张白底、手绘、怪诞但清爽的正文配图。
>
> 16:9 横版 | 小凡 IP | 纯白手绘 | 少量红橙蓝中文批注 | Codex Skill
>
> ⚠️ 本仓库是 fork 自 [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) 的私有项目,已替换视觉 IP 为"小凡",原作者 Ian 的"小黑"IP 仍归原作者所有,详见 NOTICE.md。

---

## 这个仓库是什么

小凡墨水 是一个 Codex Skill,用来指导 AI Agent 为中文文章、帖子、博客、Notion 文档和方法论内容生成正文配图。

它不是通用插画 prompt,也不是 PPT 信息图模板。它的核心目标是:先理解文章里的认知锚点,再把其中一个判断、流程、结构、状态或隐喻,变成一张有记忆点的 16:9 手绘解释图。

默认视觉 IP 是"小凡":一个细长单眼皮、碎短发、薄唇、平静表情的年轻亚洲男性,基于真人手绘风格化转译,保持白板速写感的线稿气质。小凡不是吉祥物,不是贴纸,也不是站在角落里的装饰物,而是正在认真参与系统运转的荒诞工作者。

一句话:**让 AI 不只是"配一张图",而是把文章里的一个关键认知动作画出来。**

---

## 适合谁用

特别适合:

- 写中文文章,需要正文配图和文章插图的人
- 做知识型内容、方法论内容、AI 工作流内容的人
- 想把抽象判断画成具体隐喻的人
- 想要一种比 PPT 信息图更轻、更怪、更有个人识别度的配图风格的人
- 用 Codex 做内容生产,希望稳定复用一套视觉语言的人

不适合:

- 想要商业插画、品牌 KV 或精致扁平插画的人
- 想要传统 PPT 信息图、复杂架构图或流程图的人
- 想要儿童卡通、可爱 IP、表情包风格的人
- 想把大量正文、长段解释或完整课程页塞进一张图里的人
- 需要严格可编辑矢量源文件的人

---

## 它会产出什么

默认输出:

- 16:9 横版正文配图
- 一篇文章的 4-8 张 shot list
- 每张图的主题、核心意思、结构类型、小凡动作和中文标注建议
- 最终 PNG 图片,保存到 workspace 的 `assets/<article-slug>-illustrations/`

默认不输出:

- PPTX / PDF / Keynote
- SVG / HTML / Canvas 可编辑图
- 商业海报或封面 KV
- 大段文字型信息图

---

## 视觉风格

这个 skill 默认使用"小凡怪诞正文配图"风格:

- 纯白背景,不要纸纹、米色、阴影、渐变
- 黑色手绘线稿,细线,轻微抖动
- 大量留白,主体只占画面约 40%-60%
- 少量红色、橙色、蓝色中文手写批注
- 一张图只表达一个核心动作、结构、状态或隐喻
- 小凡必须参与核心动作,不能只是装饰
- 怪诞、有创意、清爽,但不幼稚、不卖萌

具体调色板(温暖墨水感)见 `xiaofan-ink/references/style-dna.md`:黑 `#1A1A1A` / 红 `#C0392B` / 橙 `#E67E22` / 蓝 `#2C5F8D`。

---

## 示例效果

### 混乱到聚焦

![混乱到聚焦](xiaofan-ink/assets/examples/01-chaos-to-focus.png)

### 两个断点

![两个断点](xiaofan-ink/assets/examples/02-two-breakpoints.png)

### 信息汇聚

![信息汇聚](xiaofan-ink/assets/examples/03-info-converge.png)

### 一稿多用

![一稿多用](xiaofan-ink/assets/examples/04-one-source-many-shapes.png)

### 内容发酵

![内容发酵](xiaofan-ink/assets/examples/05-content-ferment.png)

### 信任桥

![信任桥](xiaofan-ink/assets/examples/06-trust-bridge.png)

这些图片是风格校准样例，不是构图模板。使用时应该从当前文章重新发明隐喻，不要照抄这些样例的物件和构图。同一篇文章的多张图，要让小凡的姿态、动作、物件、视角至少有 3 个不同维度在变化，具体见 `xiaofan-ink/references/composition-patterns.md` 的"反复刻规则"段。

> 根目录 `examples/images/` 仍保留原作者 Ian 的 8 张样例图，作为原版视觉风格的版权样例存档，仅供查阅。

---

## 安装

本仓库是私有项目,直接本地复制 skill 目录到 Codex skills 目录即可:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ./xiaofan-ink "${CODEX_HOME:-$HOME/.codex}/skills/"
```

安装后,在 Codex 里使用:

```text
Use $xiaofan-ink 为这篇中文文章设计并生成 5 张小凡怪诞正文配图。
```

---

## 怎么用

### 只做配图规划

```text
Use $xiaofan-ink 先不要生图。
请分析下面这篇文章哪里值得配图,输出 5 张左右的 shot list。
每张图写清楚:放在哪段后、主题、核心意思、结构类型、小凡在做什么、建议中文标注词。

<粘贴文章>
```

### 直接生成正文配图

```text
Use $xiaofan-ink 把下面这篇文章生成 4 张小凡怪诞正文配图。
要求:16:9 横版、纯白背景、黑色手绘线稿、少量红橙蓝中文手写批注。

<粘贴文章>
```

### 为单个概念生成一张图

```text
Use $xiaofan-ink 为"信任不是喊出来的,而是一块证据一块证据铺过去"生成一张正文配图。
画面要怪诞但清爽,小凡必须承担核心动作。
```

### 去掉图里的标题或错误文字

```text
Use $xiaofan-ink 帮我编辑这张图,去掉左上角的"流程图"标题,其他内容保持不变。
```

更多示例见 [examples/prompts.md](examples/prompts.md)。

---

## 工作流程

这个 skill 的流程是:

1. 读取文章、Markdown、Notion 内容、截图或用户给的主题
2. 提炼核心观点、认知转折、流程结构和适合视觉化的段落
3. 先输出 shot list:每张图只选一个认知锚点
4. 为每张图选择结构类型:Workflow、系统局部、前后对比、角色状态、概念隐喻、方法分层、地图路线或小漫画分镜
5. 重新发明一个低科技、怪诞但成立的物理隐喻
6. 让小凡承担核心动作
7. 每张图单独调用图像模型生成
8. 按 QA checklist 检查:白底、留白、小凡动作、中文标注、非 PPT 感、非旧案例复刻
9. 保存最终 PNG,并报告用途和路径

---

## 目录结构

```text
.
├── README.md
├── LICENSE
├── NOTICE.md
├── assets/
│   └── ian-wechat-qr.jpg
├── examples/
│   ├── images/
│   │   ├── 01-two-breakpoints.png
│   │   ├── 02-sort-by-purpose.png
│   │   └── ...
│   └── prompts.md
└── xiaofan-ink/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── assets/
    │   └── ip-reference/
    │       ├── head-think.png
    │       ├── halfbody-climb.png
    │       └── scene-stuck.png
    └── references/
        ├── style-dna.md
        ├── xiaofan-ip.md
        ├── composition-patterns.md
        ├── prompt-template.md
        └── qa-checklist.md
```

真正需要安装到 Codex 的是子目录:

```text
xiaofan-ink/
```

根目录的 README、LICENSE、NOTICE 和 examples 是 GitHub 分享文档。

---

## 注意事项

- 图片里的中文文字越短越稳定。
- 每张图只讲一个核心结构,不要把文章做成说明书。
- 小凡必须承担核心动作;如果去掉小凡画面仍然完全成立,说明小凡太装饰了。
- 示例图只用于校准线条密度、留白、颜色克制和小凡参与方式,不要复刻构图。
- AI 图像模型可能出现错字、幻觉标签、风格漂移或多余标题,生成后需要检查。
- 如果中文错字严重,优先减少标注词并重生成。

---

## 相关项目

- [Ian Handdrawn PPT](https://github.com/helloianneo/ian-handdrawn-ppt) - 中文手绘技术 PPT-style 页面图生成 Skill
- [Awesome Claude Code Skills](https://github.com/helloianneo/awesome-claude-code-skills) - Claude Code Skills / Agents / Plugins 精选合集
- [Obsidian + Claude AI Second Brain](https://github.com/helloianneo/obsidian-ai-second-brain) - Obsidian + Claude AI 个人知识库搭建指南

---

## 关于作者

**Ian (伊恩)** - 产品设计师 / 一人公司实践者 / AI Builder

用 AI 团队打造一人公司。

- GitHub: [helloianneo](https://github.com/helloianneo)
- X/Twitter: [@ianneo_ai](https://x.com/ianneo_ai)
- 网站: [www.ianneo.xyz](https://www.ianneo.xyz)
- 微信: `ianneoxyz`
- 邮箱: hello.neoc@gmail.com

---

## 继续探索

这套小凡配图 Skill,是个人用 AI 搭建内容生产系统里的小工具之一。

如果你也在用 AI 做内容、知识库、工作流或产品化,可以继续看我的网站:[www.ianneo.xyz](https://www.ianneo.xyz)。

只想先观察,可以关注我的 [X/Twitter](https://x.com/ianneo_ai)。

想了解 Indie Builders Club,加微信:`ianneoxyz`,备注「OPC」。

<p>
  <img src="assets/ian-wechat-qr.jpg" alt="Ian 微信二维码" width="120">
</p>

不方便扫码也可以搜索微信:`ianneoxyz`。

---

## License

MIT License. See [LICENSE](LICENSE).
