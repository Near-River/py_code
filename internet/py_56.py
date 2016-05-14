#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket


# TCP: socket
def tcp_socket():
    # create socket object: specify IP protocol type ...
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the server(server IP + port number)
    s.connect(('www.sina.com', 80))
    # send request
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

    # deal with the response
    buffer = []
    while True:
        content = s.recv(1024)
        if content:
            buffer.append(content)
        else:
            break

    # close the connection
    s.close()
    return b''.join(buffer)


if __name__ == '__main__':
    data = tcp_socket()
    header, html = data.split(b'\r\n\r\n', 1)
    # print(header.decode('utf-8'))
    # print(html.decode('utf-8'))
    with open('sina.html', 'w', encoding='utf-8') as f:
        f.write(html.decode('utf-8'))
