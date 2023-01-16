# import requests

# response=requests.get('http://api.open-notify.org/astros.json')

# # #search : http code list 404 notFund 200: ok
# jsonData=response.json()

# # print(jsonData['number'])
# # print(jsonData['people'])
# # print(jsonData['people'][1]['name'])

# for person in jsonData['people']:
#     if person['craft']=='Tiangong':
#         print(person['name']) 
# else:
#     print('Error : ',response.status_code)





import requests
import json
response=requests.get('http://api.open-notify.org/astros.json')
if response.status_code==200 :
    jsonData=response.json()
    # jsonStringData=json.dumps(jsonData,indent=4)
    jsonStringPeopleData=json.dumps(jsonData['people'],indent=4)
    print(jsonStringPeopleData)
else:
    print('Error : ',response.status_code)