# NewsforWenyan Bug记录与问题追踪

_最后更新: 2026-04-12_

---

## 📋 问题记录

### 2026-04-08 | 市场数据错误

**问题类型**: 内容质量 / 数据准确性
**严重程度**: 🔴 高
**状态**: ✅ HTML已修正（待Git推送）

**错误数据 vs 正确数据**：

| 数据项 | 错误值 | 正确值 | 来源 |
|--------|--------|--------|------|
| 恒生指数 | 22,800 / -2.1% | 25,877 / +3.03% | Trading Economics |
| 印度Sensex | 72,450 / -0.4% | 77,605 / +4.00% | LiveMint |
| USD/CNY | 7.25 | 6.83 | exchangerate.guru |

**修正位置**：
- `/Users/mma/Dropbox/0-行研专家/NewsforWenyan/news/NewsforWenyan_2026-04-08.html`

**预防措施**：
- ✅ 所有市场数据必须使用当日实时数据
- ✅ 优先使用权威来源：Trading Economics, LiveMint, Investing.com
- ✅ USD/CNY应参考exchangerate.guru或wise.com

---



### 2026-04-08 | 邮件链接缺少news子目录路径

**问题类型**: 邮件发送 / 链接路径
**严重程度**: 🔴 高
**状态**: ✅ 已修复

**问题描述**:
邮件中的链接错误，缺少 `news/` 子目录路径。

**错误链接**: `https://marvinchima723.github.io/NewsforWenyan/NewsforWenyan_2026-04-08.html` ❌
**正确链接**: `https://marvinchima723.github.io/NewsforWenyan/news/NewsforWenyan_2026-04-08.html` ✅

**根本原因**:
`send_email.py` 第66行硬编码的URL没有包含 `news/` 子目录：
```python
news_url = f"https://marvinchima723.github.io/NewsforWenyan/NewsforWenyan_{news_date}.html"
```

**实际情况**:
- 4月8日起，所有新闻HTML文件都存放在 `news/` 子目录下

**解决方案**:
修改 `send_email.py` 第66行，添加 `news/` 路径：
```python
news_url = f"https://marvinchima723.github.io/NewsforWenyan/news/NewsforWenyan_{news_date}.html"
```

**预防措施**:
- ✅ 已修复 `send_email.py`
- ✅ 邮件链接路径与实际文件位置保持一致

---



### 2026-04-06 | 邮件链接路径错误

**问题类型**: 邮件发送 / 链接路径
**严重程度**: 🔴 高
**状态**: ✅ 已修复

**问题描述**:
邮件中的链接错误指向 `news/NewsforWenyan_2026-04-06.html`，但该文件实际位于根目录。

**根本原因**:
`send_email.py` 第66行硬编码了 `news/` 子文件夹路径：
```python
news_url = f"https://marvinchima723.github.io/NewsforWenyan/news/NewsforWenyan_{news_date}.html"
```

**实际情况**:
- `news/` 文件夹只包含 `NewsforWenyan_2026-04-05.html`
- 4月6日文件 `NewsforWenyan_2026-04-06.html` 在根目录

**错误链接**: `https://marvinchima723.github.io/NewsforWenyan/news/NewsforWenyan_2026-04-06.html` ❌
**正确链接**: `https://marvinchima723.github.io/NewsforWenyan/NewsforWenyan_2026-04-06.html` ✅

**解决方案**:
修改 `send_email.py` 第66行，去掉 `news/` 路径：
```python
news_url = f"https://marvinchima723.github.io/NewsforWenyan/NewsforWenyan_{news_date}.html"
```

**预防措施**:
- ✅ 所有新闻HTML文件都存放在根目录
- ✅ `news/` 文件夹已废弃，不再使用
- ✅ 邮件链接路径已修正

---

### 2026-04-12 | GitHub Pages 404 ——本地commits未推送 ⭐⭐⭐

**问题类型**: 基础设施 / GitHub Pages
**严重程度**: 🔴 极高
**状态**: ✅ 已修复（手动执行git push）

