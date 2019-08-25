'''
Do the same as exercise 1 using ZeroMQ REQ and REP sockets
'''
import zmq

host = '127.0.0.1'
port = 6789
context = zmq.Context()
server = context.socket(zmq.REP)
print ('Accepting connections on %s:%s' %(host, port))
server.bind('tcp://%s:%s' %(host, port))

request_bytes = server.recv()
request_str = request_bytes.decode('utf-8')
if (request_str == 'time'):
    print('Time command received...')
    from datetime import datetime
    response = datetime.now().isoformat().encode('utf-8')
    server.send(response)
else:
    print ('Unknown command: %s' %(request_str))    
    