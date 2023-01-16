def charChange(str):
    s=''
    for i in range(0,len(str)):
        if str[i].islower()==True:
            s+=str[i].upper()
        else:
            s+=str[i].lower()
    return s
str = input('Enter a string : ')
str =charChange(str)
print("Result is ",str)