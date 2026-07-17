# CHANGELOG

> xiaofan-ink 项目关键改动记录。每次有意义改动都更新一行(或一段)。
>
> 完整 git 历史见 `git log --oneline`。本文件只记**功能级别**的改动,小修小补不进。

---

## v1.4 — 2026-07-17(公众号"小凡的草稿本" brand 资源)

为微信公众号申请做准备,建立完整 brand 资源库,跟 xiaofan-ink skill 内容库解耦。

**新增 `brand/` 目录**:
- `brand/README.md` — 公众号基础信息 + 简介(主用 / 备选 1 / 备选 2)
- `brand/avatar.png` — 头像(1:1 撕下草稿纸 + 小凡简笔 + 暖色 highlight,圆形裁切友好)
- `brand/welcome.md` — 关注欢迎语 + 6 个关键词自动回复(目录/草稿/投稿/关于/ip/草稿本)
- `brand/menu.md` — 公众号自定义菜单(3 个一级菜单设计:草稿本/草稿碎片/关于小凡)
- `brand/style-guide.md` — 视觉规范(配色/字体/排版/封面/头图/不做的事)

**公众号"小凡的草稿本"基本定位**:
- 名:`小凡的草稿本`(6 字,跟 001 主题"写废稿"呼应)
- 简介(主用):`过程比结论值钱的实验。写点工具反思、节奏、专注,跟"小凡"一起想。`
- 调性:deadpan 冷静 / 反思 / 冷幽默 / 不卖萌 / 不喊口号
- 关联仓库:xiaofan-ink(本仓库)
- 关联系列:《小凡墨水周记》(`doc/essays/`)
- 更新:每周三 1 篇
- 类型:个人订阅号

**整体项目结构更新**:
- 顶层 `README.md` 目录树增加 `brand/` 段,标注"v1.4+ 公众号 brand 资源"
- `doc/essays/README.md` 顶部加"关联公众号:小凡的草稿本",末尾加"发布到公众号"小节
- 实战 1/2/3 顶部"非 essays 正式系列"注保留
- 实战样本职责继续划清

**后续可扩展**:
- 公众号 API 自动化推送(把 `doc/essays/00X-*.md` 推到公众号草稿箱)
- 公众号菜单"最新文章"自动同步脚本
- 关注自动回复 + 关键词回复上线

---

## v1.3 — 2026-07-17(系列第 2 篇 + 托管创作规则升级)

### CREATION-PLAN 规则升级

- **主题由 agent 自主决定**:用户只给"创作一篇"触发,agent 从角度池+历史避重里选(默认走 B 模式)
- **图片不固定张数**:按认知锚点数量决定(3-6 张灵活),不再固定 4 张
- **用户参与减少**:不参与选主题,只审稿+决定发布到哪里(发布平台后续可托管)

### 系列第 2 篇(《专注力的边界》)

- 文章:`doc/essays/002-focus-boundary.md`(约 600 字,5 段)
- 5 张配图:`doc/essays/images/002-focus-boundary/01-05.png`
- 实战 prompt 库:`xiaofan-ink/assets/prompts/articles/002-focus-boundary.md`

### 第 2 篇轮换记录

- 表情:3 default + 1 confused + 1 satisfied (3 种,5 张图)✓ 符合 SERIES-STATE
- 装扮:1/5 用(咖啡杯,只在图 04)
- 姿态:5 different(卡钟形罩 / 坐空桌 / 卡门槛 / 端咖啡 / 站桌)
- 物件:钟形玻璃罩 / 番茄钟 / 笔记本 / 门 / 白板(全部新)

### 主题配对策略

002 跟 001 形成"反思时间管理"姐妹篇:
- 001:列计划(节奏类)
- 002:深度专注(专注类)
- 角度不同但主题相邻,形成系列内部连贯性

### takeaway(给下一篇用)

