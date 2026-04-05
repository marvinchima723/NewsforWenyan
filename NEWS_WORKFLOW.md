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
- ⚠️ 更新 HTML 后同步更新 `news_sources_urls.md`