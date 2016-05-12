#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from multiprocessing import Process


# process: creation
def createProcess():  # Only works on Unix/Linux/Mac:
    print('Process (%s) start...' % os.getpid())
    pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:   # return the subprocess id
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


def run_process(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def createProcess2():  # Works on Windows
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_process, args=('demo_process',))
    print('Child process start.')
    p.start()
    p.join()
    print('Child process end.')


if __name__ == '__main__':
    createProcess2()
