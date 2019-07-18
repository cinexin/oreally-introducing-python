fout = open('ooops.txt','wt')
print('Oops, I created a file', file = fout)
fout.close()

import os
os.path.exists('oops.txt')
os.path.exists('./oops.txt')
os.path.exists('waffles')
os.path.exists('.')
os.path.exists('..')

file_name = 'oops.txt'
os.path.isfile(file_name)
os.path.isdir(file_name)
os.path.isdir('.')

os.path.isabs(file_name)
os.path.isabs('/big/fake/name')
os.path.isabs('big/fake/name/without/a/leading/slash')

# Copy files
import shutil
shutil.copy('ooops.txt','ohno.txt')

# Rename files
os.rename('ohno.txt','ohwell.txt')

# Making links or symlinks()
# Make a hard link...
os.link('ooops.txt','yikes.txt')
os.path.isfile('yikes.txt')

# Make a sym link
os.path.islink('yikes.txt')
os.symlink('ooops.txt','jeepers.txt')
os.path.islink('jeepers.txt')

# Changing permissions
os.chmod('ooops.txt',0o400)
import stat
os.chmod('ooops.txt', stat.S_IRUSR)

# Get pathname with abspath()
os.path.abspath('ooops.txt')

# Get symlink pathname with realpath
os.path.realpath('jeepers.txt')

# Delete a file with remove()
os.remove('ooops.txt')