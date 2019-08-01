import time
now = time.time()
print(time.ctime(now))

# Using strftime() to format date times into strings....
t = time.localtime()
print(t)
format = "It's %A, %B %d, %Y, localtime %I:%M:%S%p"
print(time.strftime(format, t))

# We can also convert a string to a date or time using strptime()...
format = "%Y-%m-%d"
print(time.strptime("2012-01-29", format))