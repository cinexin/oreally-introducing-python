import report as wr
from sources import daily, weekly

description = wr.get_description()
print("todays weather:",description)

print("Daily forecast:", daily.forecast())
print("Weekly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)
