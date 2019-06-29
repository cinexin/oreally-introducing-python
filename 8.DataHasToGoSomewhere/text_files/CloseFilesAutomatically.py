poem = """There was a young lady named Bright,
Whose speed was faster than light;
She started one day
In a relative way,
And returned on the previous night."""

relativityFile='8.DataHasToGoSomewhere/text_files/relativity'

with open(relativityFile,'wt') as fout:
    fout.write(poem)
# After the block, file will be automatically closed