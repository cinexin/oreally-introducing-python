# Write the current date as string to the text file today.txt
from datetime import date
now = date.today()
print(now.isoformat())

fout = open('today.txt','wt')
print(now.isoformat(), file = fout)
fout.close()
