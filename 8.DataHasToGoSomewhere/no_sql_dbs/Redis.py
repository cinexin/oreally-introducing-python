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
conn.sadd('my_zoo','duck','goat','turkey')
