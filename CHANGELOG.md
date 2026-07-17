# CHANGELOG

> xiaofan-ink 项目关键改动记录。每次有意义改动都更新一行(或一段)。
>
> 完整 git 历史见 `git log --oneline`。本文件只记**功能级别**的改动,小修小补不进。

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
