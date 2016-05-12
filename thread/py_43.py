#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading


# thread: LocalThread
local_thread = threading.local()


def run(name):
    local_thread.student = name
    process()


def process():
    print('thread %s has student name: %s' % (threading.current_thread().name, local_thread.student))


t1 = threading.Thread(target=run, args=('King',))
t2 = threading.Thread(target=run, args=('Jack',))
t1.start()
t2.start()
t1.join()
t2.join()
