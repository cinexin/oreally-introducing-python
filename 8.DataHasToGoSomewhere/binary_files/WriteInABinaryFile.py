bfile='8.DataHasToGoSomewhere/binary_files/bfile'

bdata = bytes(range(0,256))
len(bdata)
fout = open(bfile,'wb')
fout.write(bdata)
fout.close()

'''
As with text, you can write binary data in chunks
'''
fout = open(bfile,'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk
fout.close()

'''
Read binary file with read
'''
fin = open(bfile,'rb')
bdata = fin.read()
len(bdata)
fin.close()