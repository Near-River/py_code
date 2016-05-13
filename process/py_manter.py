#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import queue, random
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# Distributed Process: Master
task_queue = queue.Queue()  # the queue used to send task
result_queue = queue.Queue()  # the queue used to accept result


class QueueManager(BaseManager):
    pass


def get_task_queue():
    return task_queue


def get_result_queue():
    return result_queue


def run():
    # QueueManager.register('get_task_queue', callable=lambda :task_queue)
    # QueueManager.register('get_result_queue', callable=lambda: result_queue)
    QueueManager.register('get_task_queue', callable=get_task_queue)
    QueueManager.register('get_result_queue', callable=get_result_queue)

    # binding the address and specify the authentication key
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'admin')
    manager.start()
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    print('Try get results...')

    for i in range(10):
        try:
            r = result.get(timeout=10)
            print('Result: %s' % r)
        except queue.Empty:
            print('Empty queue')

    manager.shutdown()
    print('master exit.')


if __name__ == '__main__':
    freeze_support()
    run()
