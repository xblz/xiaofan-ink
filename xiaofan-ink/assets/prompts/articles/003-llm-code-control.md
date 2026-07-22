# 实战 7 — Claude Code 用了一周, 我关掉了(系列第 3 篇)

> 文章:`doc/essays/003-llm-code-control.md`
> 系列:《小凡墨水周记》第 3 篇
> 生成日期:2026-07-22 / 主题:工具反思 — 控制权类(跟 001 节奏 / 002 专注配对, 工具三部曲收尾) / 配图数:5(1 cover + 4 正文)
> 输入参考图:`xiaofan-ink/assets/ip-reference/standard.png`(有 IP 的图都引用)
> 表情分布:1 default + 1 confused + 1 satisfied(3 种, 4 张正文)
> 装扮:0/4 用(全部不拿道具, 强调"我 vs AI" 的人物关系)
> 姿态:4 different(看终端 / 切回敲 / 站凝视空 / 站桌回看)
> v1.8 IP 决策:动作型(看/敲/看/回看)→ 保留 IP 4 张; 状态型(散落代码 / 桌面)→ 去 IP 1 张(cover)

---

## 主题选择记录(agent 自主决定)

003 主题"对 AI 编程工具的控制权"由 agent 自主选:
- **避开历史**:001 用了"工具反思-节奏"(每日计划),002 用了"工具反思-专注"(番茄钟)
- **跟 001/002 配对**:001 谈"节奏"(列计划),002 谈"专注"(深度工作),003 谈"控制权"(AI 协助),形成"工具三部曲"
- **角度新切口**:"X 的边界"格式(承袭 002), 切口是"过程 > 结论"的延伸 — AI 跳过草稿直接交作品
- **deadpan 调性匹配**:跟 000 "过程比结论值钱" 直接呼应, 形成系列内部核心理念的递进
- **热点贴合**:2026 年 Claude Code / Cursor / Codex 全面爆发, "AI 依赖反思" 是技术圈最热话题之一, 但本文切入点是"过程", 不是"AI 替代论"
- **冷幽默收尾**:让 AI 写注释 — 注释这种"过程"AI 替代得了, 但代码本身不行

## v1.8 IP 决策应用

| 图 | 动作/状态 | 决策 | 理由 |
|---|---|---|---|
| cover (00) | 状态:陌生人代码 | 去 IP | 桌面 + 陌生代码 + 编辑器窗口, 纯物件 + 留白, 让读者凝视 |
| 01 看终端 | 动作: 站 + 看代码滚 | 保留 IP | 动作型, 体现"我跟代码的关系", IP 在场 |
| 02 散落代码片段 | 状态: 散乱 | 去 IP | 纯物件 + 留白, 失控状态, 不需要人 |
| 03 切回敲键盘 | 动作: 切回手动 | 保留 IP | 关键动作, IP 体现"切回"这个决定 |
| 04 站桌回看 | 动作: 站 + 回看 | 保留 IP | 收束段, 留白感, 体现"我"重新掌控 |

## 表情选型决策

| 图 | 表情 | 选词理由 |
|---|---|---|
| 01 看终端 | deadpan | "我应该高兴才对" 那种反讽的平静, deadpan 完美 |
| 02 散落代码 | (去 IP, 无表情) | 状态型不需要人 |
| 03 切回敲键盘 | **困惑**(08-confused) | "我慌的是失去什么" — 真困惑, 不是装 |
| 04 站桌回看 | **满足**(11-satisfied) | 收束的释然, "回到自己手写一行代码" |

情绪节奏:平 → (无) → 困惑 → 满足
表情种类:3 种(deadpan 1 + 困惑 1 + 满足 1)✓ 符合 SERIES-STATE "最多 2-3 种"

## 姿态轮换

4 张图全部为新姿态(实战 1-3 + 系列 001/002 没用过):
- 01: 站 + 看终端 (新)
- 03: 切回敲键盘 (新)
- 04: 站 + 凝视空桌面 (新, 跟 002 图 05 站桌回看不同, 这是空桌面)

## 物件轮换

新物件池:终端 / 显示器 / 代码片段 / 编辑器窗口(实战 1-3 + 001/002 没用过)
注意:咖啡杯系列 001/002 用了 1/4 + 1/5, 003 故意 0/4, 强调"我 vs AI"的人物关系, 不需要其他道具干扰

---

## 5 张图的完整 prompt

### 图 cover (00) — 陌生代码 (去 IP)

**结构类型**:概念隐喻
**对应图**:`doc/essays/images/003-llm-code-control/00-stranger-code.png`

