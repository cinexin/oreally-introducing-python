''' 
6.- Use multiprocessing to create three separate processes
Make each one wait a random num of secs between 1 and 5, print the current time and then exit
'''
import multiprocessing
import time
import random

def print_current_time():
    print(time.strftime("%I:%M:%S%p", time.localtime()))

if __name__ == "__main__":
    for x in range(0,3):
        p = multiprocessing.Process(target = print_current_time)
        p.start()
        time.sleep(random.randint(1,5))
        p.terminate()