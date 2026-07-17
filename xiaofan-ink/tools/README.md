# xiaofan-ink tools — 公众号 API 自动化

> 本目录保存 xiaofan-ink 的工具脚本,跟 skill 内容解耦。
> 目前只有 `articles-to-wechat.py` — 把 `doc/essays/` 下的文章同步到微信公众号草稿箱。

## 文件

| 文件 | 用途 | git 跟踪? |
|------|------|-----------|
| `articles-to-wechat.py` | 主脚本:同步 essays 到公众号草稿 | ✅ |
| `config.example.json` | 配置模板 | ✅ |
| `config.json` | **本地凭证(包含 AppID/AppSecret)** | ❌ **gitignored** |
| `.token_cache.json` | access_token 缓存(2 小时过期) | ❌ **gitignored** |
| `README.md`(本文件) | 使用说明 | ✅ |

## 准备工作

### 1. 安装依赖

```bash
pip install requests pyyaml
```

### 2. 创建本地凭证文件

```bash
# 复制模板
cp config.example.json config.json

# 编辑 config.json,填入真实 AppID 和 AppSecret
# (凭证从 mp.weixin.qq.com → 开发 → 基本配置 → 公众号开发信息 获取)
```

> ⚠️ **重要**:`config.json` 包含真实凭证,已经在 `.gitignore` 中,不会进 git 仓库。
> 如果你不小心 commit 了,立刻在公众号后台"重置 AppSecret",旧的就失效了。

### 3. (可选)绑定白名单 IP

公众号后台 → 开发 → 基本配置 → 公众号开发信息 → IP 白名单。
把跑脚本的机器 IP 加进去(否则 access_token 拿不到)。

## 使用

### 列出所有 essays

```bash
python articles-to-wechat.py --list
```

输出示例:
```
📚 找到 2 篇 essays:

  [001] 001-why-i-dont-do-daily-plan.md
      为什么我不再做每日计划

  [002] 002-focus-boundary.md
      专注力的边界
```

### 测试 API 连接

```bash
python articles-to-wechat.py --test
```

输出示例:
```
🔗 测试 API 连接...
✅ access_token 获取成功
   前 10 字符: 38_K8gJ5xB...
```

### 同步单篇文章到草稿箱

```bash
python articles-to-wechat.py 001
```

完整流程:
1. 读 `doc/essays/001-why-i-dont-do-daily-plan.md`
2. 读配图目录 `doc/essays/images/001-why-i-dont-do-daily-plan/`
3. 获取 access_token(自动缓存 2 小时)
4. 上传所有配图到"图文消息内图片"API(获取微信 URL)
5. markdown → 微信公众号兼容 HTML(图片用微信 URL 替换)
6. 上传第一张图作封面(永久素材)
7. 创建草稿(draft/add)
8. 返回 draft_media_id

输出示例:
```
📄 读取 essay: 001-why-i-dont-do-daily-plan.md
🖼️  找到 4 张配图

🔑 获取 access_token...

📤 上传配图到图文消息内图片 API...
   上传 01-paper-sunk.png... ✅ https://mmbiz.qpic.cn/...
   上传 02-reaching-hole.png... ✅ ...
   上传 03-corner-squat.png... ✅ ...
   上传 04-desk-back.png... ✅ ...

🔄 markdown → HTML...

🖼️  上传封面...
   thumb_media_id: 38_K8gJ5xB...

📝 创建草稿...
✅ 草稿创建成功
   draft_media_id: 38_K8gJ5xB...

🎉 同步完成!
   📱 公众号后台 → 草稿箱 → 找到 [001] ... → 群发/定时发布
```

### 同步所有 essays(慎用)

```bash
python articles-to-wechat.py --all
```

会按顺序同步所有 00X 系列文章,每篇之间会**清空 access_token 缓存**。
**注意**:
- 个人订阅号每天只能群发 1 次 — 这个脚本只创建草稿,不会自动群发
- 草稿箱没数量限制,可以一次同步多篇
- 同步后,需要你手动到公众号后台点"群发"或"定时发布"

## 工作流(完整)

```
[1] 写文章 doc/essays/00X-<slug>.md(agent 托管或人工)
[2] 出图 doc/essays/images/00X-<slug>/ (agent 用 xiaofan-ink skill)
[3] 跑 python articles-to-wechat.py 00X
[4] 公众号后台 → 草稿箱 → 编辑/排版/选封面 → 群发/定时
[5] 同步到 doc/SERIES-STATE.md("已发布" 状态更新)
```

## 微信公众号类型与权限

| 类型 | 草稿箱 | 群发 | 自动回复 | 客服消息 |
|------|--------|------|----------|----------|
| 个人订阅号 | ✅ | 每天 1 次(高级群发要认证) | ✅ | 48 小时互动 |
| 认证订阅号 | ✅ | 每天多次 | ✅ | 48 小时互动 |
| 服务号 | ✅ | 每月 4 次(高级群发要认证) | ✅ | 48 小时互动 |

本号目前是**个人订阅号**,所以:
- ✅ 草稿箱可自由创建
- ✅ 自动回复可配置
- ⚠️ 群发每天 1 次,**不能脚本自动群发**(需要手动)
- ⚠️ 想自动群发需升级为认证订阅号

## 故障排查

### "找不到配置文件"

```
❌ 找不到配置文件: xiaofan-ink/tools/config.json
   请先复制 config.example.json → config.json 并填入真实凭证
```

解决:`cp config.example.json config.json` 然后编辑。

### "获取 access_token 失败: errcode": 40001 / 40013

- 40001: AppSecret 错误,去后台重置再填
- 40013: AppID 错误,检查 `wx` 开头有没有漏
- 40164: IP 不在白名单,去后台加白名单
- 45009: 调用次数超限(每分钟 2000 次,够用)

### "上传图片失败"

- 检查文件大小(单图 1MB / 2MB 限制)
- 检查文件格式(只支持 JPG/PNG)

### "创建草稿失败"

- 可能是 content HTML 里有微信不支持的标签
- 看错误返回的 errmsg,通常是 `content invalid` 或 `title invalid`

## 后续扩展(可选)

- `essay-to-multiple-platforms.py` — 同时推到知乎/小红书/Newsletter
- `cron-publish-daily.py` — 每天定时发布一篇草稿
- `analytics-dashboard.py` — 拉公众号阅读/在看数据
- `image-to-cdn.py` — 配图上传到自有 CDN(避免依赖微信临时 URL)

需要哪个跟我说,加进来。
