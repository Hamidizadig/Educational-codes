# list1=[1,2,3,1]
# list2=[4,9,8,1,2]
# list3=[-7,4,7,1]
# print(list(map(lambda a,b,c: a+b+c ,list1,list2,list3)))


# --------------------------------------

# def mymap(func,*args):
#     pass

# list1=[1,2,3,1]
# list2=[4,9,8,1,2,9,4]
# list3=[-7,4,7,1]
# mymap(lambda x: x,list1,list2,list3)
    
# ---------------------------------------  

def fun1(n):
    return n*10   


 
def fun2(n):
    return n+400   
 
def fun3(n):
    return -1*n  


def fun4(n):
    return n*100   
 

def map_functions(x,functions):
    res_list=[] 
    for func in functions:
        res_list.append(func(x))  
    return res_list

print(map_functions(3,(fun1,fun2,fun3,fun4)))