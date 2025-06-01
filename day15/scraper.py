import requests
from bs4 import BeautifulSoup

# Step 1: Send HTTP request to the website
url = "https://quotes.toscrape.com"
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract quotes and authors
quotes = soup.find_all("div", class_="quote")

# Step 4: Print results
for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    print(f"Quote: {text}\nAuthor: {author}\n")
