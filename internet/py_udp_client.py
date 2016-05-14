#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import time


# UDP: Client
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # send message
        s.sendto(data, ('127.0.0.1', 8888))
        time.sleep(1)
        print(s.recv(1024).decode('utf-8'))
    s.close()
