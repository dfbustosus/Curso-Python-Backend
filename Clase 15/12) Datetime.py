from datetime import datetime
dt= datetime.now()

print(dt)
print(dt.year)
print(dt.month)
print(dt.day)

print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)
#############################
dt= datetime(2000,1,1)
print(dt)

dt= dt.replace(year=3000)

'''
https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

%A represents the full weekday name.
%d represents the day of the month as a zero-padded decimal number.
%b represents the abbreviated month name.
%Y represents the year with century as a decimal number.
%I:%M represents the time in 12-hour format with a leading zero for the hour and minutes separated by a colon.
'''

print(dt.strftime("%A %d %b %Y %I:%M"))

dt1= datetime.now()
print(dt1.strftime("%A %d de %B del %Y- %H:%M"))

print('-----------')
from datetime import timedelta
t= timedelta(days=14, hours=14, seconds=1000)
dentro_2_semanas= dt1+t
print(dentro_2_semanas)