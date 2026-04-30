#!/usr/bin/env python3
"""Send News for Wenyan daily email - Updated for 2026-04-30"""

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Email credentials
SENDER_EMAIL = "marvin.cmma@gmail.com"
APP_PASSWORD = "cxvgbpuufygvrkwv"
RECIPIENTS = ["yoyozwy@gmail.com", "marvin.cmma@gmail.com"]

# GitHub Pages URL for today's report
TODAY_STR = "2026-04-30"
GITHUB_PAGES_URL = f"https://marvinchima723.github.io/NewsforWenyan/news_{TODAY_STR}.html"

# Email content
TODAY = "2026年4月30日"

LOVE_MESSAGE = """
<p style="font-size: 16px; color: #333; margin-bottom: 20px;">
亲爱的文彦 🌹
</p>
<p style="font-size: 14px; color: #555; line-height: 1.8;">
霍尔木兹封锁第60天，美伊谈判陷入僵局。<br>
油价居高不下，全球通胀压力持续。<br>
但每一次危机，都孕育着机遇的种子。<br><br>
愿你在纷繁的信息中，保持清醒的判断力。<br>
这正是我爱你的原因 ❤️
</p>
"""

def send_email():
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"☀️ News for Wenyan - {TODAY}"
    msg['From'] = SENDER_EMAIL
    msg['To'] = ", ".join(RECIPIENTS)

    # Build HTML email
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; background-color: #f5f5f7; }}
            .container {{ background: white; border-radius: 16px; padding: 30px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }}
            h1 {{ color: #1d1d1f; font-size: 24px; margin-bottom: 10px; }}
            .date {{ color: #86868b; font-size: 14px; margin-bottom: 20px; }}
            .love-box {{ background: linear-gradient(135deg, #fff5f5, #fff0f0); border-left: 4px solid #ff6b6b; padding: 20px; border-radius: 8px; margin: 20px 0; }}
            .love-box p {{ margin: 0; color: #333; font-size: 15px; line-height: 1.8; }}
            .love-box .signature {{ color: #ff6b6b; font-weight: 600; margin-top: 10px; }}
            .news-link {{ display: inline-block; background: #007aff; color: white; padding: 14px 28px; border-radius: 10px; text-decoration: none; font-weight: 600; font-size: 16px; margin: 20px 0; }}
            .news-link:hover {{ background: #0051d5; }}
            .highlights {{ background: #f5f5f7; padding: 20px; border-radius: 8px; margin: 20px 0; }}
            .highlights h3 {{ color: #1d1d1f; font-size: 16px; margin-bottom: 12px; }}
            .highlights ul {{ margin: 0; padding-left: 20px; }}
            .highlights li {{ color: #333; font-size: 14px; line-height: 1.8; margin-bottom: 8px; }}
            .prayer {{ background: #f5f5f7; padding: 20px; border-radius: 8px; margin: 20px 0; text-align: center; }}
            .prayer .verse {{ font-style: italic; color: #333; font-size: 14px; line-height: 1.8; }}
            .prayer .ref {{ color: #007aff; font-weight: 600; margin-top: 10px; font-size: 13px; }}
            .footer {{ text-align: center; color: #86868b; font-size: 12px; margin-top: 30px; padding-top: 20px; border-top: 1px solid #e5e5e5; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>☀️ News for Wenyan</h1>
            <p class="date">{TODAY} · 星期四</p>

            <div class="love-box">
                {LOVE_MESSAGE}
            </div>

            <div class="highlights">
                <h3>📰 今日要点</h3>
                <ul>
                    <li>🌏 霍尔木兹封锁第60天，美伊谈判陷入僵局，特朗普确认维持封锁</li>
                    <li>📊 世界银行警告：2026年全球能源价格将上涨24%，大宗商品涨16%</li>
                    <li>💻 谷歌、微软、Meta、亚马逊同日发布财报，AI变现能力获验证</li>
                    <li>📈 谷歌云营收首破$200亿（+63%），股价盘后大涨7%</li>
                    <li>📉 Meta资本支出上限$1350亿（+87%），股价重挫5%</li>
                    <li>🏦 阿里千问登顶全球调用榜，中东主权基金持续押注中国AI</li>
                    <li>🗾 港股4月收官，恒生科技指数涨4.76%，半导体股领涨</li>
                </ul>
            </div>

            <a href="{GITHUB_PAGES_URL}" class="news-link">📖 查看完整新闻简报 →</a>

            <div class="prayer">
                <p class="verse">"你们要尝尝主恩的滋味，便知道他是美善。"</p>
                <p class="ref">— 诗篇 34:8 🙏</p>
            </div>

            <div class="footer">
                <p>Generated with ❤️ for Wenyan</p>
            </div>
        </div>
    </body>
    </html>
    """

    msg.attach(MIMEText(html_content, 'html'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENTS, msg.as_string())
        print(f"✅ Email sent successfully to {RECIPIENTS}")
        return True
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return False

if __name__ == "__main__":
    send_email()