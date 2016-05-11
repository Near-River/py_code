#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from io import StringIO, BytesIO


# IO 2: StringIO & BytesIO
def stringIO():
    # write to StringIO:
    f = StringIO()
    f.write('hello')
    f.write(' ')
    f.write('world!')
    print(f.getvalue())

    # read from StringIO:
    f = StringIO('AAA\nBBB\nCCC')
    while True:
        s = f.readline()
        if s == '':
            break
        print(s.strip())


def bytesIO():
    # write to BytesIO:
    f = BytesIO()
    f.write(b'hello')
    f.write(b' ')
    f.write(b'world!')
    print(f.getvalue())

    # read from BytesIO:
    data = 'ABCDEFG'.encode('utf-8')
    f = BytesIO(data)
    print(f.read())


if __name__ == '__main__':
    # stringIO()
    bytesIO()
