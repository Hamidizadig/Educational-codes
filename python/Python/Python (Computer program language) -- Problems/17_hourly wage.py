price =  int(input('Enter price : '))
nextsYers=int(input('inter Year : '))
swelling=int(input('swelling is : '))
print ('Year     Price')
for i in range(1,swelling+1):
    price=price+(price*swelling/100)
    print(i,'  ',price)    