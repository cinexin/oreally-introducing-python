import socket

host = 'localhost'
port = 6789
address = (host, port)
max_size = 1000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)

command = 'time'.encode('utf-8')
client.sendall(command)
data = client.recv(max_size)
print('Current datetime: %s' %(data.decode('utf-8')))
client.close()
