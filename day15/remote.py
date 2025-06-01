import requests
from bs4 import BeautifulSoup

# Step 1: Read the HTML file
with open("abc.html", "r", encoding="utf-8") as f:
    reader = f.read()

# Step 2: Parse HTML
soup = BeautifulSoup(reader, 'html.parser')

# Step 3: Find all <a> tags
ab = soup.find('a')

# Step 4: Extract and write the href and text of each link
with open("content.txt", "w", encoding="utf-8") as f:
    for value in ab:
        text=value.get_text()
        f.write(text)