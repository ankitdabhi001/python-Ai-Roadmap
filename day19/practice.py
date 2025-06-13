import re

text = """
Meet Ankit: an aspiring data scientist.
Email: ankit.ds123@gmail.com
Phone: 9876543210
Budget: ₹42,500
"""

# Extract data
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w{2,4}\b', text)
phones = re.findall(r'\b\d{10}\b', text)
money = re.findall(r'₹?\d{1,3}(?:,\d{3})*(?:\.\d+)?', text)

print("📧 Emails:", emails)
print("📞 Phones:", phones)
print("💰 Budget:", money)
