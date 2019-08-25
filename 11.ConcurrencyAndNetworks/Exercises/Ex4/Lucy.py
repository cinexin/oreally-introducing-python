import redis
from time import sleep

conn = redis.Redis()
timeout = 10
topic = 'chocolate'
sub = conn.pubsub()
sub.subscribe(topic)

remaining = 1
while remaining > 0:
    sleep(0.5)
    msg = conn.blpop(topic, timeout)
    remaining = conn.llen(topic)
    if msg:
        chocolate = msg[1]
        print ('Lucy got a piece of %s. Reamining: %s' %(chocolate, remaining))