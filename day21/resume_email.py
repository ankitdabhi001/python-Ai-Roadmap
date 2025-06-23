

import subprocess
import re
import smtplib
from email.message import EmailMessage

# -------------------------
# 📧 EMAIL CONFIG
# -------------------------
YOUR_EMAIL = "a1000aje@gmail.com" 
APP_PASSWORD =  "zbvh aidd ahgv vqzh"   # Use Gmail App Password
RECEIVER_EMAIL = "ankitdabhi77777@gmail.com"

# -------------------------
# 📥 Read Resume and JD
# -------------------------
def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

resume = read_file("resume.txt")
job_description = read_file("job_description.txt")

# -------------------------
# 🧠 LLaMA3 Prompt
# -------------------------
prompt = f"""
You are simulating the output of a resume matching tool.

Compare the resume and job description and return the result in this format ONLY:

Match Score: __%
Matching Skills: [...]
Missing Skills: [...]
Suggestions: [...]

Resume:
{resume}

Job Description:
{job_description}
"""

# -------------------------
# 🦙 Run LLaMA3 with Ollama
# -------------------------
def run_llama(prompt):
    result = subprocess.run(
        ['ollama', 'run', 'llama3'],
        input=prompt.encode('utf-8'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode('utf-8')

# -------------------------
# 🧪 Execute
# -------------------------
output = run_llama(prompt)
print("===== AI Resume Analysis =====")
print(output)

# -------------------------
# 📊 Extract Score
# -------------------------
match = re.search(r"Match Score[:\s]+(\d{1,3})", output)
if match:
    score = int(match.group(1))
    print(f"🎯 Detected Match Score: {score}")

    # -------------------------
    # 📤 Send Email if Score ≥ 80
    # -------------------------
    if score >= 80:
        msg = EmailMessage()
        msg["Subject"] = f"✅ Resume Match Score: {score}% (AI Approved)"
        msg["From"] = YOUR_EMAIL
        msg["To"] = RECEIVER_EMAIL
        msg.set_content(f"""Hi Ankit,

✅ Your resume scored {score}% match with the job description!

Details:
{output}

– AI Resume Bot
""")

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(YOUR_EMAIL, APP_PASSWORD)
                smtp.send_message(msg)
                print("✅ Email sent!")
        except Exception as e:
            print(f"❌ Email failed: {e}")
else:
    print("⚠️ Could not detect a match score in the output.")
    print("🧾 Full Response:\n", output)
