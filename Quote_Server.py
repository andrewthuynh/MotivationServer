#Coded by Andrew Huynh
import random
import socket
import threading

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 47650 # use one of your assigned ports instead                    
SERVER_ADDR = (SERVER_HOST, SERVER_PORT)

class HandlerThread(threading.Thread):
    """TODO write docstring!"""

    def __init__(self, client, address):
        """constructor"""
        threading.Thread.__init__(self)
        self.client = client
        self.address = address

    def run(self):
        text = open('Quotes.txt', 'r')
        info = text.read()
        quote = info.split('\n*\n')
        while True:
            client, address = connection.accept()
            client.send(k.encode())
            data = client.recv(4096).decode()
            data = data.strip()
            if data != "y":
    	        break
            else
    	        client.send(random.choice(quote).encode())

        client.shutdown(socket.SHUT_RDWR)
        client.close()
        

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connection.bind(SERVER_ADDR)
connection.listen(10)

k = "Type y for a quote\nType anything else to exit\n"

