import csv
villains = [['Doctor','No'],['Rosa', 'Klebb'],['Mister', 'Big'],['Auric', 'Goldfinger'],['Ernst','Blofeld']]
with open('villains','wt', newline = '') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)
    
with open('villains','rt') as fin:
    cin = csv.reader(fin)
    for row in cin:
        print(row)
    villains = [row for row in cin]
    print(villains)
    
'''
Data can be a list of dictionaries instead a list of lists
'''
import csv
with open('villains','rt') as fin:
    cin = csv.DictReader(fin,fieldnames=['first','last'])
    villains = [row for row in cin]
    print(villains)
    
# Let's rewrite the CSV using dictionaries
villains = [
    {'first': 'Doctor', 'last': 'No'},
    {'first': 'Rosa', 'last': 'Klebb'},
    {'first': 'Mister', 'last': 'Big'},
    {'first': 'Auric', 'last': 'Goldfinger'},
    {'first': 'Ernst', 'last': 'Blofeld'},
]
with open('villains', 'wt', newline = '') as fout:
    cout = csv.DictWriter(fout,['first','last'])
    cout.writeheader()
    cout.writerows(villains)
'''
Now, let's read it back
By omitting fieldnames arguments in the DictReader() call, 
we instruct to use the values in the first line of the file (first, last) as column labels
and matching dictionary keys
'''
with open('villains','rt') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]
print(villains)