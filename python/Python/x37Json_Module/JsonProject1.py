import json

# jsonString='{\"id\":1,\"name\":\"amix\",\"age\":22}'
# obj1=json.loads(jsonString)
# print(obj1)
# print(type(obj1))
# print(obj1['name'])


# with open("\file1.json", "r") as file1:
#     obj1 = json.load(file1)
#     print(obj1)
#     print(type(obj1))


# with open("file1.json","r") as file1:
#     objList=json.load(file1)
#     for obj in objList:
#         print(obj)

#     print(objList[0]['name'])

# print


person1 = {
    'id': 1,
    'name': 'azita',
    'family': 'shuz',
    'age': 42,
    'avg': 17.86,
    'marital': True,
    'children': [{'name': 'shanix', 'age': 9}, {'name': 'pasash', 'age': 4}]
}
print(person1)
print(type(person1))
jstr = json.dumps(person1)
print(jstr)
print(type[jstr])
print(len(jstr))
print(jstr[2])
