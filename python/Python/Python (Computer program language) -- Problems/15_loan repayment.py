while True :
    m= int(input('Enter Amount : '))
    tedded = int(input('Enter tedded : '))
    interest = int(input('Enter Interest : '))
    totalLoan=(12*m)/(12-tedded*interest/100)
    amountInstallment=totalLoan/tedded
    print("totalLoan =" ,totalLoan,'\t',amountInstallment)
    ansi=input('do you want to continue (y,n) ?: ')
    if ansi [0] =='n':
        break