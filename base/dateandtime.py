import datetime

# get the current date and time
now = datetime.datetime.now()
print(now)

# get current date
current_date = datetime.date.today()
print(current_date)

d = datetime.date(2022, 12, 25)
print(d)

timestamp = datetime.date.fromtimestamp(1326244364)
print("Date =", timestamp)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime.datetime(2022, 12, 28, 23, 55, 59, 342380)
print(b)

from datetime import datetime, date

# using date()
t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)

t3 = t1 - t2

print("t3 =", t3)
print("Type of t3 =", type(t3)) 

from datetime import timedelta

t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("Total seconds =", t.total_seconds())

#---------------------------------------------
from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("Time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

#------------------------------------------------

date_string = "25 December, 2022"
print("date_string =", date_string)

# use strptime() to create date object
date_object = datetime.strptime(date_string, "%d %B, %Y")

print("date_object =", date_object)

#----------------------------------------------

import pytz

local = datetime.now()
print("Local:", local.strftime("%m/%d/%Y, %H:%M:%S"))


tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))

#-------------------------------------------------