- 满足表情 prompt 措辞仍然不够明显(连续 2 篇问题),第三次验证:下次"嘴角上扬"组合"半闭眼"或"almost-smile"
- 卡门槛类的"门/框/边界"姿态,身体位置要明显在中间,脚不要伸出去
- 端杯子时让小凡放松(肘撑桌)比"教学性按笔记本"更自然

---

## v1.2 — 2026-07-17(长期创作计划 + 系列首发)

建立《小凡墨水周记》正式系列,把仓库从"skill 验证库"升级到"长期创作内容库"。

**新增文档**:
- `doc/CREATION-PLAN.md` — 长期创作规范(系列定位/节奏/结构/流程/决策/基础设施/长期视角)
- `doc/SERIES-STATE.md` — 防重复数据库 + 三维轮换状态跟踪(姿态/装扮/物件已用未用清单)
- `doc/essays/README.md` — 系列说明,跟实战样本划清职责

**新增目录**:
- `doc/essays/` — 正式发布内容(从 001 开始)
- `doc/essays/images/00X-<slug>/` — 配图(同号子目录)

**新增内容**(系列第 1 篇):
- `doc/essays/001-why-i-dont-do-daily-plan.md` — 《为什么我不再做每日计划》(约 600 字,4 段)
- `doc/essays/images/001-why-i-dont-do-daily-plan/01-04.png` — 4 张配图
- `xiaofan-ink/assets/prompts/articles/001-why-i-dont-do-daily-plan.md` — 实战 prompt 库

**第 1 篇轮换记录**(严格执行 SERIES-STATE 防反复刻):
- 表情:2 默认 + 1 困惑 + 1 满足(实战 3 用了思考/疲惫,本次换困惑/满足)
- 装扮:1/4 用(咖啡杯,实战 2 用过耳机/工具包/笔记本,实战 3 没用)
- 姿态:4 种全部为新(卡纸堆 / 洞里伸手 / 蹲角落 / 站回头)
- 物件:纸堆 / 洞 / 桌(实战 1-3 没用过)

**实战样本划清职责**:
- `doc/whiteboard-vs-doc.md` / `doc/why-i-quit-gtd.md` / `doc/why-i-write-drafts.md` 顶部加"状态:skill 实战验证样本,非《`essays/`》正式系列"
- 这 3 篇继续作为 skill 能力展示,但不计入正式系列

**系列元决定**(拍板项):
- 系列名:《小凡墨水周记》
- 频率:每周 1 篇(每周三)
- 长度:600-1000 字
- 配图:4 张
- 视觉:warm-ink 4 色,小凡 deadpan 默认 + 1-2 种微表情

**第 1 篇 takeaway(给下一篇用)**:
- 收尾用满足时 prompt 措辞要更明显("slight 1-2mm mouth upturn" 不够,改 "slight 3-4mm mouth upturn" 或加 "almost-smile")
- "试图接" + "困惑" 组合容易让 body 跟 face 不连戏,要么统一方向要么去掉意图
- 桌面/桌子的"满"会挤压小凡,小物件(杯/瓶/小盒)效果更好

---

## v1.1 — 2026-07-17(实战 3 — 表情库首篇实战)

基于 v1.0 新增的"微表情库",写第三篇实战示例文章,验证表情库在实战中的效果。

**新增文章 + 配图**:
- `doc/why-i-write-drafts.md` — 第三篇实战文章(约 600 字)
  - 主题:为什么我开始主动写"废稿"(写作方法反思)
  - 4 段配 4 张图,1 个结论
- `doc/images/why-i-write-drafts/01-draft-pile.png` — 废稿堆(deadpan 默认)
- `doc/images/why-i-write-drafts/02-three-openings.png` — 三个被划掉的开头(思考表情)
- `doc/images/why-i-write-drafts/03-rewrite.png` — 推倒重来(疲惫表情)
- `doc/images/why-i-write-drafts/04-real-cost.png` — 成本是废稿(deadpan 默认)

