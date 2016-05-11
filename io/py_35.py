#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json


# pickling: JSON
d = dict(id='s001', name='Jack', age=21)
print(d)
pd = json.dumps(d)
print('Json Str: ', pd)
nd = json.loads(pd)
print(nd)
print(id(d) == id(nd))


with open('json.txt', 'w', encoding='utf-8') as f:
    json.dump(d, f)

with open('json.txt', 'r', encoding='utf-8') as f:
    nd = json.load(f)
    print(nd)
