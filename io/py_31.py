#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime


# IO 1: read & write
def writeFile():
    with open('demo.txt', 'w', encoding='utf-8') as f:
        f.write('DateTime: ')
        f.write(datetime.now().strftime('%Y-%m-%d'))


def readFile():
    with open('demo.txt', 'r', encoding='utf-8', errors='ignore') as f:
        s = f.read()
        print(s)


def readBinaryFile():
    with open('cat.jpg', 'rb') as f:
        s = f.read()
        print('open as binary data for reading...')
        print(s)


if __name__ == '__main__':
    # writeFile()
    readFile()
    # readBinaryFile()
