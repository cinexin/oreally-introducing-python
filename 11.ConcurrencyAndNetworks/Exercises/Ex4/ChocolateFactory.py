'''
Write a simulation that pushes different types of chocolates to a Redis list
Lucy (the client) will receive the chocolates
'''
# Server Side: Chocolate factory
import redis
import random

conn = redis.Redis()
chocolate_topic = 'chocolate'
chocolate_types = ['black', 'white', 'milked', 'semi-sweet']

for i in range(20):
    chocolate = random.choice(chocolate_types)
    print ('Delivering %s chocolate' %(chocolate))
    conn.rpush(chocolate_topic, chocolate)
