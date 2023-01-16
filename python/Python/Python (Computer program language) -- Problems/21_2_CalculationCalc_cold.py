import math


def calc_cold(v, t):
    return(33_((10*math.sqrt(v)-v+10.5)(33-t))/23.1)


def main():
    v = float(input('Enter v: '))
    t = float(input('Enter v: '))
    print('W is ', calc_cold(v, t))


main()
