'''
Be careful with reading the whole file with large files
It can consume sooooo much RAM
'''
relativityFile='8.DataHasToGoSomewhere/text_files/relativity'
fin = open(relativityFile,'rt')
poem = fin.read()
fin.close()
print(poem)

'''
Better read by chunks
'''
poem = ''
fin = open(relativityFile,'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment
print(poem)
fin.close()

'''
Or read by lines...
'''
poem = ''
fin = open(relativityFile, 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
print(poem)
fin.close()

'''
And there's even a better (and shorter) way
line by line
'''
poem = ''
fin = open(relativityFile,'rt')
for line in fin:
    poem += line
print(poem)
fin.close()

'''
You can even save the lines into a list
'''
fin = open(relativityFile,'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')
for line in lines:
    print(line, end = '')
    