```text
Theme: 陌生代码 - 打开 3 个月前的项目, 一个函数我不认识。

Core idea: 代码能跑, 测试过, 但我不认识它。AI 帮我写完留下的"陌生人遗产"。

Composition: A top-down view of a simple white desk. Center: an open laptop with the screen showing several lines of code in a monospace font - the code is clean, well-commented, but feels alien / unfamiliar. To the side, a small piece of paper with a hand-written note saying "这是我的吗?" in Chinese. The desk has lots of white space. No person visible. The whole image conveys "this code is not yours, even though it's in your project."

Chinese handwritten labels: '这是我的吗?' in red on the paper note / '能跑' in green next to the code / '不认识' in red on a small label near the screen
```

### 图 01 — 看终端 (deadpan, 站+看代码滚)

**结构类型**:概念隐喻
**对应图**:`doc/essays/images/003-llm-code-control/01-staring-terminal.png`

```text
Theme: 站在终端前看代码滚 - 跟代码的关系断了。

Core idea: 我站在我自己的代码前面, 但代码在动, 我跟不上。

Composition: Xiaofan is standing in front of a tall standing desk or workbench, looking at a large monitor / terminal screen. The screen shows code scrolling rapidly, lines moving too fast for him to read. Xiaofan is half-turned toward the viewer, with a deadpan calm expression as if he's watching a process he can no longer control. His posture is slightly stiff, not relaxed. The terminal window has a small "$_" cursor blinking. The whole scene conveys "I wrote this, but it's no longer mine."

Input: xiaofan-ink/assets/ip-reference/standard.png (Xiaofan's face for consistency)

Chinese handwritten labels: '我跟不上了' in red near Xiaofan's head / 'Ctrl+C' in orange on the terminal / '$_' in blue on the screen
```

### 图 02 — 散落代码片段 (去 IP)

**结构类型**:状态刻画
**对应图**:`doc/essays/images/003-llm-code-control/02-stray-snippets.png`

```text
Theme: 散落的代码片段 - 失去过程的痕迹。

Core idea: 草稿乱, 但那是"我还没想清楚"的痕迹。AI 跳过草稿, 留下的不是"过程"。

Composition: A top-down view of a desk surface (white background). Several short code snippets are scattered loosely across the desk, each on a different small piece of paper or sticky note. The snippets are clean and well-formatted (AI-style), but they're disconnected from each other - no clear sequence, no through-line. Between the snippets, lots of white space, suggesting absence rather than chaos. No person visible. A small "?" mark floats near the top right.

Chinese handwritten labels: '草稿呢?' in red at the top / '过程没了' in red near a small empty space between snippets / '?' in black
```

### 图 03 — 切回敲键盘 (confused, 切回手动)

**结构类型**:动作特写
**对应图**:`doc/essays/images/003-llm-code-control/03-typing-back.png`

```text
Theme: 切回手动敲键盘 - 工具站错位, 我切回来。

Core idea: Claude Code 放在"替你写"那个位置不对, 我自己回来写。

Composition: Xiaofan is sitting at a simple white desk, hands on a keyboard, looking at a monitor. The monitor shows a very simple editor with just 3-4 lines of code he just typed - rough, with a typo, not yet polished. Xiaofan's expression is confused (08-confused from variants) - he doesn't yet know what he's writing, just that he needs to write it himself. Beside the keyboard, a coffee cup (empty, forgotten). The scene conveys "I switched back to manual, even though I don't know what I'm doing yet." Slight mess on desk, not a curated workspace.

Input: xiaofan-ink/assets/ip-reference/standard.png (face), xiaofan-ink/assets/ip-reference/variants/08-confused.png (confused expression reference)

Chinese handwritten labels: '我自己写' in red on the screen / '不知道对不对' in blue below the code / '?' in red near the cup
```

### 图 04 — 站桌回看 (satisfied, 收束的释然)

**结构类型**:收束定格
**对应图**:`doc/essays/images/003-llm-code-control/04-looking-back.png`

```text
Theme: 站桌回看 - 关掉之后, 回到那个下午。

Core idea: 代码我可以重写, 失去对过程的掌控, 那种空, 我不知道怎么补。关掉之后, 有点爽。

Composition: Xiaofan is standing at his desk, looking back at the viewer (or off to the side), with a satisfied expression (11-satisfied from variants) - a small slight upturn of the lips, eyes half-closed, calm. The desk is half-empty: a few pieces of paper with his own handwriting (not code), an empty coffee cup, the closed laptop. The scene feels like "the work is over, I can rest now." The whole image conveys "back to the afternoon when I wrote code by hand, even though nothing came out of it."

Input: xiaofan-ink/assets/ip-reference/standard.png (face), xiaofan-ink/assets/ip-reference/variants/11-satisfied.png (satisfied expression reference)

Chinese handwritten labels: '回到那个下午' in red on a small label / '1 行代码' in blue near the laptop / '?' small in red near Xiaofan (slight uncertainty, not regret)
```

---

## 实战复盘(系列第 3 篇, 待生成后补)

待补。
