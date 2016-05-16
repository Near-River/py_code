#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
from aiohttp import web

# aiohttp:
async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index Page</h1>')


async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route(method='GET', path='/', handler=index)
    app.router.add_route(method='GET', path='/hello/{name}', handler=hello)
    server = await loop.create_server(app.make_handler(), host='127.0.0.1', port=8080)
    print('Server started at http://127.0.0.1:8080...')
    return server


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()
