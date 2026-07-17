# 实战 4 — 为什么我不再做每日计划(系列首发)

> 文章:`doc/essays/001-why-i-dont-do-daily-plan.md`
> 系列:《小凡墨水周记》第 1 篇
> 生成日期:2026-07-17 / 主题:工具反思 — 节奏类 / 配图数:4
> 输入参考图:`xiaofan-ink/assets/ip-reference/standard.png`
> 表情分布:2 默认 + 1 困惑 + 1 满足
> 装扮:1/4 用(咖啡杯)
> 姿态:4 种(卡在纸堆 / 洞里伸手 / 蹲角落 / 回头看)

---

## 表情选型决策

| 图 | 表情 | 选词理由 |
|---|---|---|
| 01 纸堆 | deadpan | 入口段"计划填满了但人空了",陈述事实,deadpan 合适 |
| 02 洞里伸手 | **困惑**(08-confused) | "列计划花的时间比做的事还多",困惑表情传递"没想清楚" |
| 03 蹲角落 | **疲惫**(09-tired) | "做完才看清",做完的累,疲惫表情到位 |
| 04 站回头 | **满足**(11-satisfied) | 收束段"放弃计划反而做得更多",满足收尾 |

情绪节奏:平 → 困惑 → 疲惫 → 满足(完整呼吸,跟实战 3 的"平 → 思考 → 疲惫 → 平" 不同 — 这次收尾用满足,因为主题是"做完"的满足感)

## 姿态轮换

4 张图全部用实战 1-3 没出现过的姿态,严格执行 SERIES-STATE 防反复刻规则:
- 01: 半个身子卡在纸堆里(新)
- 02: 从洞里伸手接不住(新)
- 03: 蹲在角落画外看(新)
- 04: 站但回头看画外(新)

## 装扮轮换

- 03: 桌上有咖啡杯(但小凡没拿,只是画外物件,不算"装扮")
- 04: 小凡手握咖啡杯(明确用 05-coffee.png 变体,1/4 用)

实战 2 用了 3/4 装扮,实战 3 用了 0/4 装扮,本次 1/4,符合"不极端"原则。

## 物件轮换

本次用了"纸堆"和"洞"两个隐喻,实战 1-3 没出现过,池子更新。

## 4 张图的完整 prompt

### 图 01 — 计划填满了纸(deadpan, 半个身子卡纸堆)

**结构类型**:概念隐喻
**对应图**:`doc/essays/images/001-why-i-dont-do-daily-plan/01-paper-sunk.png`

```text
Generate a 16:9 horizontal Chinese article illustration on pure white background. Style: casual hand-drawn line illustration. Xiaofan is a loose line-drawn self-portrait with recognizable features. The face must look like the same Xiaofan as the reference. Xiaofan must perform the core conceptual action, not decorate the scene. He is the main action subject. Lots of white space. Do not draw a title in the corner. No PPT, no flowchart, no commercial vector style, no realistic photo elements.

Theme: 计划填满了纸但没填满人 - 列了一堆每日计划,真正做的事反而更少。

Structure type: 概念隐喻

Core idea: 计划列得越细,真正在做事的时间反而越少 - 计划填满了纸,但人空了。

Composition: A tall messy pile of paper sheets, all written on with handwritten lists and crossed-out items, taking up most of the canvas. Xiaofan is half-sunk INTO the paper pile, only his head and one hand visible above the pile, his other hand holding a pencil that just finished writing something. He looks out with a deadpan calm expression, as if the pile of plans has swallowed him. The papers around him are various sizes and slightly chaotic. Xiaofan (a young Asian man with short messy black bangs covering forehead, narrow single-eyelid eyes, thin lips, deadpan calm expression, hand-drawn line art) half-sunk in a paper pile.

Chinese handwritten labels: '今日 8 件事' in orange on a top sheet / '划掉' in red on multiple sheets / '没做' in blue on a remaining sheet

Constraints: ...
```

### 图 02 — 计划的反噬(困惑, 洞里伸手)

**结构类型**:角色状态
**对应图**:`doc/essays/images/001-why-i-dont-do-daily-plan/02-reaching-hole.png`

```text
Theme: 计划的反噬 - 列计划花的时间比实际做的事还多。

Structure type: 角色状态

Core idea: 划掉的越多,空的就越多 - 计划给你虚假完成感。

Composition: A small scene like a paper rain. Sheets of paper with handwritten lists are falling from above like rain, scattered around. Xiaofan is reaching his hand UP from a hole/circular opening in the ground, trying to catch a falling sheet but his hand is just missing it. His face shows slightly furrowed brows, eyes half-closed, mouth slightly relaxed - a confused expression. Only his upper body and reaching hand are visible. Xiaofan (a young Asian man with short messy black bangs covering forehead, narrow single-eyelid eyes, thin lips, slightly furrowed brows, eyes half-closed, mouth slightly relaxed, hand-drawn line art) reaching up from a hole.

Chinese handwritten labels: '?' in red near his hand / '想做' in blue on a falling sheet / '没做' in red on another / '划掉' in red on a third

Constraints: ...
```

