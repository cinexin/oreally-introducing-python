from time import time, sleep

t1 = time()
num = 5
num *= 2
print(time() - t1)

t1 = time()
sleep(1.0)
print(time() - t1)
