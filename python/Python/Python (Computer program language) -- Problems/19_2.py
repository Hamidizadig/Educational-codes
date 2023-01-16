nomber=int(input('Enter Nomber : '))
pow=int(input('Enter Nomber : '))
sum=0
temp=nomber
for i in range(1,pow):
    sum=0
    for j in range(1,nomber+1):
        sum=sum+temp
    temp = sum
print(nomber,"^",pow,"=",sum)
