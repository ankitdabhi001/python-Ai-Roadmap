import imaplib
import email
from email.header import decode_header
from gpt4all import GPT4All

# --------------------------
# LLM Setup
# --------------------------

model_name = "Llama-3.2-3B-Instruct-Q4_0.gguf"
model_path = "E:/Python Roadmap/python-Ai-Roadmap/models"

# --------------------------
# Gmail App Login
# --------------------------
EMAIL = "sender@gmail.com"
PASSWORD = " App_Password"  # App password (NOT your normal password)

# --------------------------
# Clean Email Function
# --------------------------
def clean_email(text):
    lines = text.splitlines()
    keep = []
    for line in lines:
        if any(x in line.lower() for x in ["unsubscribe", "view in browser", "confidential", "--", "gmail.com> wrote"]):
            break
        keep.append(line)
    return "\n".join(keep).strip()

# --------------------------
# Summarization Prompt
# --------------------------
def create_prompt(cleaned_text):
    return f"""
You are an intelligent assistant. Read the email below and summarize it in clear bullet points, focusing on key updates, deadlines, or tasks.

Email:
-------
{cleaned_text}

Summary:
- 
"""

# --------------------------
# Connect to Gmail + Read Emails
# --------------------------

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, PASSWORD)
mail.select("inbox")

status, messages = mail.search(None, "ALL")
email_ids = messages[0].split()
latest_ids = email_ids[-1:]  # Last 5 emails

# --------------------------
# Run summarization
# --------------------------
with GPT4All(model_name, model_path=model_path, allow_download=False) as model:
    for i in reversed(latest_ids):
        status, data = mail.fetch(i, "(RFC822)")
        if status != "OK" or data is None:
            continue

        try:
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
        except:
            continue

        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else "utf-8")

        from_ = msg.get("From", "Unknown")

        # Extract plain text body
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

        # Clean + Summarize
        clean_text = clean_email(body[:4000])
        prompt = create_prompt(clean_text)
        summary = model.generate(prompt, max_tokens=150)

        # Output
        print("=" * 60)
        print(f"📨 Subject: {subject}")
        print(f"👤 From: {from_}")
        print(f"📝 Body Preview:\n{body[:120]}...\n")
        print(f"🧠 Summary:\n{summary.strip()}")
        print("=" * 60)

        # Save to file (optional)
        with open("email_summaries.txt", "a", encoding="utf-8") as f:
            f.write(f"Subject: {subject}\nFrom: {from_}\nSummary:\n{summary.strip()}\n{'='*60}\n\n")

# Logout from Gmail
mail.logout()
