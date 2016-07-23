#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio

__author__ = 'Nate River'


@asyncio.coroutine
def wget(host):
    print('wget %s ...' % host)
    connect = asyncio.open_connection(host=host, port=80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHOST: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        # yield from asyncio.sleep(0.01)
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body and close the socket
    writer.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['www.baidu.com', 'www.sohu.com', 'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
