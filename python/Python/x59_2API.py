import requests
import json
parameter={'q':'Stuttgart' ,'appid' :'e3ddc078c5cfebe9566a6a7602612e57'}

# response=
# parameter=q={stuttgart}&appid={API e3ddc078c5cfebe9566a6a7602612e57}
response=requests.get('https://api.openweathermap.org/data/2.5/weather?',parameter)

if response.status_code==200:
    jData=response.json()
    mainInfo=jData['main']
    print(mainInfo['temp'])
    print(mainInfo['pressure'])
    print(mainInfo['humidity'])
    # print(json.dumps(response.json(),indent=4))
else:
    print('Error: ',response.status_code)
    

