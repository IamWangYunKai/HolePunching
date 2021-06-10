import socket
from time import sleep

server_main_address = ('127.0.0.1', 6666)#('47.97.208.144', 7070)
server_assist_address = ('127.0.0.1', 7777)#('47.97.208.144', 8080)

# main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# main_socket.connect(server_main_address)

assist_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
assist_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
assist_socket.connect(server_assist_address)

# step 3
while True:
    assist_socket.send('BBB'.encode())
    sleep(1)
