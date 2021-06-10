import socket
from threading import Thread
from time import sleep
 
UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data = 'server:cmd'.encode("utf-8")
message = 'server'
# the public IP server
addr = ("47.100.46.11", 3386)

ip = ""
port = 0

# send UDP package to another computer
def send():
    while True:
        print('Send ' , message ,'to ', ip, ':', port)
        UDPSock.sendto(message.encode("utf-8"), (ip, port))
        sleep(0.2)

# receive UDP package from another computer
def recv():
	while True:
	    data, adr = UDPSock.recvfrom(1024)
	    print('Recv' , data , 'from' ,adr)

# ask the public IP server for another computer IP
UDPSock.sendto(data, addr)
address = UDPSock.getsockname()

# receive another computer IP from the public IP server
dest = ''
while len(dest) < 1:
	dest,adr = UDPSock.recvfrom(1024)

dest = str(dest, encoding = "utf-8")
try:
	ip = dest.split(':')[0]
	port = int(dest.split(':')[1])
	print('Get IP/port', ip, port, 'from', addr)
except:
	print('Error', dest)

send_thread = Thread(target = send, args = ())
send_thread.start()
sleep(0.5)

recv_thread = Thread(target = recv, args = ())
recv_thread.start()
