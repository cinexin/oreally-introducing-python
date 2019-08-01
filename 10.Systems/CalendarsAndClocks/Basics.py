# CALENDARS
import calendar
calendar.isleap(1900)
calendar.isleap(1996)
calendar.isleap(2000)
calendar.isleap(2002)
calendar.isleap(2004)

import datetime
calendar.isleap(datetime.datetime.now().year)

# BASIC DATETIME
from datetime import date
halloween = date(2014,10,31)
print(halloween.day)
print(halloween.month)
print(halloween.year)
print(halloween.isoformat())

now = date.today()
print(now)

# DATETIME-DELTA OPS
from datetime import timedelta
one_day = timedelta(days = 1)
tomorrow = now + one_day
print(tomorrow)
yesterday = now - one_day
print(yesterday)

# TIME OPS
from datetime import time
noon = time(12,0,0)
print(noon.hour)
print(noon.minute)
print(noon.second)
print(noon.microsecond)
from datetime import datetime
some_day = datetime(2014,1,2,3,4,5,6)
print(some_day)
print(some_day.isoformat())
now = datetime.now()
print(now)
print(now.month)
print(now.day)
print(now.year)
print(now.minute)
print(now.second)
print(now.microsecond)

# MERGING DATE AND TIMES
from datetime import datetime, time, date
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
print(noon_today)
print(noon_today.date())
print(noon_today.time())

# USING ABSOLUTE TIME (time module)
# UNIX time counts the number of seconds since January 1st 1970
import time
# this is not the same module as "from datetime import time" 
now = time.time()
print(now)
# convert an epoch value into a string...
print(time.ctime(now))
print(time.localtime(now))
print(time.gmtime(now))
# you can also convert a struct_time object to epoch seconds
tm = time.localtime(now)
print(time.mktime(tm))
