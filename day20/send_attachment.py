
# SEND EMAIL USING SCHEDULE 

import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os 

def send_email():
    sender_email = "your_email@gmail.com"
    receiver_email = "receiver_email@example.com"
    app_password = "your_app_password"

    # Create the email
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = '📎 Email with Attachment from Python (Scheduled)'

    body = "Hi,\n\nThis is a scheduled email with attachment.\n\nRegards,\nAnkit"
    message.attach(MIMEText(body, 'plain'))

    # Attachment part
    filename = "test.pdf"
    filepath = "E:/files/test.pdf"

    if os.path.exists(filepath):
        with open(filepath, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename={os.path.basename(filepath)}',
            )
            message.attach(part)
    else:
        print("❌ File not found!")
        return

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("✅ Scheduled email sent successfully!")

# 🔁 Step 1: Schedule the email
schedule.every().day.at("10:00").do(send_email)  # ⏰ Set your time here (24-hr format)

# 🔁 Step 2: Keep script running
print("⏳ Waiting to send scheduled email... Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every 60 seconds
