#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, time, random
from multiprocessing import Pool


# process Pool:
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def createPool():
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()   # Prohibit of adding process to the Pool
    p.join()
    print('All subprocesses done.')


if __name__ == '__main__':
    createPool()



