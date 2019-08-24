from xmlrpc.server import SimpleXMLRPCServer

def double(num):
    return num * 2

server = SimpleXMLRPCServer(('localhost', 6790))
server.register_function(double,"double")
server.serve_forever()