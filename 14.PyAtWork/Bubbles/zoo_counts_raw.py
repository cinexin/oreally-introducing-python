import csv
from collections import Counter

counts = Counter()
with open('zoo.csv', 'rt') as fin:
    cin = csv.reader(fin)

    for num, row in enumerate(cin):
        # we skip the header...
        if num > 0:
            counts[row[0]] += int(row[-1])
for animal, count in counts.items():
    print("%s %s" %(animal, count))