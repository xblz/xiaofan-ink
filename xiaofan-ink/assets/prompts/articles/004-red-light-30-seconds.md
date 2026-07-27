# 实战 8 — 等红灯 30 秒(系列第 4 篇, v2.0 生活小事角度池开篇)

> 文章:`doc/essays/004-red-light-30-seconds.md`
> 系列:《小凡墨水周记》第 4 篇
> 生成日期:2026-07-27 / 主题:生活小事 — 过程 > 结论 / 配图数:4(1 cover + 3 正文)
> 输入参考图:`xiaofan-ink/assets/ip-reference/standard.png`(有 IP 的图都引用)
> 表情分布:1 default + 1 thoughtful + 1 satisfied(3 种, 3 张正文)
> 装扮:0/3 用(全部不拿道具, 强调"我 vs 信息" 的关系)
> 姿态:3 different(站等红灯 / 站发愣 / 走过路口)
> v1.8 IP 决策:动作型(站/站/走)→ 保留 IP 3 张; 状态型(路口 + 留白)→ 去 IP 1 张(cover)

---

## 主题选择记录(agent 自主决定 + 用户参与)

004 主题"等红灯 30 秒" 由 **用户从候选池中选** —— 这跟 v1.3 "主题由 agent 自主决定" 规则配合:agent 提候选, 用户挑。

### 候选池生成(7 个, 全部暗合核心三句话之一)

- 超市试吃装的不是样品, 是剧本(草稿 > 作品)
- **等红灯 30 秒, 我以为我需要信息, 其实我需要 30 秒(过程 > 结论)** ← 用户选
- 出门忘带钥匙, 10 年仪式 1 次破功(过程 > 结论)
- 微信撤回消息, 撤回不是修改, 是暴露(草稿 > 作品)
- PPT 改 5 版, 改稿改的是起点的灵气(过程 > 结论)
- 便利店饭团, 最顺手的不是最对的(过程 > 结论)
- 开会打哈欠传染, 其实是厌倦传染(过程 > 结论)
- 退订公众号, 关注不是喜欢, 是不敢说不(草稿 > 作品)

### 选 #2 的理由

- 切口最普世(任何有手机的人都经历过)
- 跟"过程 > 结论" 直接对应:掏出手机 = 拿结论, 30 秒发呆 = 拿过程
- 跟 000 "草稿 > 作品" 形成二阶呼应(30 秒里浮现的是"自己的草稿", 刷到的是"别人的作品")
- 跟"卖萌"距离最远(纯反思, 没有任何温情感)

### 不立 flag

#7(打哈欠传染) 也已敲定, **等用户触发信号再写**, 不主动开。跟"想写就写"调性自洽。

## v1.8 IP 决策应用

| 图 | 动作/状态 | 决策 | 理由 |
|---|---|---|---|
| cover (00) | 状态: 路口 + 红灯 + 没人 | 去 IP | 城市路口 + 红灯 + 留白 + 远处小凡影子(隐约), 让读者凝视 |
| 01 站等红灯 | 动作: 站 + 拿手机但没看 | 保留 IP | 关键动作: 掏到一半停住, IP 体现"那一瞬间的犹豫" |
| 02 站发愣 | 动作: 站 + 表情 thoughtful | 保留 IP | 30 秒里想事情, 表情需要细的"思考" |
| 03 走过路口 | 动作: 走 + 满足平静 | 保留 IP | 收束的释然, "30 秒够长" |

## 表情选型决策

| 图 | 表情 | 选词理由 |
|---|---|---|
| 01 站等红灯 | deadpan | "掏到一半停住" 是平静动作, deadpan 完美 |
| 02 站发愣 | **思考**(07-thoughtful) | "30 秒里想 3 周前发的那段话", 真思考 |
| 03 走过路口 | **满足**(11-satisfied) | 收束的释然, "30 秒够长" |

情绪节奏:平 → 思考 → 满足
表情种类:3 种(deadpan 1 + 思考 1 + 满足 1)✓ 符合 SERIES-STATE "最多 2-3 种"

## 姿态轮换

3 张图全部为新姿态(实战 1-3 + 系列 001/002/003 没用过):
- 01: 站 + 拿手机但没看(新, 跟 002 站+看钟不同)
- 02: 站 + 发愣(新, 跟 002 站+看空桌不同)
- 03: 走(新)

## 物件轮换

新物件池:路口 / 红灯 / 手机(没看) / 远处行人 / 树 / 朋友的对话框
注意:咖啡杯系列 001/002/003 多次用, 004 故意 0/3 用, 强调"我 vs 信息" 的人物关系, 不需要道具干扰
手机是新物件(实战 1-3 + 001/002/003 都没用过), 但不是"小凡的装扮", 是"环境里没看的物件"

