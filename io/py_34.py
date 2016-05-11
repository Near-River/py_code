#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle


# pickling: pickle
d = dict(id='s001', name='Jack', age=21)
print(d)
pd = pickle.dumps(d)
print(pd)
nd = pickle.loads(pd)
print(nd)
print(id(d) == id(nd))


with open('pickle.txt', 'wb') as f:
    pickle.dump(d, f)

with open('pickle.txt', 'rb') as f:
    nd = pickle.load(f)
    print(nd)
