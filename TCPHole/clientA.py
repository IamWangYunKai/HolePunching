import socket
import threading
from time import sleep

local_mode = False
if local_mode:
    server_main_address = ('127.0.0.1', 6666)
    server_assist_address = ('127.0.0.1', 7777)
else:
    server_main_address = ('47.97.208.144', 6666)
    server_assist_address = ('47.97.208.144', 7777)

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.connect(server_main_address)

assist_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
assist_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
assist_socket.connect(server_assist_address)

def handle_tcp():
    while True:
        recv_data = assist_socket.recv(65535)
        if len(recv_data) > 0:
            print('Data:', recv_data.decode())
        else:
            sleep(0.001)
            assist_socket.close()
            print('Close socket')
            break

# step 3
assist_socket.send('AAA'.encode())
recv_thread = threading.Thread(target = handle_tcp, args=())
recv_thread.start()
# step 4