---

## 4 张图的完整 prompt

### 图 cover (00) — 路口 + 红灯 + 没人掏手机 (去 IP)

**结构类型**:状态刻画
**对应图**:`doc/essays/images/004-red-light-30-seconds/00-red-light.png`

```text
Theme: 路口 + 红灯 + 没人 - 等红灯的 30 秒, 大家都不掏手机。

Core idea: 一个普通城市十字路口, 红灯亮, 几辆车停下, 没人掏手机(罕见)。远处隐约一个小凡的背影, 但不仔细看看不出。整张图传达"这 30 秒, 没人刷"。

Composition: Top-down or slightly elevated view of a simple crossroad intersection. Red traffic light visible. A few cars stopped at the line. A small figure (Xiaofan) seen from behind, at the very back, but blurred / sketchy. No phones visible in anyone's hands. Lots of white space around the intersection. The whole image conveys "30 seconds, no scrolling."

Chinese handwritten labels: '30 秒' in red floating above / '没人刷' in red on a small label / '?' in red on the crossroad
```

### 图 01 — 站等红灯 (deadpan, 掏到一半停住)

**结构类型**:动作特写
**对应图**:`doc/essays/images/004-red-light-30-seconds/01-standing.png`

```text
Theme: 站等红灯, 手机掏到一半停住 - 那一瞬间的犹豫。

Core idea: 习惯伸手掏手机, 但 30 秒够长, 这次不掏。deadpan 表情体现"那一秒的停顿"。

Composition: Xiaofan is standing at a crossroad, one hand halfway reaching into his pocket / holding a phone that is in his pocket / just pulled out, NOT looking at it. The phone is half-visible but his eyes are looking forward at the red light. Deadpan calm expression, no urgency. The red light is visible in the distance. Other people / cars are also stopped, but Xiaofan is centered. The scene conveys "the moment of stopping the habitual action."

Input: xiaofan-ink/assets/ip-reference/standard.png (Xiaofan's face for consistency)

Chinese handwritten labels: '掏到一半' in red on his hand / '30 秒' in blue above the red light / '不看' in red on the phone (small)
```

### 图 02 — 站发愣 (thoughtful, 30 秒里想事情)

**结构类型**:角色状态
**对应图**:`doc/essays/images/004-red-light-30-seconds/02-lights-green.png`

```text
Theme: 站发愣 - 30 秒里, 灯变绿了, 后面车按喇叭, 我还在想。

Core idea: 那 30 秒里, 我想的不是路口有什么, 是 3 周前发的那段话。灯变绿了, 我没反应过来。

Composition: Xiaofan is standing at the same crossroad. The traffic light is now GREEN. Cars behind him are honking (represented by 3 small "哔" symbols floating). Xiaofan's expression is thoughtful (07-thoughtful from variants) - slightly furrowed brow, eyes looking at something that isn't there, mouth slightly closed but not in a frown. His hand is still at his side, not holding the phone. He's "still there" mentally. The scene conveys "I'm not here yet, the light is green but my mind is still on that 3-week-old message."

Input: xiaofan-ink/assets/ip-reference/standard.png (face), xiaofan-ink/assets/ip-reference/variants/07-thoughtful.png (thoughtful expression reference)

Chinese handwritten labels: '灯绿了' in green above the light / '哔' in red floating 3 times (small) / '?' in red near Xiaofan / '3 周前' in blue below (a small text floating)
```

### 图 03 — 走过路口 (satisfied, 收束的释然)

**结构类型**:收束定格
**对应图**:`doc/essays/images/004-red-light-30-seconds/03-crossed.png`

```text
Theme: 走过路口 - 那 30 秒, 我跟自己说了一句话。

Core idea: 30 秒够长, 够我听见自己的草稿。走过路口那一刻, 表情满足, 不是开心, 是平静。

Composition: Xiaofan is walking across the crossroad, halfway through, looking forward. His expression is satisfied (11-satisfied from variants) - small slight upturn of the lips, eyes half-closed, calm. The traffic light is now red for the cross-direction. His hands are at his sides, no phone. The scene conveys "30 seconds was long enough. I just said something to myself." Slight slow walk, not rushing.

Input: xiaofan-ink/assets/ip-reference/standard.png (face), xiaofan-ink/assets/ip-reference/variants/11-satisfied.png (satisfied expression reference)

Chinese handwritten labels: '30 秒够长' in red on a small label / '自己的草稿' in blue below (a small text floating) / '没掏' in red small near his hand
```

---

## 实战复盘(系列第 4 篇, 待生成后补)

待补。
