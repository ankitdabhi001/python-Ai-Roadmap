from gpt4all import GPT4All
import requests
from bs4 import BeautifulSoup

def scrape_jobs(keyword=None):
    url = "https://remoteok.io/remote-dev-jobs"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_rows = soup.find_all('tr', attrs={'data-id': True})
    job_titles = []
    for job in job_rows:
        title_tag = job.find('h2')
        if title_tag:
            title = title_tag.text.strip()
            if keyword:
                if keyword.lower() in title.lower():
                    job_titles.append(title)
            else:
                job_titles.append(title)
    print(f"Found {len(job_titles)} jobs")
    return job_titles


def analyze_trends(job_titles):
    text = "\n".join(job_titles)

    # Load your model (adjust model name & path if needed)
    model = GPT4All("Llama-3.2-3B-Instruct-Q4_0.gguf", model_path="./models", allow_download=False)

    prompt = f"""
Here is a list of job titles posted recently:\n\n{text}

Summarize the trends in 3–4 bullet points. What roles, languages, or patterns stand out?
"""
    print("🧠 Sending prompt to GPT4All...")
    response = model(prompt)
    return response

if __name__ == "__main__":
    # Optional: filter jobs by keyword like "Python"
    jobs = scrape_jobs(keyword="Python")
    print("✅ Scraped Jobs:\n", "\n".join(jobs[:10]), "\n...")

    if jobs:
        summary = analyze_trends(jobs)
        print("\n📌 GPT Summary of Job Trends:\n", summary)
    else:
        print("No jobs found to analyze.")
