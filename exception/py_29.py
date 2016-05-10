#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import pdb


# debugging: assert & logging & pdb
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('0')

# main()


logging.basicConfig(level=logging.DEBUG)     # configure the logging level

s = '0'
n = int(s)
logging.debug('n = %d' % n)
pdb.set_trace()
print(10 / n)
