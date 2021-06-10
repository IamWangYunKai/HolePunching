import socket
import threading
from time import sleep

server_main_address = ('', 6666)
server_assist_address = ('', 7777)

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
main_socket.bind(server_main_address)

assist_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
assist_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
assist_socket.bind(server_assist_address)

def handle_assist_tcp(client_sock, client_addr):
    print('client_addr:', client_addr)
    while True:
        recv_data = client_sock.recv(65535)
        if len(recv_data) > 0:
            print('Data:', recv_data.decode())
            client_sock.send('Get AAA'.encode())
        else:
            sleep(0.001)
            client_sock.close()
            break

def handle_main_tcp(client_sock, client_addr):
    print('client_addr:', client_addr)
    while True:
        recv_data = client_sock.recv(65535)
        if len(recv_data) > 0:
            print('Data:', recv_data.decode())
            client_sock.send('Get AAA'.encode())
        else:
            sleep(0.001)
            client_sock.close()
            break


while True:
    assist_socket.listen()
    main_socket.listen()
    client_sock, client_addr = assist_socket.accept()
    recv_thread = threading.Thread(target = handle_assist_tcp, args=(client_sock, client_addr))
    recv_thread.start()

    client_sock, client_addr = main_socket.accept()
    recv_thread = threading.Thread(target = handle_main_tcp, args=(client_sock, client_addr))
    recv_thread.start()

assist_socket.close()