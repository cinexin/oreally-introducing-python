# 2.- Read the text file today.txt into the string today_string
fin = open('today.txt','rt')
today_string = fin.read().strip()
fin.close()

# 3.- Parse the date from today_string
import time
format = "%Y-%m-%d"
print(time.strptime(today_string, format))