import imaplib
import email
from email.header import decode_header
import requests

# -------------------------------------
# 🔐 Gmail Credentials (Set yours here)
# -------------------------------------
EMAIL = "a1000aje@gmail.com"
APP_PASSWORD = "app_password"  # 🔑 from https://myaccount.google.com/apppasswords

# -------------------------------------
# 🔌 Login to Gmail
# -------------------------------------
print("🔌 Logging into Gmail...")
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, APP_PASSWORD)
mail.select("inbox")

# -------------------------------------
# 📥 Get last 5 emails
# -------------------------------------
print("📥 Fetching latest 5 emails...")
status, messages = mail.search(None, "ALL")
email_ids = messages[0].split()[-5:]

# -------------------------------------
# 🤖 Process & summarize each email
# -------------------------------------
for i in reversed(email_ids):
    print("📨 Processing email ID:", i.decode())

    status, data = mail.fetch(i, "(RFC822)")
    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email)

    # ---- Decode subject ----
    subject, encoding = decode_header(msg["Subject"])[0]
    subject = subject.decode(encoding if encoding else "utf-8") if isinstance(subject, bytes) else subject

    # ---- Get sender ----
    from_ = msg.get("From")

    # ---- Extract plain text body ----
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                try:
                    body = part.get_payload(decode=True).decode(errors="ignore")
                    break
                except:
                    pass
    else:
        body = msg.get_payload(decode=True).decode(errors="ignore")

    # ---- Prepare prompt for DeepSeek ----
    prompt = f"Summarize this email in 2-3 sentences:\n\n{body}"
    print("🤖 Sending to DeepSeek...")

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "deepseek-coder",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        summary = response.json().get("response", "❌ No summary returned.")
        print("✅ Got response from DeepSeek!")
    except Exception as e:
        summary = f"❌ Error: {e}"

    # ---- Display & Save ----
    print("\n" + "=" * 60)
    print(f"📨 Subject: {subject}")
    print(f"👤 From: {from_}")
    print(f"📝 Body Preview:\n{body[:200]}...\n")
    print(f"🧠 Summary:\n{summary}")
    print("=" * 60 + "\n")

    with open("email_summaries.txt", "a", encoding="utf-8") as f:
        f.write(f"Subject: {subject}\nFrom: {from_}\nSummary: {summary}\n")
        f.write("=" * 60 + "\n")

# ✅ Logout
mail.logout()
print("✅ Done! Summaries saved in 'email_summaries.txt'")
