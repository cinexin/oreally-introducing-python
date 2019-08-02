# 7.- Create a date object of your date of birth
import locale
from datetime import date
my_birthday = date(1981,5,20)

# 8.- What day of the week was your day of birth
locale.setlocale(locale.LC_TIME, 'es_es')
print(my_birthday.strftime("%A"))

# 9.- When will you be (or whn were you) 10.000 days old
from datetime import timedelta
delta = timedelta(days = 10000)
day_x = my_birthday + delta
print(day_x)