**新增实战 prompt 库**:
- `xiaofan-ink/assets/prompts/articles/why-i-write-drafts.md`
  - 4 张图各自的 5 段 prompt(Theme/Structure type/Core idea/Composition/Chinese labels)
  - 表情选词理由 + 表情使用复盘
  - 反复刻陷阱预标记

**表情使用复盘**:
- 4 张图用了 **2 默认 + 1 思考 + 1 疲惫**
- 情绪节奏:平 → 思考 → 疲惫 → 平(完整呼吸)
- 4 张图全部一次过,无重出
- 表情库设计验证成功:微表情在 deadpan 底色上有效传递 1 度情绪,又不破坏"白板随手画"清冷气质

**实战结论**:
- 表情库使用纪律(同文最多 2-3 种 + 一旦加表情必须删掉 deadpan)在实战中可操作
- prompt 替换词(`slightly raised right eyebrow, eyes looking down-left` 等)直接生效,没额外 trigger 错误风格
- 表情库和备选装扮(本篇未用)可独立/叠加使用,互不冲突

**walkthrough 扩展**:
- `doc/walkthrough.md` 顶部"准备工作"段加表情库提示
- 新增"7.6 表情库怎么用?"FAQ 段
- 新增"8. 附录 B:实战案例集"section,含实战 1/2/3 三篇对比表 + 实战 3 表情库实战细节
- 实战案例集定位:作为后续实战的参考,展示表情库如何从 v0.5 反复刻陷阱 → v0.6 改进 → v1.0 表情库的战绩

---

## v1.0 — 2026-07-17(微表情库)

基于 deadpan 底色,加 5 个微表情变体,让"小凡-读者"的情感连接更具体。

**新增 5 张表情变体**(`xiaofan-ink/assets/ip-reference/variants/`):
- `07-thoughtful.png` — 思考(右眉微挑 / 眼斜看 / 嘴闭)
- `08-confused.png` — 困惑(眉心微聚 / 眼微眯 / 嘴微松)
- `09-tired.png` — 疲惫(眉尾下垂 / 眼半闭 / 嘴松)
- `10-surprised.png` — 惊讶(眉上挑 / 眼睁大 1.2x / 嘴微张)
- `11-satisfied.png` — 满足(嘴角微扬 1-2mm / 眼微眯 / 眉平)

**风格校准**:
- 5 张全部用 standard.png 作 input_file_paths,跟现有 01-06 outfit 变体完全一致
- 全部保持纯线稿无填色,跟 standard.png / head-think.png 等核心参考图风格一致
- 表情都是 deadpan 底色上的 1 度微变化,**不是大表情** — 不会触发"日漫/吉祥物/表情包"错误风格

**文档更新**:
- `xiaofan-ink/references/xiaofan-ip.md` — 新增"表情库(可选用)"section
  - 列出 5 个微表情及适用场景
  - 强调"微表情,不是夸张五官"
  - 强调"表情库和备选装扮可叠加,但一张图最多 1 表情 + 1 装扮"
- `xiaofan-ink/assets/prompts/_standard-ip-description.md` — 新增"表情选项(可选用)"section
  - 表情-prompt 用词对照表(英文 prompt 替换词)
  - 提供带表情的 IP 描述段示例
- `xiaofan-ink/references/prompt-template.md` — 新增"表情选择(可选用)"section
  - 明确"默认 deadpan 即可,什么时候用表情"
  - 表情使用纪律(同文最多 2-3 种 + 一旦加表情必须删掉 deadpan)
  - 3 个实战示例(默认 / 思考 / 满足)

**表情使用纪律**:
- 默认一律 deadpan,不要每张图都加情绪
- 同一篇文章里,多张图最多 2-3 种不同表情
- 一旦加表情,IP 描述段里 `deadpan calm expression` 必须删掉,避免和表情词冲突

**为什么是 v1.0**:
- 之前 v0.x 阶段是"个人用、私有项目阶段"
- v1.0 是"表情库建立完整"的里程碑 — IP 三维度全部到位(姿态/装扮/表情)
- 后续如果公开,从 v1.x 继续

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
