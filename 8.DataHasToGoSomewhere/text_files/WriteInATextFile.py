poem = """There was a young lady named Bright,
Whose speed was faster than light;
She started one day
In a relative way,
And returned on the previous night."""
len(poem)

relativityFile='8.DataHasToGoSomewhere/text_files/relativity'

# Open a file in "write" "text" mode
# Then write
fout = open(relativityFile,"wt")
fout.write(poem)
fout.close()

# Open a file in "write" "text" mode
# Then print
fout = open(relativityFile,"wt")
print(poem,file=fout)
fout.close()
'''Take into account print adds a space 
after each argument and a newline at the end
To avoid this and make print work exactly like write...
'''
fout = open(relativityFile, "wt")
print(poem, file = fout, sep='', end='')
fout.close()

# Write chunks...
fout = open(relativityFile, "wt")
file_len = len(poem)
offset = 0
chunk = 100
while True:
    if offset > file_len:
        break
    fout.write(poem[offset:offset + chunk])
    offset += chunk
fout.close()

'''
Opening in "x" mode
'x' is for exclusive creation
so it fails if file already exists
'''
try:
    fout = open(relativityFile,'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity file already exists!')
