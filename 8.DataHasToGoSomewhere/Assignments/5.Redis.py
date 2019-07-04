''' 8.11 Create a Redis hash called test with the fields count (1) and name ('Fester Bestertester)'''
import redis
conn = redis.Redis()
conn.delete('test')
conn.keys('*')
conn.hmset('test',{'name':'Fester Bestertester','count':1})
conn.hkeys('test')
conn.hvals('test')
conn.hgetall('test')
conn.hincrby('test','count', 70)
conn.hgetall('test')