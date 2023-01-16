Employees = int(input(('Enter nomber of Employees : ')))
i = 1
while i <= Employees:
    id = int(input('Enter Id :'))
    workhour = int(input('Enter WorkHour : '))
    hourlyWage = int(input('Enter hourly wage : '))
    overtime = 0
    if workhour > 40:
        overtime = (3/2.0-1)*(workhour-40)*hourlyWage
    p = overtime+hourlyWage*workhour
    print('id= ', id, ' overtime = ', overtime, 'p= ', p)
    i = i+1
