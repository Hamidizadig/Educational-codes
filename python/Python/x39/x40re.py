# import re
# str1="mersedes anastas shutz simma anastas tsmo"
# res=re.search(r'anastas',str1) 
# print(res)
# print(res.group())



# import re
# str1="mersedes anastas shutz simma anastas tsmo"
# res=re.search(r'r.+s',str1) 
# print(res)
# print(res.group())


# import re
# str1="mersedes anastas shutz simma anastas tsmo"
# res=re.findall(r'anastas',str1) 
# print(res)


# import re
# str1="mersedes anastas shutz simma anastas tsmo"
# res=re.findall(r's.+?\s',str1) 
# print(res)





# import re
# str1='''
# mersedes
# sasam@gmail.com
# anastas@gmailcom
# 77anastas@gmailcom
# 09357784590
# shutz 
# 09183334784
# simma55@yaho.com
# 9172864587
# anastas tsmo
# '''
# mobilnombers=re.findall(r'09\d{9}',str1)
# print(mobilnombers)
# emails=re.findall(r'[a-z]+\@.+\..{2,3}',str1)
# print(emails)




# import re
# str1='''
# mersedes
# sasam@gmail.com
# anastas@gmailcom
# 77anastas@gmailcom
# 09357784590
# shutz 
# 09183334784
# simma55@yaho.com
# 9172864587
# anastas tsmo
# '''
# # mobilnombers=re.findall(r'09\d{9}',str1)
# # print(mobilnombers)
# # emails=re.findall(r'[a-z]+\@.+\..{2,3}',str1)
# # print(emails)

# emails=re.finditer(r'[a-zA-Z]+\@.+\..{2,3}',str1)
# print(emails)
# for item in emails:
#     print(item.group())
    
    
    
    

# import re
# str1='''
# mersedes
# sasam@gmail.com
# anastas@gmailcom
# 77anastas@gmailcom
# 09357784590
# shutz 
# 09183334784
# simma55@yaho.com
# 9172864587
# anastas tsmo
# '''

# res=re.sub(r'(09\d{9})\s','####',str1)
# print(res)




# import re
# str1='''
# name is: mersedes - age is : 40 - avg is: 1.25
# name is: shutzes - age is : 19 - avg is: 9.20
# name is: simma - age is : 26 - avg is: 4.82
# name is: yasus - age is : 19 - avg is: 8.02
# name is: anastas - age is : 29 - avg is: 11.5
# '''
# # res=re.search(r'name is simma -age is : 26 - avg is : 4.82' ,str1)
# res=re.findall(r'Name is: \w+ - Age is: \d+ - Avg is: \d+\.\d+',str1)
# for item in res:
#     print(item)



# import re
# str1='''
# name is: mersedes - age is : 40 - avg is: 1.25
# name is: shutzes - age is : 19 - avg is: 9.20
# name is: simma - age is : 26 - avg is: 4.82
# name is: yasus - age is : 19 - avg is: 8.02
# name is: anastas - age is : 29 - avg is: 11.5
# '''
# res=re.findall(r'Name is: (\w+) - Age is: (\d+) - Avg is: (\d+\.\d+)',str1)
# for item in res:
#     print(item)




import re
str1='''
name is: mersedes - age is : 40 - avg is: 1.25
name is: shutzes - age is : 19 - avg is: 9.20
name is: simma - age is : 26 - avg is: 4.82
name is: yasus - age is : 19 - avg is: 8.02
name is: anastas - age is : 29 - avg is: 11.5
'''

res=re.sub(r'Name is: (\w+) - Age is: (\d+) - Avg is: (\d+\.\d+)','\g<1>*\g<2>*\g<3>'str1)
print(res)