import os

# Create a dir
os.mkdir('poems')
os.path.exists('poems')

# Remove a dir
os.rmdir('poems')
os.path.exists('poems')

# List contents of a dir
os.mkdir('poems')
os.listdir('poems')
os.mkdir('poems/mcintyre')
os.listdir('poems')

fout = open('poems/mcintyre/the_good_man','wt')
fout.write('''Cheerful and happy was his mood.....\'Tis sad, but such is world\'s ways.''')
fout.close()
os.listdir('poems/mcintyre')

# Change current dir with chdir()
os.chdir('poems')
os.listdir('.')

# List matching files with glob()
import glob
# Get all files that begin with 'm'
glob.glob('m*')

# Get all files with only 2 characters
glob.glob('??')

# Get all files with 8-chars that begin with m and end with e
glob.glob('m??????e')

# Get all files that begin with [a,k,l,m] end ends with e
glob.glob('[aklm]*e')