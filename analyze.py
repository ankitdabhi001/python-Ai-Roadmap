import subprocess

def run_deepseek(prompt):
    result = subprocess.run(
        ['ollama', 'run', 'deepseek-coder'],
        input=prompt.encode('utf-8'),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode('utf-8')

# Load resume & job description
with open("resume.txt", "r", encoding="utf-8") as f:
    resume = f.read()

with open("job_description.txt", "r", encoding="utf-8") as f:
    job_desc = f.read()

# Create prompt
prompt = f"""
You are an AI that compares resumes and job descriptions.

📄 Resume:
{resume}

📌 Job Description:
{job_desc}

🎯 TASK:
- Identify matching skills
- List missing qualifications
- Give a match score (0-100)
- Suggest resume improvements

Respond in this format:

🟢 Match Score: __%
🛠 Matching Skills: [...]
🔴 Missing Skills: [...]
📝 Suggestions: [...]
"""

# Run DeepSeek
output = run_deepseek(prompt)

# Show result
print("===== AI Resume Analysis =====")
print(output)
