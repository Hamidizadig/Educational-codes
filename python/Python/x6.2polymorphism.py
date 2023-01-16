def sum(datatype, *args):
    if(datatype == "int"):
        s = 0
    elif(datatype == "str"):
        s = ""
    for i in args:
        s += i
    return s


print(sum("int", 3, 4))
print(sum("int", 3, 5, 8, 4, 4))
print(sum("int", 3, 99))
print(sum("str", "aaa", "fff", "gg", "zzz"))
