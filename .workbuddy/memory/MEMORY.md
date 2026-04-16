# MEMORY.md · 长期记忆

## 项目概况
- 项目：Wenyan每日新闻（NewsforWenyan）
- GitHub: https://github.com/marvinchima723/NewsforWenyan
- GitHub Pages: https://marvinchima723.github.io/NewsforWenyan/
- 本地路径: /Users/mma/Dropbox/0-行研专家/NewsforWenyan/
- 发送邮箱: yoyozwy@gmail.com / marvin.cmma@gmail.com

## 发送方式
- macOS mail命令发送HTML邮件（mail exit 0）
- 注意：Gmail SMTP因网络限制无法直连，实际投递结果待确认
- 建议探索外部邮件API（SendGrid/Mailgun）提升投递可靠性

## 内容风格
- 苹果设计风格（SF Pro字体、深色主题#0a0a0c）
- 麦肯锡报告格式（分类清晰、数据驱动、关键洞察）
- 分类：地缘政治、全球经济、亚太、科技、主权基金投资
- 关键数据表格：原油、亚洲股市指数

## 自动化
- 每天早上8点发送（FREQ=DAILY;BYHOUR=8）
- 状态：ACTIVE
- workspace: /Users/mma/Dropbox/0-行研专家/NewsforWenyan

## 邮件投递注意
2026-04-12记录：sendmail本地返回0，但Gmail SMTP因网络限制无法直连，建议使用外部邮件API提升可靠性。