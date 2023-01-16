'''
try:
    x=int(input("enter Nomber : "))
    y=int(input("enter Number : "))
    print(x/y)
except:
    print("Error")'''

'''try:
    x=int(input("enter Nomber : "))
    y=int(input("enter Number : "))
    print(x/y)
except FileNotFoundError:/ ZeroDivisionError as error: -->system text
    print("Error")'''

try:
    x = int(input("enter Nomber a: "))
    y = int(input("enter Number b: "))
    print(x/y)
    l1 = [2, 5, 3]
    n = int(input("Enter index of list : "))
    print(l1[n])
    f = open("file2.txt", "r")
except ZeroDivisionError:
    print("Error1")
except IndexError:
    print("Error2")
except FileNotFoundError:
    print("Error3")
else:
    print("Ok")
finally:
    print("end")
