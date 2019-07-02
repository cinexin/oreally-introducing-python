import redis
# this is the default
# the same would be:
# redis.Redis('localhost')
# or: redis.Redis('localhost',6379)
conn = redis.Redis()
# list all keys
conn.keys('*')
conn.set('secret','ni!')
conn.set('carats',24)
conn.set('fever','101.5')
conn.keys('*')
conn.get('secret')
conn.get('carats')
conn.get('fever')

# the setnx() method sets a value only if the key does not exist
conn.setnx('secret','icky-icky-icky-ptang-zoop-boing!')
conn.get('secret')

# the getset() method returns the old value and sets it to a new one at the same time
conn.getset('secret','icky-icky-icky-ptang-zoop-boing!')
conn.get('secret')

# get a substring by using getrange()
# remember: offset 0 = start, -1: end
conn.getrange('secret',-6,-1)

# Replace a substring by using setrange() (using a zero-based offset)
conn.setrange('secret',0,'ICKY')
conn.get('secret')

# Set multiple keys at once
conn.mset({'pie':'cherry','cordial':'sherry'})

# Get multiple keys at once
conn.mget(['fever','carats'])

# Delete a key with delete()
conn.delete('fever')

# Increment by using incr() incrbyfloat() commands
# There's no substract for float operation, negative values do the trick
conn.incr('carats')
conn.incr('carats',10)
conn.decr('carats')
conn.decr('carats',15)
conn.set('fever','101.5')
conn.incrbyfloat('fever')

# REDIS LISTS
conn.lpush('zoo','bear')
conn.lpush('zoo','alligator')
conn.lpush('zoo','duck')
conn.linsert('zoo','before','bear','beaver')
conn.linsert('zoo','after','bear','cassowary')
conn.lset('zoo',2,'marmoset')
conn.rpush('zoo','yak')
conn.lindex('zoo',3)
conn.lrange('zoo',0,2)
conn.ltrim('zoo',1,4)
print(conn.lrange('zoo',0,2))
conn.lrange('zoo',0,-1)

# REDIS HASHES
conn.hmset('song',{'do':'a dder','re':'about a deer'})
conn.hset('song','mi','a note to follow re')
conn.hget('song','mi')
conn.hmget('song','re','do')
conn.hkeys('song')
conn.hvals('song')
conn.hlen('song')
conn.hgetall('song')
conn.hsetnx('song','fa','a note that rhymes with la')

# REDIS SETS
# Add elements to a set
conn.sadd('my_zoo','duck','goat','turkey')
# get number of elements of a set
conn.scard('my_zoo')
# get all the set's values
conn.smembers('my_zoo')
# remove a value from the set
conn.srem('my_zoo','turkey')
conn.sadd('better_zoo','tiger','wolf','duck')
# intersection of 2 sets
conn.sinter('my_zoo','better_zoo')
# store the intersection in another set (fowl_zoo)
conn.sinterstore('fowl_zoo','my_zoo','better_zoo')
conn.smembers('fowl_zoo')
# union of 2 stes
conn.sunion('my_zoo','better_zoo')
# store the union in another set (fabolous_zoo)
conn.sunionstore('fabulous_zoo','my_zoo','better_zoo')
conn.smembers('fabulous_zoo')
# get the diff of 2 sets (what does my_zoo have that better_zoo doesn't have?)
conn.sdiff('my_zoo','better_zoo')
conn.sdiffstore('zoo_sale','my_zoo','better_zoo')
conn.smembers('zoo_sale')

# SORTED SETS
'''
Sorted sets (or zsets) are sets of unique values, 
each value having an associated floating point score
You can access each item by its value or score
Sorted sets have manu uses:
- Leader boards
- Secondary indexes
- Timeseries, using timestamps as scores
We'll se the last use case, tracking user logins via timestamps
(Unix epoc value)
'''
import time
now = time.time()
print(now)

# first guest...
conn.zadd('logins',{'smeagol':now})
# 5 minutes later, next guest...
conn.zadd('logins',{'sauron':now + (5*60)})
# 2 hours later, another guest...
conn.zadd('logins',{'bilbo': now + (2*60*60)})
# one day later, the last guest...
conn.zadd('logins',{'treebeard': now + (24*60*60)})
# in what order bilbo arrived?
conn.zrank('logins','bilbo')
# when was that?
conn.zscore('logins','bilbo')
conn.zrange('logins',0,-1)
conn.zrange('logins',0,-1,withscores=True)

# BITS
# let's say we want to track who visited our website in an specifi range of dates...
days = ['2013-02-25','2013-02-26','2013-02-27']
# let's say these are user ids visiting our website in the above days
big_spender = 1089
tire_kicker = 40459
late_joiner = 550212
# with bits, we can mark who visited our website on an specific day
# let's say, the first date or days "big_spender" and "tire_kicker" hit our website...
conn.setbit(days[0],big_spender,1)
conn.setbit(days[0],tire_kicker,1)
# the next day, "big_spender" came back...
conn.setbit(days[1],big_spender,1)
# the last day, "big_spender" came back again, and a new user too
conn.setbit(days[2],big_spender,1)
conn.setbit(days[2],late_joiner,1)
# Let's get the daily visitor count for these 3 days...
# not working in my local redis server...(ouch!)
for day in days:
    print(day)
    conn.bitcount(day)

conn.getbit(days[1],tire_kicker)

# CACHE AND EXPIRATION
# We can use the expire() function to instruct Redis how long to keep the key
# by default, it keeps the key forever
# the expiration value is a number of seconds
import time
key = 'now you see it'
conn.set(key,'but not for long')
conn.expire(key,5)
conn.ttl(key)
conn.get(key)
time.sleep(6)
conn.get(key)