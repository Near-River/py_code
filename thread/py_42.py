#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading

# thread 2: lock
count = 0
lock = threading.Lock()


def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


def change_it(n):
    global count
    count += n
    count -= n


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(count)
