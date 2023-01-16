from MyPackage import requests
from MyPackage import re

# res=requests.get("https://darsman.com/")
# print(res.status_code)
# # print(res.text)
# print(re.findall(r'<title>(.*)</title>',res.text))



res=requests.get("https://yahoo.com/")
print(res.status_code)
# print(res.text)
print(re.findall(r'<title>(.*)</title>',res.text))


