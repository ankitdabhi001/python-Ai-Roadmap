import requests
from bs4 import BeautifulSoup


url="https://remoteok.io/remote-dev-jobs"
header={'user-agent':'chrome'}

response=requests.get(url,headers=header)
soup=BeautifulSoup(response.text,'html.parser')


job_section= soup.find_all('tr',class_='job')



with open("job.txt","w",encoding="utf-8") as f:

    for job in job_section:
        title=job.find('h2')
        compony=job.find('h3')

        if title and compony:
            f.write(f"COMPONY : {compony.text.strip() + "\n"}")
            f.write(f"JOb: {title.text.strip() +"\n"}")