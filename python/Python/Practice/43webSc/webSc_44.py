import re
import requests
from bs4 import BeautifulSoup

result=requests.get("https://conferenceindex.org/conferences")
# print(result.status_code)
soup=BeautifulSoup(result.content,"html.parser")
res=soup.find("h1")
print(res)
print(res.text)
print(res.text.strip())


res=soup.select("ul.list-unstyled>li")
for item in res:
    print(item.text.strip())