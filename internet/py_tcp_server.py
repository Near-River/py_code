#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
from threading import Thread


# TCP: Server
def serve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # binding a port
    s.bind(('127.0.0.1', 8888))
    # listen port
    s.listen(5)  # specify the maximum number of connection
    while True:
        # accept a new connection
        sock, addr = s.accept()
        t = Thread(tcp_link(sock, addr))
        t.start()
    # close the connection
    s.close()


def tcp_link(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'welcome!')
    while True:
        content = sock.recv(1024)
        if not content or content.decode('utf-8') == 'exit':
            break
        sock.send(('hello: %s' % content.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


if __name__ == '__main__':
    serve()
