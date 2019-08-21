import gevent
from gevent import socket
hosts = ['www.crappytaxidermy.com','www.walterpottertaxidermy.com','www.houseoftaxidermy.com']
'''
spawn() method of gevent creates a "green thread" or "microthread"
each thread executes separately gevent.socket.gethostbyname(url)
'''
jobs = [gevent.spawn(gevent.socket.gethostbyname,host) for host in hosts]
'''
the gevent.joinall() method waits for all the spawned jobs (green threads) to finish
'''
gevent.joinall(jobs,timeout = 5)
for job in jobs:
    print(job.value)