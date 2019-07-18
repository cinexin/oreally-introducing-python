import os
# get current pid of Python interpeter
os.getpid()
# get current working directory
os.getcwd()
# get user id
os.getuid()
# get group id
os.getgid()

# Create a process with subprocess
import subprocess
# execute a program and get its output
ret = subprocess.getoutput('dir')
print(ret)
# get the output along with the return status
ret = subprocess.getstatusoutput('dir')
print(ret)