# import requests
# from bs4 import BeautifulSoup

# res=requests.get("https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_installation.htm#")
# soup=BeautifulSoup(res.content,"html.paerser")
# print(soup.head)


# import requests
# from bs4 import BeautifulSoup

# with open("/https://stackoverflow.co/teams/") as file1:
#     soup=BeautifulSoup(file1, "html.parser")
#     print(soup.find_all('amg'))
# #   print(soup.body)


# import requests
# from bs4 import BeautifulSoup

# with open("/https://stackoverflow.co/teams/") as file1:
#     soup=BeautifulSoup(file1, "html.parser")
#     imgList=soup.find_all('img')
#     for img in imgList:
#         print(img)


import requests
from bs4 import BeautifulSoup

# with open("/https://stackoverflow.co/teams/") as file1:
#     soup=BeautifulSoup(file1, "html.parser")
#     imgList=soup.find_all('img')
#     for img in imgList:
#         print(img['src'])
#     links=soup.find_all('a')
#     for link in links:
#         print(link)
#         print(link('href'))


# items=soup.select("div")
# print(items)


# items=soup.select(".img-box")
# print(items)


# items=soup.select("#title1")
# print(items)


# items=soup.select("#title1")
# for item in items:
#     print(item['href'])


# items=soup.select("#title1")
# for item in items:
#     print(item.text)


# res=requests.get("https://webscraper.io/test-sites")
# soup=BeautifulSoup(res.content,"html.paerser")
# # items=soup.select('body')
# items=soup.select('li')
# for item in items:
#     print(item)


# res=requests.get("https://webscraper.io/test-sites")
# soup=BeautifulSoup(res.content,"html.paerser")
# # items=soup.select('body')
# items=soup.select('li')
# print(f"Item Count : {len(items)}")
# for item in items:
#     print(item)


# res=requests.get("https://webscraper.io/test-sites")
# soup=BeautifulSoup(res.content,"html.paerser")
# # items=soup.select('body')
# items=soup.select('div.thambnail')
# print(f"Item Count : {len(items)}")
# for item in items:
#     print(item)


res = requests.get("https://webscraper.io/test-sites")
soup = BeautifulSoup(res.content, "html.paerser")
# items=soup.select('body')
items = soup.select('div.thambnail')
print(f"Item Count : {len(items)}")
for item in items:
    print(item.select('h4>a')[0].text.scrip())
    productPrice = item.select('h4.price')[0].text.strip('\n')
    imgSrc = item.select(".img-responsive")[0]['srs']
    print(f"name : {productName}\tPrice : {productPrice}\t img : {imgSrc}")
