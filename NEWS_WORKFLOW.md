# News for Wenyan - 生成工作流

## 每次生成新闻的标准流程

### 1. 搜集新闻 (Web Search)
- 使用 Web Search 搜索每个新闻主题
- **每次搜索时，记录搜索到的原文URL**
- 优先使用权威来源：Reuters, FT, Bloomberg, CNBC, Nikkei, NBS 等

### 2. 追踪来源 URL
- 将每条新闻的原文链接记录到 `news_sources_urls.md`
- 格式：`| 分类 | 标题 | URL | 来源 |`
- 即使是同一天的新闻，也要更新这个文件

### 3. 生成 HTML
- 每个 `.news-card` 都需要包含可点击的原文链接
- 卡片内的 `<a>` 标签包裹标题和描述
- 底部来源行也需要是 `<a>` 链接，格式：`来源名 · 日期 ↗`

### 4. HTML 链接格式示例
```html
<article class="news-card">
    <div class="news-meta">...</div>
    <a href="[原文URL]" target="_blank" style="text-decoration:none;color:inherit;">
        <h3 class="news-title">[新闻标题]</h3>
        <p class="news-desc">[新闻描述]</p>
    </a>
    <p class="news-source">
        <a href="[原文URL]" target="_blank" style="color:var(--text-tertiary);">
            [来源] · [日期] ↗
        </a>
    </p>
</article>
```

## 新闻分类

每次生成以下6个分类的新闻：

1. **⚔️ 地缘政治** — 中东、美中关系、全球冲突
2. **📊 全球经济** — 宏观政策、IMF/世界银行报告、全球市场
3. **🌏 亚太动态** — 日本、韩国、印度、中国重要经济动态
4. **💻 科技** — AI、科技行业、芯片
5. **🏦 主权基金** — 海湾主权基金（穆巴达拉、ADIA等）投资动态
6. **🏦 穆巴达拉专栏** — 穆巴达拉投资亚太/中国/亚洲科技/AI/数字基础设施的专门新闻（**每日必选**）

### 穆巴达拉专栏说明
- **标签颜色**：`tag-mubadala`（金色/琥珀色主题，区别于其他分类）
- **搜索关键词**：`Mubadala Asia investment`, `Mubadala China`, `Mubadala India`, `Mubadala technology AI`, `Mubadala digital infrastructure`
- **放置位置**：在"今日要闻"之后，独立成一个新的 `section`
- **来源优先级**：穆巴达拉官网 > Zawya > Khaleej Times > AGBI > Bloomberg

## URL 追踪文件
- **路径**: `/Users/mma/Dropbox/0-行研专家/NewsforWenyan/news_sources_urls.md`
- 每次生成新闻后必须更新
- 包含：日期、标题、原文链接、来源

## 来源优先级
1. Reuters / Bloomberg / FT / CNBC（国际权威）
2. NBS / Global Times / Xinhua（官方来源）
3. Nikkei / Trading Economics / 其他专业媒体

## 注意事项
- ⚠️ 每条新闻必须有原始链接，禁止只标注来源名称
- ⚠️ 链接必须是可直接访问的 URL，不能是付费墙后的页面

### 穆巴达拉专栏 HTML 示例
```html
<!-- 穆巴达拉专栏 -->
<section class="news-section">
    <h2 style="border-left-color: #FF9F0A;">🏦 穆巴达拉投资动态</h2>
    <div class="news-grid">
        <article class="news-card">
            <div class="news-meta">
                <span class="news-tag tag-mubadala">🏦 穆巴达拉</span>
                <span class="tag-region">🌏 亚洲</span>
            </div>
            <a href="[原文URL]" target="_blank" style="text-decoration:none;color:inherit;">
                <h3 class="news-title">[新闻标题]</h3>
                <p class="news-desc">[新闻描述]</p>
            </a>
            <p class="news-source">
                <a href="[原文URL]" target="_blank" style="color:var(--text-tertiary);">[来源] · [日期] ↗</a>
            </p>
        </article>
    </div>
</section>
```

### CSS 样式（需添加到 HTML 的 `<style>` 中）
```css
.tag-mubadala { background: rgba(255,159,10,0.2); color: #FF9F0A; }
```

> ⚠️ 更新 HTML 后同步更新 `news_sources_urls.md`

---

## ⚠️ 发布检查清单（必读）

每次生成新闻或深度专题后，必须逐项确认：

### 链接验证
- [ ] 所有外部链接已用 web_fetch 验证有效
- [ ] 无未来日期的测试页（检查链接中的日期）
- [ ] 优先使用权威来源（Xinhua > Borneo Post）

### GitHub Pages 同步（强制）
- [ ] 新HTML文件已 git add → commit → push
- [ ] `index.html` 已更新（添加新的历史简报入口或深度专刊入口）
- [ ] **⚠️ 验证推送结果（必须）：用 web_fetch 访问生成的URL，确认返回正常页面而非404**
- [ ] 如返回404 → 进入Debug循环，继续修复直到验证通过

### 邮件
- [ ] 邮件发送成功（注意：需要VPN或手机热点）
- [ ] 收件人：yoyozwy@gmail.com, marvin.cmma@gmail.com

### 文档
- [ ] `news_sources_urls.md` 已更新当日URL（如是每日简报）
- [ ] 如有新问题，记录到 `BUG_TRACKING.md`

---

## 🔄 GitHub推送验证循环（强制执行）

**每次推送后必须验证，验证失败必须Debug直到成功：**

```
推送 → 验证URL → 404? → 检查git状态 → 重新推送 → 再次验证 → 直到通过
```

### 第一步：推送
```bash
git add <文件> && git commit -m "描述" && git push
```

### 第二步：验证（推送后立即执行）
用 web_fetch 访问生成的URL，例如：
```
https://marvinchima723.github.io/NewsforWenyan/Hormuz_Crisis_Report_v3_2026-04-06.html
```

### 第三步：如遇404，进入Debug循环
1. 检查 `git status` — 确认文件是否在tracked列表
2. 确认 `git log` — 确认commit是否存在
3. 如是网络问题（HTTP2 framing layer / 连接超时）→ 需要VPN
4. 重试推送，等待2-3秒后再次验证URL
5. **持续循环直到验证通过，不轻易放弃**

### 第四步：验证通过后
- 继续下一步（发送邮件等）

### 网络问题处理
| 错误信息 | 原因 | 解决 |
|---------|------|------|
| `HTTP2 framing layer error` | 中国网络与GitHub不兼容 | 需要VPN |
| `Failed to connect to github.com port 443` | 防火墙封锁 | 需要VPN |
| `Could not resolve host` | DNS污染 | 尝试 `8.8.8.8` DNS或VPN |
| `connection reset` | 连接被重置 | VPN + 重试 |
| `anonymous base` | Git认证失效 | 检查token是否有效 |

---

## 🐛 常见问题与解决方案

| 问题 | 原因 | 解决 |
|------|------|------|
| GitHub Pages 404 | 文件未同步到仓库 | 确认git push成功，验证URL |
| 链接无法访问 | 来源网站不稳定 | 换用Xinhua/Reuters等权威源 |
| 邮件发送失败 | Gmail SMTP被封锁 | 启用VPN或手机热点 |
| git push失败 | 远程有更新或网络问题 | git pull --rebase 后再push；或VPN重试 |
| 404但git显示已推送 | 浏览器缓存 | 硬刷新 Ctrl+Shift+R |
| 404但git显示已推送 | GitHub Pages未更新 | 等待1-2分钟后再试 |

---

_此文档随每次问题发现而更新，确保工作流程持续改进。_
