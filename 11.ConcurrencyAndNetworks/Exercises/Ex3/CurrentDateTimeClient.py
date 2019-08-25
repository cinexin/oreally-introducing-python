import xmlrpc.client

host = 'localhost'
port = 6789
proxy = xmlrpc.client.ServerProxy('http://%s:%s/' %(host, port))
result = proxy.current_date_time()
print('Current date time is %s' %(result))