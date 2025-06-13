import re
from gpt4all import GPT4All

# 🧠 Extract info using regex
def ai_pattern_extractor(text):
    extracted_info = {
        "name": re.findall(r'Name:\s*([A-Za-z.\s]+)', text),
        "email": re.findall(r'Email:\s*([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', text),
        "phone": re.findall(r'(?:Phone|Contact):\s*(\d{10})', text),
        "budget": re.findall(r'₹[\d,]+', text),
        "urls": re.findall(r'https?://[^\s|"]+', text)
    }

    print("📦 Extracted Data:")
    for k, v in extracted_info.items():
        print(f"{k.title()}: {v}")
    return extracted_info

# 🤖 Summarize using GPT4All LLaMA model
def summarize_with_llama(extracted_info):
    # ✅ Load model (ensure the model file is in /models)
    model_path = "E:/Python Roadmap/python-Ai-Roadmap/models"
    llm = GPT4All("Llama-3.2-3B-Instruct-Q4_0.gguf", model_path=model_path, allow_download=False)

    # 📝 Construct the prompt
    prompt = f"""
You are an AI assistant. Here's extracted info from resumes and listings:

Names: {extracted_info['name']}
Emails: {extracted_info['email']}
Phones: {extracted_info['phone']}
Budgets: {extracted_info['budget']}
URLs: {extracted_info['urls']}

✅ Generate a 3-line summary:
1. What kind of jobs or roles are these people likely targeting?
2. What tech or domains are most common?
3. How would a recruiter follow up with them?
"""

    # 🧾 Get summary
    output = llm.generate(prompt, max_tokens=300)
    print("\n🤖 Summary by LLaMA:\n")
    print(output.strip())

# 🧩 Raw Text Input
if __name__ == "__main__":
    raw_text = """
    👤 Name: Priya Sharma | 📧 Email: priya.sharma1995@gmail.com
    📞 Phone: 9988776655 | 💰 Expected Salary: ₹65,000
    🌐 Portfolio: https://priyasharma.dev | GitHub: https://github.com/priyacodes
    🔗 LinkedIn: https://linkedin.com/in/priya-sharma | #Python #MachineLearning #OpenToWork

    👤 Name: Ramesh K. | 📧 Email: rk_developer@outlook.com
    📞 Contact: 9123456789 | 💼 Budget: ₹55,500
    🌍 Website: http://rameshk.dev | #DataScience #RemoteJobs

    👤 Name: Ankit Verma | 📧 Email: ankit.ds123@gmail.com
    📱 Phone: 9876543210 | 💰 Budget: ₹42,500
    📡 Twitter: https://twitter.com/ankit_ai | #datascience #openToWork

    Product Listing: “iPhone 14 - Great condition, ₹79,999 - contact at deals@phonesale.in”
    Product Listing: “Samsung Smart TV - ₹55,000 | support@salehub.org”
    """

    data = ai_pattern_extractor(raw_text)
    summarize_with_llama(data)