### 图 03 — 做完才看清(疲惫, 蹲角落)

**结构类型**:概念隐喻
**对应图**:`doc/essays/images/001-why-i-dont-do-daily-plan/03-corner-squat.png`

```text
Theme: 做完才看清 - 不做计划,只做"今天这 3 件事"。

Structure type: 概念隐喻

Core idea: 做完才知道对不对,不对就调整 - 不追求管理所有事,只追求今天做这 3 件。

Composition: Xiaofan is squatting in a corner of the canvas, looking OFF-CANVAS to the right with a tired expression. In the lower-right of the canvas, a desk with a stack of messy draft papers (representing "things actually done"). His drooping brows and half-closed eyes convey exhaustion from doing the work. A small coffee cup on the desk (he has been at it for a while). Xiaofan (a young Asian man with short messy black bangs covering forehead, narrow single-eyelid eyes, thin lips, drooping brows, eyes half-closed, mouth loose, hand-drawn line art) squatting in a corner looking off-canvas tired.

Chinese handwritten labels: '做完才看清' in orange / '3 件事' in blue / '调整' in orange near him

Constraints: ...
```

### 图 04 — 现在的桌面(满足, 站回头 + 咖啡杯)

**结构类型**:概念隐喻 + 收束
**对应图**:`doc/essays/images/001-why-i-dont-do-daily-plan/04-desk-back.png`

```text
Theme: 现在的桌面 - 不做计划,反而做得更多。

Structure type: 概念隐喻 + 收束

Core idea: 计划没让我多做一件事。放弃计划,我反而做得更多。

Composition: Xiaofan is standing at a small simple desk, looking back over his shoulder toward the viewer's outside. On the desk: 3 handwritten papers labeled (3 things done), 1 red-bordered paper labeled "not doing today" list, and a half-drunk coffee cup (he is holding it). His face has a slight 1-2mm mouth upturn, half-closed eyes, level brows - a quiet satisfaction. He is not facing the desk; he is looking back, as if to say "the work is done, no need to plan more." Xiaofan (a young Asian man with short messy black bangs covering forehead, narrow single-eyelid eyes, thin lips, slight 1-2mm mouth upturn, half-closed eyes, level brows, hand-drawn line art) standing at a desk looking back, holding a coffee cup.

Chinese handwritten labels: '3 件做完' in blue on three sheets / '不做' in red on the red-bordered paper / '放弃计划' in orange / '半杯' near the coffee cup

Constraints: ...
```

---

## 实战复盘(系列首发)

### 优点

- 4 张图全部一次过,无重出
- 表情差异肉眼可辨(deadpan / 困惑 / 疲惫 / 满足)
- 4 种姿态全部用实战 1-3 没出现过的,严格执行防反复刻
- 物件创新:纸堆 + 洞(实战 1-3 没用过的隐喻池)
- 情绪节奏完整:平 → 困惑 → 疲惫 → 满足(收尾用满足,跟实战 3 的"平收"不同)

### 不足

- **图 04 满足表情不够明显**:嘴角上扬 1-2mm 在图中几乎看不出,看起来还是 deadpan。改进方向:prompt 里 "slight 1-2mm mouth upturn" 改成 "slight 3-4mm mouth upturn" 或加 "almost-smile",模型可能更能捕捉
- **图 02 伸手方向跟脸朝向不协调**:手往左伸但脸朝右看,看起来"身体跟脸不连戏"。改进方向:prompt 里把 "trying to catch a falling sheet" 改成 "looking up confused, papers falling around",去掉"接"的意图
- **图 03 桌子画得太满**:有点挤压小凡,留白不够。改进方向:把"desk"换成更小的"tray"或"几个 paper 直接地上"

### 改进 takeaway(给下一篇用)

- 收尾用满足时,prompt 措辞要更明显("almost-smile" / "subtle smile" / "mouth upturn" 都不够,"slight smile" 配合 "eyes slightly squinted" 更有效)
- "试图接" + "困惑"组合容易让 body 跟 face 不连戏,要么统一方向,要么去掉意图描述
- 桌面/桌子的"满"会挤压小凡,小物件(杯/瓶/小盒)效果更好

### 系列首发观察

- 实战 1-3 是 skill 验证样本,这次是正式系列首发,差别在:
  - 文件路径:`doc/images/<slug>/` → `doc/essays/images/001-<slug>/`
  - 命名:`01.png` → `01-paper-sunk.png`(带描述)
  - front matter:实战样本没有,系列每篇加 YAML
- 整体流程跑通,后续每周三按相同流程复制即可
