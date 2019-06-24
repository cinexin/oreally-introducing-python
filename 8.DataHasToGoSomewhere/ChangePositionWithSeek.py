'''
As you read and write, Python keeps track of where you are in the file
tell() function returns your current offset from the beginning of the file, in bytes
seek() function lets you jump to another byte offset in the file
'''
fin = open('bfile','rb')
fin.tell()
fin.seek(255)
bdata = fin.read()
len(bdata)
print(bdata[0])
'''
You can call seek() with a second argument: seek(offset, origin)
If origin is 0 (default), go offset bytes from the start
If origin is 1, go offset bytes from the current position
If origin is 2, go offset bytes relative to the end

These values are also defined in the standard os module
'''
import os
print(os.SEEK_SET)
print(os.SEEK_CUR)
print(os.SEEK_END)
# So, we could have read the last byte in different ways
fin = open('bfile','rb')
fin.seek(-1,2)
fin.tell()
bdata = fin.read()
len(bdata)
bdata[0]

# Example of seeking from the current position in the file
fin = open('bfile','rb')
fin.seek(254,0)
fin.tell()
fin.seek(1,1)
fin.tell()
bdata = fin.read()
len(bdata)
print(bdata[0])