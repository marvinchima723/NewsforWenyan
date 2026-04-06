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