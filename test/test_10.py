# -*- coding: utf-8 -*-
import threading, time
from queue import Queue
from threading import Thread


# 模拟多线程并发抓取
# q是任务队列    NUM是并发线程总数  JOBS是任务数
q, NUM, JOBS = Queue(), 3, 10


# 具体处理函数，负责处理单个任务
def do_somthing(arguments):
    print('current thread %s: ' % threading.current_thread().name, arguments)


# 工作进程，负责不断从队列中取数据并处理
def working():
    while True:
        arguments = q.get()
        do_somthing(arguments)
        time.sleep(1)
        q.task_done()

# fork NUM个线程等待队列
for i in range(NUM):
    t = Thread(target=working)
    t.setDaemon(True)  # 设置为守护线程
    t.start()

# 把JOBS排入队列
for i in range(JOBS):
    q.put('Job：%d' % (i + 1))

# 等待所有JOBS完成
q.join()  # join()：Blocks until all items in the Queue have been gotten and processed.
