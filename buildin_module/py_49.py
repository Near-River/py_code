#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import struct


# build-in: struct
# struct.pack()
print(struct.pack('>I', 10240099))  # arg 1: processing instructions
# struct.unpack()
print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

with open('dialog.bmp', 'rb') as f:
    content = f.read(30)
    print(content)
    lst = struct.unpack('<ccIIIIIIHH', content)
    print('length:', lst[2])
    print('width: ', lst[6])
    print('height: ', lst[7])
