import redis
import random

conn = redis.Redis()
cats = ['siamese', 'persian', 'maine coon', 'norgwgian forest']
hats = ['stovepipe', 'bowler','tam-o-shanter','fedora']

for msg in range(10):
    cat = random.choice(cats).encode('utf-8')
    hat = random.choice(hats).encode('utf-8')
    print ('Publishing: %s wears a %s' %(cat, hat))
    conn.publish(cat, hat)
