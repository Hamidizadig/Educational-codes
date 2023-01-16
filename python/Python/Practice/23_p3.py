# list1=[10,20,30,40,50,60,70,80,90,100]
# list2=[item for item in list1 if item%3==0]
# print(list2)



# str1="shi rex   amikas simma    saraz"
# str2=''.join([ch for ch in str1 if ch!=' '])
# print(str2)


# str1=input("input text: ")
# # str1="shi rex   amikas simma    saraz"
# removeList=['b','e','d',' ']
# str2=''.join([ch for ch in str1 if ch not in removeList])
# str3='_'.join([ch for ch in str1 if ch!=' '])
# print(str3)





str1="shi rex   amikas simma    saraz"
str2=''.join(['\t' if ch==' ' else ch for ch in str1])
print(str2)