import socket

UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
listen_addr = ("", 3386)
UDPSock.bind(listen_addr)

server_ip = None
client_ip = None
server_ports = {}
client_ports = {}

while True:
    data, addr = UDPSock.recvfrom(1024)
    data = str(data, encoding = "utf-8")
    ip_type, attr = data.split(":")
    ip = str(addr[0])
    port = str(addr[1])
    if ip_type == 'server':
        server_ip = ip
        server_ports[attr] = port
        print(addr , 'is connected as a server', attr)
    elif ip_type == 'client':
        client_ip = ip
        client_ports[attr] = port
        print(addr , 'is connected as a client', attr)
    else:
        print('Error data:', data, 'from', addr)

    if len(server_ports) > 0 and len(client_ports) > 0 :
        print('Ready to start NAT ！')
        for server_port in list(server_ports.keys()):
            for client_port in list(client_ports.keys()):
                # same port attributes
                if server_port == client_port:
                    # exchange IP & port to each other
                    data_s2c = server_ip + ":" + server_ports[server_port]
                    data_c2s = client_ip + ":" + client_ports[client_port]
                    UDPSock.sendto(data_s2c.encode("utf-8"), (client_ip, int(client_ports[client_port])))
                    UDPSock.sendto(data_c2s.encode("utf-8"), (server_ip, int(server_ports[server_port])))
                    del server_ports[server_port]
                    del client_ports[client_port]
                    print('Connect ', data_s2c, 'and', data_c2s, 'as', server_port)