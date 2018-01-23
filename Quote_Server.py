import random
import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 47650 # use one of your assigned ports instead                    
SERVER_ADDR = (SERVER_HOST, SERVER_PORT)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connection.bind(SERVER_ADDR)
connection.listen(10)

k = "Type y for a quote\nType anything else to exit\n"

text = open('Quotes.txt', 'r')
info = text.read()
quote = info.split('\n*\n')

client, address = connection.accept()
while True:
    client.send(k.encode())
    data = client.recv(4096).decode()
    data = data.strip()
    if data != "y":
    	break
    else
    	client.send(random.choice(quote).encode())
        
client.shutdown(socket.SHUT_RDWR)
client.close()
