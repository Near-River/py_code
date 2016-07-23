#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket


# UDP: Server
def serve():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # binding a port
    s.bind(('127.0.0.1', 8888))
    print('Bind UDP on 8888...')
    udp_link(s)
    s.close()


def udp_link(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        print('Receive data: %s from %s' % (data.decode('utf-8'), addr))
        sock.sendto(b'Hello, %s' % data, addr)


if __name__ == '__main__':
    serve()
