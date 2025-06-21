
# READ EMAIL 

import imaplib
import email
from email.header import decode_header
from gpt4all import GPT4All

model_name="Llama-3.2-3B-Instruct-Q4_0.gguf"
model_path = "E:/Python Roadmap/python-Ai-Roadmap/models"
model = GPT4All("Llama-3.2-3B-Instruct-Q4_0.gguf", model_path=model_path, allow_download=False)


# ------------------------------
# 1. Gmail IMAP credentials
# ------------------------------
EMAIL = "a1000aje@gmail.com"
PASSWORD = "Your App Password"  # Use Gmail App Password (not your normal password)

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
latest_5_ids = email_ids[-1:]  # Last 1 emails

# ------------------------------
# 5. Read each email
# ------------------------------# Open GPT4All model once
with GPT4All(model_name, model_path=model_path, allow_download=False) as model:
    for i in reversed(latest_5_ids):
        status, data = mail.fetch(i, "(RFC822)")
        if status != "OK" or data is None:
            print(f"Failed to fetch email ID {i}")
            continue

        try:
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
        except:
            print(f"Error decoding email ID {i}")
            continue

        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else "utf-8")

        from_ = msg.get("From", "Unknown")

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
                        continue
        else:
            try:
                body = msg.get_payload(decode=True).decode(errors="ignore")
            except:
                body = "[Error reading body]"
        new_body=body[:4000]
        prompt = f"Summarize this email in 2-3 sentences:\n{new_body}"
        summary = model.generate(prompt, max_tokens=150)

        print("=" * 60)
        print(f"📨 Subject: {subject}")
        print(f"👤 From: {from_}")
        print(f"📝 Body Preview:\n{body[:100]}...\n")
        print(f"🧠 Summary:\n{summary}")
        print("=" * 60)
# ------------------------------
# 6. Logout from the server
# ------------------------------
mail.logout()
