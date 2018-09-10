import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5

# def echo_server(port):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     server_addr = (host, port)
#     print('Start server at %s : %s' % (host, port))
#     sock.bind(server_addr)
#     sock.listen(backlog)
#     while True:
#         print('waiting for connect...')
#         clinet, addr = sock.accept()
#         data = clinet.recv(data_payload)
#         if data:
#             print("Data : "+data)
#             clinet.send(data)
#             print('sent %s byte back to %s' % (len(data), addr))
#         clinet.close()


def echo_server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_addr = (host, port)
    print('Start server at %s : %s' % (host, port))
    sock.bind(server_addr)
    print('waiting for connect...')
    while True:
        data, addr = sock.recvfrom(data_payload)
        if data:
            print("Data : " + data.decode('utf-8'))
            sock.sendto(data, addr)
            print('sent %s byte back to %s' % (len(data), addr))
    sock.close()


if __name__ == '__main__':
    echo_server(8002)