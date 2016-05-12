#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time, queue
from multiprocessing.managers import BaseManager


# Distributed Process: Worker
class QueueManager(BaseManager):
    pass


def work():
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')
    # connect to the master(server)
    server_addr = '127.0.0.1'
    print('Connect to server %s...' % server_addr)
    worker = QueueManager(address=(server_addr, 5000), authkey=b'admin')
    worker.connect()
    task = worker.get_task_queue()
    result = worker.get_result_queue()
    # do calculate job
    for i in range(10):
        try:
            n = task.get(i)
            r = '%d * %d = %d' % (n, n, n * n)
            time.sleep(1)
            result.put(r)
        except queue.Empty:
            print('task queue is empty.')


if __name__ == '__main__':
    work()
