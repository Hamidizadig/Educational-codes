# import requests
# import json
# parameter={'rel_rhy':'jingle'}
# response=requests.get('https://api.datamuse.com/words',parameter)

# if response.status_code==200:
#     print(response.content)
# else:
#     print('Error: ',response.status_code)


import requests
import json
parameter = {'rel_rhy': 'jingle'}
response = requests.get('https://api.datamuse.com/words', parameter)
if response.status_code == 200:
    print(json.dumps(response.json(), indent=4))
else:
    print('Error: ', response.status_code)


# https://openweathermap.org
# https://openweathermap.org/current
# free API : https://api.openweathermap.org/data/2.5/weather?
