#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Coroutine:
def costumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[COSTUMER] Costuming %s' % n)
        r = '200 OK'


def produce(c):
    n = 0
    c.send(None)    # Start generator
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s' % n)
        r = c.send(n)
        print('[COSTUMER] Returning %s' % r)
    c.close()


if __name__ == '__main__':
    c = costumer()
    produce(c)
