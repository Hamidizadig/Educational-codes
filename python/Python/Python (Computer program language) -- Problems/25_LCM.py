def lcm(x,y):
    if x>y:
        z=x
    else:
        z=y
    while(True):
        if(z%x==0)and(z%y==0):
            lcm=z
            break
        z+=1
    return lcm
def main():
    x=int(input('Enter x : '))
    y=int(input('Enter y : '))
    print('LCM is : ',lcm(x,y))
main()