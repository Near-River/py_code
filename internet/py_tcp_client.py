#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import time


# TCP: Client
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the server
    s.connect(('127.0.0.1', 8888))
    print(s.recv(1024).decode('utf-8'))
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # send message
        s.send(data)
        time.sleep(1)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()
