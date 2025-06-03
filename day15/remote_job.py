import requests
from bs4 import BeautifulSoup

url = "https://remoteok.io/remote-dev-jobs"
browser = {'user-agent':'chrome'}

response =requests.get(url,headers=browser)
soup = BeautifulSoup(response.text,'html.parser')

job_selection=soup.find_all('tr',class_='job')

with open("letest.txt","w") as f:

    for a in job_selection:
        title = a.find('h2')
        compony = a.find('h3')

        f.write(f"Job = {title.text.strip() + "\n"}")
        f.write(f"compony = {compony.text.strip() + "\n"}")
        f.write("---------------------------" + "\n")


