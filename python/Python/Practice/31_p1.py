import collections
class MyList(collections.UserList):
    def append(self,x):
        if x in self:
            print("Error: %s" % x)
        else:
            collections.UserList.append(self,x)
            
list1=MyList([12,34,56,89,90])
list1.append(34)
print(list1)