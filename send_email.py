#!/usr/bin/env python3
"""
News for Wenyan - Email Sender
Sends daily news link with love message to Wenyan
"""

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

def get_config():
    """获取邮件配置"""
    return {
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587,
        'smtp_user': 'marvin.cmma@gmail.com',
        'smtp_password': os.getenv('SMTP_PASSWORD', 'cxvgbpuufygvrkwv'),
        'recipients': ['yoyozwy@gmail.com', 'marvin.cmma@gmail.com']
    }

def get_love_message(date_str, news_url):
    """生成充满爱意的邮件内容"""
    quotes = [
        '"The best thing to hold onto in life is each other."',
        '"Love is not about how many days, months, or years you have been together. Love is about how well you love each other every single day."',
        '"In all the world, there is no heart for me like yours."',
        '"You are my today and all of my tomorrows."'
    ]
    
    import random
    quote = random.choice(quotes)
    
    return f"""💌 To My Beloved Wenyan,

My dearest Wenyan,

{quote}

You are not just my wife, but my greatest inspiration. In a world of uncertainty, you remain my constant—grounding me with your wisdom, your strength, and your unwavering love.

🌟 Today, I pray for you:
"The Lord bless you and keep you; the Lord make his face shine on you and be gracious to you." — Numbers 6:24-26

May this day bring you clarity, peace, and the energy to conquer whatever challenges lie ahead! 🦋

永远爱你 ❤️
— Marvin

━━━━━━━━━━━━━━━━━━━━
📰 今日新闻:
{news_url}
━━━━━━━━━━━━━━━━━━━━

News for Wenyan · Powered by AI
"""

def send_email(news_date=None, news_url=None):
    """发送邮件"""
    config = get_config()
    
    if news_date is None:
        news_date = datetime.now().strftime('%Y-%m-%d')
    if news_url is None:
        news_url = f"https://marvinchima723.github.io/NewsforWenyan/NewsforWenyan_{news_date}.html"
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f'☀️ News for Wenyan - {datetime.now().strftime("%Y年%m月%d日")}'
    msg['From'] = config['smtp_user']
    msg['To'] = ', '.join(config['recipients'])
    
    text_content = get_love_message(news_date, news_url)
    text_part = MIMEText(text_content, 'plain', 'utf-8')
    msg.attach(text_part)
    
    try:
        server = smtplib.SMTP(config['smtp_server'], config['smtp_port'], timeout=60)
        server.starttls()
        server.login(config['smtp_user'], config['smtp_password'])
        server.send_message(msg)
        server.quit()
        print(f'✅ 邮件发送成功! ({news_date})')
        return True
    except Exception as e:
        print(f'❌ 发送失败: {e}')
        return False

if __name__ == '__main__':
    import sys
    date = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime('%Y-%m-%d')
    send_email(date)