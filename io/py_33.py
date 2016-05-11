#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from datetime import datetime


# IO 3: Manipulating files and directories
print(os.name)
# print(os.environ.get('PATH'))
print(os.path.abspath('.'))

print(os.path.join('/Users/tempdir/', 'file.txt'))
print(os.path.split('/Users/tempdir/file.txt')[1])
print(os.path.splitext('/Users/tempdir/file.txt')[1])

print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

for f in os.listdir(os.path.abspath('.')):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