**问题描述**:
访问 `https://marvinchima723.github.io/NewsforWenyan/` 出现 404 File Not Found 错误。

**根本原因**:
⚠️ **这是第4次出现同样的问题！**

GitHub Pages显示404的原因是：**本地有commits未推送到GitHub**

执行 `git status` 显示：
```
Your branch is ahead of 'origin/main' by 3 commits.
```

即使创建了index.html和所有HTML文件，如果这些变更没有推送到GitHub远程仓库，GitHub Pages就无法访问这些文件。

**4次出现记录**：
1. 2026-04-06：首次建立index.html，未推送
2. 2026-04-06：v3深度报告，未推送
3. 2026-04-10~11：多次简报累积，未推送
4. 2026-04-12：再次累积3个commits未推送

**解决方案**:
```bash
cd /Users/mma/Dropbox/0-行研专家/NewsforWenyan
git status  # 检查是否有未推送的commits
git push    # 推送到GitHub（可能需要VPN）
```

**根本原因分析**：
GitHub Push因网络问题（HTTP2 framing layer error）频繁失败，但任务流程中未检测失败状态。错误被静默吞掉，导致本地认为"已同步"而实际GitHub端落后。

**预防措施（必须执行）**：
- ✅ **每次自动化任务最后，必须执行：`git status` 检查是否需要push**
- ✅ **如果显示"ahead by X commits"，必须执行`git push`**
- ✅ **如果`git push`失败（网络问题），记录到当日执行报告，提醒需要手动补推**
- ✅ **自动化任务日志模板增加Git状态检查项**：
  ```
  Git Status: [检查结果]
  Git Push: [成功/失败]
  If Failed: [需要VPN手动推送]
  ```

---

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

### 2026-04-06 | v3深度报告404——文件未同步到GitHub

**问题类型**: 基础设施 / GitHub Pages
**严重程度**: 🔴 高
**状态**: ⚠️ 待修复（网络问题阻塞）

**问题描述**:
访问 `https://marvinchima723.github.io/NewsforWenyan/Hormuz_Crisis_Report_v3_2026-04-06.html` 显示 GitHub Pages 404 错误。

**根本原因**:
创建了新的HTML文件后，没有同步推送到GitHub。每次创建新的HTML文件（无论是每日简报还是专题深度报告），都必须执行 `git add` → `git commit` → `git push` 流程，否则GitHub Pages无法访问。

**解决方案**:
需要VPN连接后执行：
```bash
cd /Users/mma/Dropbox/0-行研专家/NewsforWenyan
git add Hormuz_Crisis_Report_v3_2026-04-06.html index.html
git commit -m "feat: add Hormuz v3 report"
git push
```

**预防措施**:
- ✅ 每次创建新HTML文件后，立即执行完整git流程
- ✅ 自动化任务清单已更新（见下方"同步Git"步骤）
- ⚠️ GitHub推送需要VPN（与中国网络不兼容）

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

每次生成新闻或深度专题后，确认以下步骤：

- [ ] 生成当日 HTML 文件（例：`NewsforWenyan_YYYY-MM-DD.html`）或专题文件（例：`Hormuz_Crisis_Report_v3_YYYY-MM-DD.html`）
- [ ] 验证所有外部链接可访问
- [ ] 更新 `index.html` 的历史简报列表或深度专刊入口
- [ ] 更新 `news_sources_urls.md` 记录当日 URL（如适用）
- [ ] **⚠️ 同步Git（必须）：** `git add` → `git commit` → `git push origin main`
  - ⚠️ 需要VPN连接
  - ⚠️ 深度专题文件（不是每日简报）也需要同步！不能只更新index.html
- [ ] **⭐ Git最终检查（必须）：** 执行 `git status` 确认 "Your branch is ahead of 'origin/main' by 0 commits"
  - 如果显示 "ahead by X commits"，必须再次执行 `git push`
  - 如果push失败，记录"⚠️ GitHub未同步，需要VPN手动推送"
- [ ] 发送邮件 `python3 send_email.py YYYY-MM-DD`（仅每日简报）
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
