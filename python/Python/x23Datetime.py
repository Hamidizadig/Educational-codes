from datetime import date, time, datetime, timedelta
import pytz
from khayyam import *

date1 = JalaliDate(1363, 11, 9)
print(date1)

datetime1 = JalaliDatetime(1358, 5, 15, 7, 34, 26)
print(datetime1)

datetime2 = JalaliDatetime.now()
print(datetime2)
Gdate1 = datetime1.todate()
Gdate2 = datetime2.todate()
print(Gdate1)
print(Gdate2)

# print(date1)

#

'''date2=JalaliDatetime.now()
print(date2)
###############'''
# date1=datetime(1985,1,29,6,0)
# date2=datetime(2022,7,20,18,0)
# daydiff=abs(date2-date1)
# daydiff=abs(date2-date1).total_seconds()
# mindiff=abs(date2-date1).total_seconds()-60
# hourdiff=abs(date2-date1).total_seconds()/(60*60)
# daydiff=abs(date2-date1).total_seconds()/(24*60*60)
# print(daydiff)
# print(daydiff)
# print(mindiff)
# print(hourdiff)
# print(daydiff)

# date1=datetime(2012,4,14,2,45)
# date2=datetime(2020,9,1,5,35)
# timedelta1=timedelta(days=1,hours=5,minutes=14,seconds=20)
# date3=date1+timedelta1
# print(date1)
# print(date3)

# print(datetime.now())
# print(datetime.utcnow())
# print(datetime.now(pytz.timezone('asia/Tehran')))

# print(date.today())
# print(datetime.now())
# date1=date(1985,1,29)
# print(date1)
# time1=time(23,23,56)
# print(time1)

# datetime1=datetime(2101,8,19,5,48,59,487494)
# print(datetime1)
# print(datetime1.year)
# print(datetime1.microsecond)
# print(datetime.now())
# print(datetime.utcnow())
# print(datetime.now())
# print(datetime.now().strftime("%Y-%m-%D %H:%M:%S"))
# date3=datetime.strptime("8/18/2012","%m/%d/%Y")
# print(date3.year)
# print(date3.month)
# print(date3.day)
# date3=datetime.strptime("1990-8-25 20:12:45" ,"%Y-%m-%d %H:%M:%S")
# print(date3.year)
# print(date3.month)
# print(date3.day)
# print(date3.hour)
# print(date3.minute)
# print(date3.second)
