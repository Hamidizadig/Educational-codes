# import demjson
# class Person:
#     def __init__(self, id, name, age):
#         self.id = id
#         self.name = name
#         self.age = age
#     def __str__(self) -> str:
#         return f"id : {self.id} \tname : {self.name}\tage : {self.age} "
# person1 = Person(1, "saxis", "shonz")
# person2 = Person(2, "kals", "shuz")
# list1=[]
# list1.append(person1.__dict__)
# list1.append(person2.__dict__)
# jStr = demjson.encode(person1.__dict__)
# print(jStr)
# print(type(jStr))



# class Person:
#     def __init__(self,id,name,age):
#         self.id=id
#         self.name=name
#         self.age=age
#     def __str__(self) -> str:
#         return f"id : {self.id} \tname : {self.name}\tage : {self.age} "
# person1=Person(1,"saxis","shonz")
# person2=Person(2,"kals","shuz")
# list1=[]
# list1.append(person1.__dict__)
# list1.append(person2.__dict__)
# jStr=demjson.encode(list1)
# print(jStr)
# print(type(jStr))
# demjson.decode(jStr)import demjson