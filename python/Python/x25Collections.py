import collections
from ftplib import parse150


class MyString(collections.UserString):
    def remove(self, s):
        self.data = self.data.replace(s, "")


str1 = MyString('saspu')
str1.remove("p")
print(str1)


# class MyList(collections.UserList):
#     def remove(self):
#         raise RuntimeError("Del not allowed")
# list1=MyList([1,5,2])
# print(list1)

# # try:
# #     print(x)
# # except:
# #     print('an exception occurred')

# list1.remove(5)
# print(list1)


# l=[4,2,5]


# dq1=collections.deque([1,2,3])
# print(dq1)
# dq1.append(4)
# dq1.appendleft(400000)
# dq1.pop()
# dq1.popleft()
# print(dq1)

# Person=collections.namedtuple("person","name age avg children")
# p1=Person("samix",45,9.6,["shuzes","asax"])
# p2=Person("sohav",30,14.8,[])

# print(p1)
# for i in Person._make(p1):
#     print(p1)

# print(p1._asdict()) // list to dic

# print(p1._fields)

# print(Person._make(p1))

# print(p1.avg)
# print(p1.children)
# print(p2.children.append("zara"))

# d1={"s":1,"z":2,"v":3}
# d2={20:"red",33:"green"}
# d3={100:True,300:False}
# d4=collections.ChainMap(d1,d2,d3,d1,d2,d3)
# print(d4)


# s1=collections.OrderedDict()
# s1["a"]="sipsos"
# s1["b"]="hisoxis"
# s1["c"]="shandis"
# s1["d"]="shxex"

# for k,v in s1.items():
#     print(f"{k} : {v}")
# print()
# s2=collections.OrderedDict()
# s2["d"]="shxex"
# s2["b"]="hisoxis"
# s2["c"]="shandis"
# s2["a"]="sipsos"
# for k,v in s2.items():
#     print(f"{k} : {v}")

# print(s1==s2)

# d1={"a":"ashaxis","b":"shapsus","n":"shakhis","m":"pasixios"}
# print(d1)
# d2={"a":"ashzesis","b":"pastaxis","m":"shimoxiz","n":"xasiox"}
# print(d2)
# print(d1==d2)

# d={}
# d=collections.defaultdict(object)
# print(d["red"])

# print(dir(collections))
# c=collections.Counter("rftgyhunjikml,kmnjbhgvfcvgbhnjkml,m;klbkhgvjftgyhujnlbkhgvfuigyuhijokpjhgvjfutygkhbjnkm;jiuiygvkhbljilhuyogiukhbjlk")
# print (c)
# l=[56,85,94,5,4,5,5,45,45,45,45,45,45,4,545,45,45,4,54,4,5,45,45,45,45,4,54,54,54,54,54,55,58,4,84,5,5484,8,5,5,4,84582,5,5,48,48,]
# c=collections.Counter(l).most_common(11)
# print (c)
