# import jmespath
# data={
#   "people": [
#     {
#       "age": 20,
#       "tags": ["a", "b", "c"],
#       "name": "Bob"
#     },
#     {
#       "age": 25,
#       "tags": ["d", "e", "f"],
#       "name": "Fred"
#     },
#     {
#       "age": 30,
#       "tags": ["g", "h", "i"],
#       "name": "George"
#     }
#   ]
# }
# print(type(data))
# print(jmespath.search("people[*].{name: name, tags: tags[0]}",data))



# people={
#     "People":[
                
#              {'id':1,'name':"samiz" ,'age':30,'children':[{'name':'simma',"age":18}]},
#              {'id':2,'name':"shaniz",'age':20,'children':[{'name':'ships',"age":27}]},
#              {'id':3,'name':"usox"  ,'age':35,'children':[]}
                                  
#               ]
#     }
# print(jmespath.search("People[0].name",people))
# print(jmespath.search("People[2].age",people))
# print(jmespath.search("People[1].[name,age]",people))
# print(jmespath.search("People[*].[name,age]",people))
# print(jmespath.search("People[*].name",people))
# print(jmespath.search("People[:2].name",people))
# print(jmespath.search("People[1].children[0].name",people))
# print(jmespath.search("People[1].children[*].name",people))
# print(jmespath.search("People[*].children[*].name",people))
# print(jmespath.search("People[?age>`25`].name",people))
# print(jmespath.search("People[?age>`25`]children",people))
# print(jmespath.search("People[?age>`25`]children[*].[name,age]",people))


