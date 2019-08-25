'''
Do the same as Ex1 with XMLRPC system
'''
from xmlrpc.server import SimpleXMLRPCServer

def current_date_time():
    print ('Current date time request received...')
    from datetime import datetime
    return datetime.now().isoformat()

host = 'localhost'
port = 6789
print ('Accepting connections on %s:%s' %(host, port))
server = SimpleXMLRPCServer((host, port))
server.register_function(current_date_time,"current_date_time")
server.serve_forever()