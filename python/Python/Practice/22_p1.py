# def myIsDigit(x):
#     try:
#         int(x)
#         return True
#     except:
#         return False
# x=input("Enter Number : ")
# if myIsDigit(x)==True:
#     x=int(x)
#     print(x/10)
# else:
#     print("Error")




def myIsDigit(x):
    try:
        int(x)
        return True
    except:
        return False
x=input("Enter Number : ")
if myIsDigit(x):
    x=int(x)
    print(x/10)
else:
    print("Error")

