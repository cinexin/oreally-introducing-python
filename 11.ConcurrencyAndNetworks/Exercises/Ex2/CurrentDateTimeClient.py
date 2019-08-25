import zmq

host = '127.0.0.1'
port = 6789
context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect('tcp://%s:%s' %(host,port))

command = 'time'
request_bytes = command.encode('utf-8')
client.send(request_bytes)
response = client.recv().decode('utf-8')
print('Current time is %s' %(response))