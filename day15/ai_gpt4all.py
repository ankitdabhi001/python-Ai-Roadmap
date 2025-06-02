import requests
from bs4 import BeautifulSoup
from gpt4all import GPT4All

# STEP 1: Scrape remoteok.io for job listings
url = "https://remoteok.io/remote-dev-jobs"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# STEP 2: Extract job titles and companies
job_section = soup.find_all('tr', class_='job')

jobs_data = []
for job in job_section:
    title_tag = job.find('h2')
    company_tag = job.find('h3')
    if title_tag and company_tag:
        title = title_tag.text.strip()
        company = company_tag.text.strip()
        jobs_data.append(f"{title} at {company}")

# Combine all jobs into a single text block
scraped_text = "\n".join(jobs_data)

# Print scraped jobs (optional)
print("🧾 Scraped Jobs:\n")
print(scraped_text[:500] + "\n...")  # Preview only first few lines

# STEP 3: Use GPT4All (LLaMA3) to summarize
model = GPT4All("Llama-3.2-3B-Instruct-Q4_0.gguf")
model.open()

prompt = f"""
Here are some recent remote developer job postings:\n\n{scraped_text}

Summarize the above jobs in 3-4 bullet points with main trends or roles:
"""

summary = model.prompt(prompt)

# STEP 4: Print Summary
print("\n📌 Summary of RemoteOK Jobs:\n")
print(summary)
