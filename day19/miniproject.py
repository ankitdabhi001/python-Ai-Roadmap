
# mini project  AI Pattern Extractor

import re

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

name = re.findall(r'Name:\s*([A-Za-z.\s]+)', raw_text)
email = re.findall(r'Email:\s*([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)', raw_text)
phone=re.findall(r'(?:Phone|Contact):\s*\d{10}',raw_text)
budget=re.findall(r'₹[\d,]+',raw_text)
urls = re.findall(r'https?://[^\s|]+', raw_text)

print(name)
print(email)
print(phone)
print(budget)
print(urls)