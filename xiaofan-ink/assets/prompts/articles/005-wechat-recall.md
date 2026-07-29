# 实战 9 — 微信撤回消息, 撤回不是修改, 是暴露(系列第 5 篇, v2.0 生活小事角度池)

> 文章:`doc/essays/005-wechat-recall.md`
> 系列:《小凡墨水周记》第 5 篇
> 生成日期:2026-07-29 / 主题:生活小事 — 草稿 > 作品 / 配图数:4(1 cover + 3 正文)
> 输入参考图:`xiaofan-ink/assets/ip-reference/standard.png`(有 IP 的图都引用)
> 表情分布:1 default + 1 thoughtful + 1 default(2 种, 3 张 IP 正文)
> 装扮:0/3 用(全部不拿道具, 强调"我 vs 撤回" 的关系)
> 姿态:3 different(看手机 / 想 / 放下手机)
> v1.8 IP 决策:动作型(看/想/放)→ 保留 IP 3 张; 状态型(微信对话时间轴)→ 去 IP 1 张(cover)

---

## 主题选择记录

005 主题"微信撤回消息" 由 **用户从候选池触发** —— 候选 4 在 v2.0 创建时已锁定, 这次用户主动说要写。

### 选 #4 的理由

- 切口普世(任何用微信的人都做过撤回 + 见过撤回)
- 跟"草稿 > 作品" 直接对应:撤回是想把"草稿的我" 改"作品的我", 但撤回本身暴露了"草稿的我"
- 跟 000 "草稿 > 作品" 形成二阶呼应(000 说"草稿更诚实", 005 演示"为什么撤回破坏诚实")
- 跟"卖萌"距离最远(略带批判, 反思工具对人际关系的影响)
- 跟 004 形成"小事" 系列第二篇(004 过程 > 结论, 005 草稿 > 作品)

## v1.8 IP 决策应用

| 图 | 动作/状态 | 决策 | 理由 |
|---|---|---|---|
| cover (00) | 状态: 手机屏幕 + 撤回提示 | 去 IP | 纯物件 + 留白, 让读者凝视那个"灰字" |
| 01 看手机 | 动作: 看撤回提示 | 保留 IP | 关键动作, IP 体现"看到" 那一下 |
| 02 时间轴 | 状态: 微信对话 + 撤回灰字 | 去 IP | 状态型, 时间轴 + 草稿/撤回对比 |
| 03 想 | 动作: 想那条消息是啥 | 保留 IP | 收束的"想", IP 体现"那个草稿的我" |

## 表情选型决策

| 图 | 表情 | 选词理由 |
|---|---|---|
| 01 看手机 | deadpan | "看到了" 是平静反应, deadpan 合适 |
| 02 时间轴 | (去 IP, 无表情) | 状态型不需要人 |
| 03 想 | **思考**(07-thoughtful) | "撤回是想让我没看到, 但我看到了" 真思考 |

情绪节奏:平 → (无) → 思考 → 平(段 4 收束)
表情种类:2 种(deadpan 1 + 思考 1)✓ 符合 SERIES-STATE "最多 2-3 种"
(注: 收束段 03 deadpan 不算"另一种", 跟 01 同 deadpan)

## 姿态轮换

3 张图全部为新姿态(实战 1-3 + 系列 001/002/003/004 没用过):
- 01: 拿手机看(新, 跟 004 站等红灯不同)
- 03: 拿手机想(新, 跟 002 站+看空桌不同)

## 物件轮换

新物件池:手机(大屏特写) / 微信对话框 / "X 撤回了一条消息" 灰字 / 撤回 2 分钟倒计时
注意:手机是 004 出现过的物件, 但 004 是"路口 + 手机(没看)", 005 是"手机 + 撤回提示", 物件场景不同, 算"新用"

---

## 4 张图的完整 prompt

### 图 cover (00) — 手机屏幕 + 撤回提示 (去 IP)

