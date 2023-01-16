def calc_f(m1,m2,d):
    g=6.673e-8
    return(g*m1*m2/pow(d))
def pow (d):
    return(d*d)
def main():
    m1=float(input('Enter m1 :'))
    m2=float(input('Enter m2 :'))
    d=float(input('Enter d :'))
    print('F is ',calc_f(m1,m2,d))
main()