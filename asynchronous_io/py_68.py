#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import threading


# asyncio: syntax for 3.5
async def hello(name):
    print('hello, %s. %s' % (name, threading.current_thread().name))
    # call another coroutine
    await asyncio.sleep(1)
    print('hello, %s. %s' % (name, threading.current_thread().name))


if __name__ == '__main__':
    # achieve the EventLoop object
    loop = asyncio.get_event_loop()
    # execute coroutines
    tasks = [hello('jack'), hello('king')]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
