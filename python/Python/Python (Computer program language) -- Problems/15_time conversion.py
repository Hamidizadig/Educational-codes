fromYear =int(input('enter year from : '))
fromMonth =int(input('enter month from : '))
fromDay =int(input('enter day from : '))
untilYear =int(input('enter year until : '))
untilMonth =int(input('enter month until : '))
untilDay =int(input('enter day until : '))
if untilDay<fromDay:
    untilMonth-=1
    untilDay +=30
day=untilDay-fromDay
if untilMonth<fromMonth:
    untilYear-=1
    untilMonth +=30
month=untilMonth-fromMonth
year=untilYear-fromYear
days=day+month*30+year*36
hours=days*24
minuts=hours*60
seconds=minuts*60
print("distance time is : {0}/{1}/{2}",year,month,day)
print('Hour is (hh:mm:ss):{0}:{1}:{2}',hours,minuts,seconds)