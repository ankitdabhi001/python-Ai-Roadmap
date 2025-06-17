# import imaplib

# mail = imaplib.IMAP4_SSL("imap.gmail.com")
# mail.login("a1000aje@gmail.com",'yvxf sysr ejhk cume')
# mail.select("inbox")

import imaplib
import email
from email.header import decode_header

# ------------------------------
# 1. Gmail IMAP credentials
# ------------------------------
EMAIL = "a1000aje@gmail.com"
PASSWORD = "zbvh aidd ahgv vqzh"  # Use Gmail App Password (not your normal password)

# ------------------------------
# 2. Connect to Gmail Server
# ------------------------------
mail = imaplib.IMAP4_SSL("imap.gmail.com")  # SSL-secure connection
mail.login(EMAIL,PASSWORD)

# ------------------------------
# 3. Select the inbox
# ------------------------------
mail.select("inbox")

# ------------------------------
# 4. Search all emails
# ------------------------------
status, messages = mail.search(None, "ALL")

# Get the list of email IDs
email_ids = messages[0].split()
latest_5_ids = email_ids[-5:]  # Last 5 emails

# ------------------------------
# 5. Read each email
# ------------------------------
for i in reversed(latest_5_ids):
    status, data = mail.fetch(i, "(RFC822)")  # Fetch full email content
    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email)

    # -------- Decode Subject --------
    subject, encoding = decode_header(msg["Subject"])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding if encoding else "utf-8")

    # -------- Decode From --------
    from_ = msg.get("From")

    # -------- Get Body --------
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))
            if content_type == "text/plain" and "attachment" not in content_disposition:
                try:
                    body = part.get_payload(decode=True).decode(errors="ignore")
                    break
                except:
                    pass
    else:
        body = msg.get_payload(decode=True).decode(errors="ignore")

    # -------- Print Email --------
    print("=" * 50)
    print(f"📨 Subject: {subject}")
    print(f"👤 From: {from_}")
    print(f"📝 Body Preview:\n{body[:200]}...")  # First 200 characters
    print("=" * 50)

# ------------------------------
# 6. Logout from the server
# ------------------------------
mail.logout()
