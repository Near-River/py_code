#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools, time


# build-in: itertools
def test_count():
    natures = itertools.count(1)
    for i in natures:
        print(i)
        time.sleep(1)


def test_cycle():
    c = itertools.cycle('ABC')
    for i in c:
        print(i)
        time.sleep(1)


def test_repeat():
    r = itertools.repeat('ABC', 3)
    for i in r:
        print(i)
        time.sleep(1)


def test_chain():
    r = itertools.chain('ABC', 'XYZ')
    for i in r:
        print(i)


def test_groupby():
    groups = itertools.groupby('AaBCcdefGGg', lambda x: x.upper())
    for key, group in groups:
        print(key, list(group))


if __name__ == '__main__':
    test_count()
    # test_cycle()
    # test_repeat()
    # test_chain()
    # test_groupby()
    c = itertools.takewhile(lambda x: x <= 10, itertools.count(1))
    for i in c:
        print(i)
