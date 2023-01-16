import json

person1={
        'id':1,
        'name':'azita',
        'family':'shuz',
        'age':42,
        'avg':17.86,
        'marital':True,
        'children':[{'name':'shanix','age':9},{'name':'pasash','age':4}]
        }


print(person1)
print(type(person1))
jstr=json.dumps(person1)
print(jstr)
print(type[jstr])
print(len(jstr))
print(jstr[2])

with open('file2.json','w')as file2:
    file2.write(jstr)

