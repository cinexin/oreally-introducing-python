'''
Use a plain socket to implement a current-time service. 
When a client sends the string time to the server, return the current date time as ISO string
'''
import socket

host = 'localhost'
port = 6789

address = (host,port)
max_size = 1000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
print('Accepting connections on %s:%s' %(host, port))
server.listen()

(client, addr) = server.accept()

data = client.recv(max_size)

if (data == 'time'.encode('utf-8')):
    print('Time command received...')
    from datetime import datetime
    response = datetime.now().isoformat().encode('utf-8')
    client.sendall(response)
else:
    print('Unknown command: %s' %data)
    
client.close()
server.close()
