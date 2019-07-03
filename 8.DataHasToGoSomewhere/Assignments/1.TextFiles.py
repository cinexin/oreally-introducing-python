'''
8.1. Assign the string 'This is a test of the emergency text system to test1
Write test1 in a file called test.txt
'''
test1 = 'This is a test of the emergency text system'
testFile = '8.DataHasToGoSomewhere/Assignments/test.txt'
with open(testFile,'wt') as fout:
    fout.write(test1)

'''
8.2. Open the file test.txt and read its contents into the string test2
'''
with open(testFile,'rt') as fin:
    test2 = fin.read()
test1 == test2