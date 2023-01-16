products=[
    {'name':'A','price':'1','brand':'LG'},
    {'name':'B','price':'10','brand':'SONY'},
    {'name':'C','price':'100','brand':'SNOVA'},
    {'name':'D','price':'1000','brand':'SONY'}
    ]
brand=input('Enter Brand : ')
# print(list(filter(lambda product : product['brand']=='SONY' ,products)))
print(list(filter(lambda product : product['brand']==brand ,products)))