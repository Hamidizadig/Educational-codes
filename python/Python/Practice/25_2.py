def append_sum_list(func):
    def inner(numList):
        numList.append(sum(numList))
        return numList
    return inner
      
@append_sum_list
def printList(list1):
    return list1
    
list1=[12.85,45,454,0,84,4,484,84,8,5,5]
print(printList(list1))