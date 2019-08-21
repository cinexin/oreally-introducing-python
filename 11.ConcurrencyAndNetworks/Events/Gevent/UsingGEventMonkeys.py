import gevent
from gevent import monkey
'''
This makes as many gevent speedups as possible
That is, when you want gevent to be applñied all the way down
'''
monkey.patch_all()
import socket
hosts = ['www.crappytaxidermy.com','www.walterpottertaxidermy.com','www.houseoftaxidermy.com']
jobs = [gevent.spawn(socket.gethostbyname,host) for host in hosts]
gevent.joinall(jobs, timeout = 5)
for job in jobs:
    print(job.value)
