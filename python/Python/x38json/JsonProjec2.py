import json

# person1={
#         'id':1,
#         'name':'azita',
#         'family':'shuz',
#         'age':42,
#         'avg':17.86,
#         'marital':True,
#         'children':[{'name':'shanix','age':9},{'name':'pasash','age':4}]
#         }


# print(person1)
# print(type(person1))
# jstr=json.dumps(person1)
# print(jstr)
# print(type[jstr])
# print(len(jstr))
# print(jstr[2])

# with open('file2.json','w')as file2:
#     file2.write(jstr)


# person1={
#         'id':1,
#         'name':'azita',
#         'family':'shuz',
#         'age':42,
#         'avg':17.86,
#         'marital':True,
#         'children':[{'name':'shanix','age':9},{'name':'pasash','age':4}]
#         }
# with open('file3.json','w') as file3:
#     json.dump(person1,file3,indent=4)


person1={
        'id':1,
        'name':'azita',
        'family':'shuz',
        'age':42,
        'avg':17.86,
        'marital':True,
        'children':[{'name':'shanix','age':9},{'name':'pasash','age':4}]
        }
people=[person1,person1,person1]
# for item in people:
#     print(item)
        
        
with open('file4.json','w') as file4:
    json.dump(people,file4,indent=4)
    

# with open('file3.json','w') as file3:
#     json.dump(person1,file3,indent=4)