**结构类型**:状态刻画
**对应图**:`doc/essays/images/005-wechat-recall/00-recall-prompt.png`

```text
Theme: 手机屏幕 + 撤回提示 - 微信聊天里那条灰字"X 撤回了一条消息"。

Core idea: 撤回不是删除, 是"留一条缝"。那条灰字就是缝。

Composition: A simple WeChat-style chat interface on a white phone screen. At the top, a few normal message bubbles. In the middle, a single grey line of text saying "X 撤回了一条消息" (X recalled a message). Below, lots of white space. No person visible. The whole image conveys "the recall is gone, but the gray line of 'someone recalled' is still there."

Chinese handwritten labels: 'X 撤回了一条消息' in red on the gray line (highlighted) / '2 分钟内' in red small at the corner / '?' in red floating small
```

### 图 01 — 看手机 (deadpan, 看到撤回提示)

**结构类型**:动作特写
**对应图**:`doc/essays/images/005-wechat-recall/01-saw-recall.png`

```text
Theme: 看手机, 看到撤回提示 - 朋友撤回了, 我看到了。

Core idea: 撤回是 2 分钟内反悔, 但反悔这件事所有人都看见。我看见了。

Composition: Xiaofan is sitting somewhere (no clear background, just white space), holding a phone with both hands, looking at the screen. On the phone screen, visible, is a WeChat-style chat with a grey line "X 撤回了一条消息". Xiaofan's expression is deadpan calm - he sees it, but doesn't react strongly. His body language is still, not shocked. The scene conveys "I saw it, I know you recalled, but I'm not going to make a big deal of it."

Input: xiaofan-ink/assets/ip-reference/standard.png (Xiaofan's face for consistency)

Chinese handwritten labels: '看见了' in red small near his face / '?' in red on the phone / '2 分钟' in orange small
```

### 图 02 — 时间轴 (去 IP)

**结构类型**:对比结构
**对应图**:`doc/essays/images/005-wechat-recall/02-timeline.png`

```text
Theme: 微信时间轴: 草稿 → 撤回 - 撤回把"草稿的我" 抹掉了。

Core idea: 撤回不是修改, 是删除。删除前有"草稿的我", 删除后只剩"撤回提示"。

Composition: A horizontal timeline with 3 nodes. Left node: a normal message bubble in light grey (the original "draft" message that was sent). Middle: an arrow with a small clock icon and "2 min" label. Right node: a grey line saying "X 撤回了一条消息" - the draft is gone, only the recall line remains. Lots of white space. The whole image shows "the draft was here, the recall replaced it, but you only see 'recalled', not 'what was recalled'." Two red arrows showing "草稿 → 撤回" and "暴露" labels.

Chinese handwritten labels: '草稿' in blue at left node / '撤回' in red at right node / '暴露' in red on the middle arrow / '?' small in red at right
```

### 图 03 — 想 (thoughtful, 想那条消息是啥)

**结构类型**:角色状态
**对应图**:`doc/essays/images/005-wechat-recall/03-thinking.png`

```text
Theme: 想那条消息是啥 - 撤回是想让我没看到, 但我看到了。

Core idea: 撤回的人不想让你看到, 但你看到"撤回" 本身, 已经在想"那是啥"。

Composition: Xiaofan is holding his phone, but now his eyes are looking up and to the side, not at the screen. He's thinking about what the recalled message could have been. His expression is thoughtful (07-thoughtful from variants) - slightly furrowed brow, eyes distant, mouth slightly closed. The phone is in his hand but the screen is dim. The scene conveys "I don't even need to look at the phone. I'm thinking about what you said and then recalled."

Input: xiaofan-ink/assets/ip-reference/standard.png (face), xiaofan-ink/assets/ip-reference/variants/07-thoughtful.png (thoughtful expression reference)

Chinese handwritten labels: '那是啥' in red floating near his head / '?' in red small / '草稿的我' in blue below the phone (small)
```

---

## 实战复盘(系列第 5 篇, 待生成后补)

待补。
