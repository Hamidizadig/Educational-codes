# T(n,m)=n!\(m!*(n-m)!)

# 5!=1*2*3*4*5





# def fact(num):
#     f=1
#     for i in range(1,num+1):
#         f*=i
#     print(f)

# fact(5)





# def fact(num):
#     f = 1
#     for i in range(1, num+1):
#         f *= i
#     return f


# print(fact(64))






# def fact(num):
#     f = 1
#     for i in range(1, num+1):
#         f *= i
#     return f


# k=fact(8)/(fact(3)*fact(5))
# print(k)






def fact(num):
    f = 1
    for i in range(1, num+1):
        f *= i
    return f

def com(n,m):
    print(fact(n)/(fact(m)*fact(n-m)))
    
com(18,4)
