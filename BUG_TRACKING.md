# NewsforWenyan Bug记录与问题追踪

_最后更新: 2026-04-06_

---

## 📋 问题记录

### 2026-04-06 | GitHub Pages 404 问题

**问题类型**: 基础设施 / GitHub Pages
**严重程度**: 🔴 高
**状态**: ✅ 已修复

**问题描述**:
访问 `https://marvinchima723.github.io/NewsforWenyan/` 出现 404 File Not Found 错误。

**根本原因**:
GitHub Pages 需要根目录有 `index.html` 文件作为入口。之前只推送了日期命名的HTML文件（如 `NewsforWenyan_2026-04-06.html`），没有入口页面。

**解决方案**:
创建 `index.html` 作为入口页面，包含：
- 最新简报快速入口
- 历史简报列表
- GitHub仓库链接

**预防措施**:
- ✅ 每次创建新的日期HTML文件时，同步更新 `index.html` 的"历史简报"部分
- ✅ 确认GitHub Pages已启用（Settings → Pages → Source: main branch）

---

### 2026-04-06 | 无效新闻链接

**问题类型**: 内容质量 / 链接失效
**严重程度**: 🟡 中
**状态**: ✅ 已修复

**问题描述**:
部分新闻链接无法访问或内容为未来日期测试页。

**受影响的链接**:

| 原链接 | 问题 | 替换为 |
|--------|------|--------|
| `theborneopost.com/...` | 无法访问 | `english.news.cn/...` (Xinhua) |
| `humai.blog/...` | 未来日期测试页 | `renovateqr.com/blog/...` |

**解决方案**:
- 发布前验证所有链接（使用 web_fetch 工具）
- 优先使用权威来源：新华网、Xinhua、Reuters、Bloomberg
- 避免使用小众新闻站或个人博客

**预防措施**:
- ✅ 发布前验证所有外部链接
- ✅ 优先使用主流媒体来源
- ✅ 记录已验证的可靠来源到 `news_sources_urls.md`

---

### 2026-04-05 | Git 推送冲突

**问题类型**: Git / 版本控制
**严重程度**: 🟡 中
**状态**: ✅ 已记录

**问题描述**:
多人/多设备操作导致 git push 失败，需要 force push 或 rebase。

**预防措施**:
- 每次推送前先 `git pull origin main --rebase`
- 如遇冲突，使用 `git stash` → `git pull` → `git stash pop`
- 不轻易使用 `git push --force`，优先解决冲突

---

## 🔧 自动化任务检查清单

每次生成新闻后，确认以下步骤：

- [ ] 生成当日 HTML 文件（例：`NewsforWenyan_YYYY-MM-DD.html`）
- [ ] 验证所有外部链接可访问
- [ ] 更新 `index.html` 的历史简报列表
- [ ] 更新 `news_sources_urls.md` 记录当日 URL
- [ ] `git add` → `git commit` → `git push origin main`
- [ ] 发送邮件 `python3 send_email.py YYYY-MM-DD`
- [ ] 在浏览器验证 GitHub Pages 显示正常

---

## 📝 已知问题 / 待优化

- [ ] 邮件发送需要VPN或手机热点（Gmail SMTP在中国被封锁）
- [ ] 历史简报积累后，index.html 的存档列表会变长，需要考虑分页或搜索功能
- [ ] 自动化任务（每天7点）当前为 PAUSED 状态，需要手动触发

---

## 🏷️ 来源可靠性分级

### ✅ 推荐来源（已验证有效）

| 来源 | 适用分类 | 备注 |
|------|---------|------|
| Xinhua (english.news.cn) | 亚太、中国 | 权威、可访问 |
| CNN | 地缘政治 | 实时新闻 |
| Reuters | 全球经济 | 权威 |
| Bloomberg | 金融、市场 | 需要VPN |
| Zawya | 穆巴达拉 | 阿联酋官方投资平台 |
| AGBI | 穆巴达拉、全球 | 权威财经媒体 |

### ⚠️ 谨慎使用

| 来源 | 问题 | 替代 |
|------|------|------|
| Borneo Post | 偶尔无法访问 | Xinhua |
| 小众博客 | 未来日期测试页 | RenovateQR / 主流媒体 |
| 各类新闻汇总站 | 链接稳定性差 | 直接用原始来源 |

### ❌ 避免使用

| 来源 | 原因 |
|------|------|
| 未验证的小众站点 | 链接易失效 |
| 需要登录的付费内容 | 读者无法访问 |

---

_此文档随每次问题发现而更新，用于积累经验和预防重复问题。_
