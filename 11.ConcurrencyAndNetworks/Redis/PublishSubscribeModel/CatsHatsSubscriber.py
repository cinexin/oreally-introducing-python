import redis

conn = redis.Redis()
topics = ['maine coon', 'siamese']
sub = conn.pubsub()
sub.subscribe(topics)

for msg in sub.listen():
    if msg['type'] == 'message':
        cat = msg['channel'].decode('utf-8')
        hat = msg['data'].decode('utf-8')
        print ('Subscriber gets: %s wears a %s' %(cat, hat))