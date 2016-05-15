#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server


# WSGI: web server gateway interface
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


if __name__ == '__main__':
    http_server = make_server(host='127.0.0.1', port=8888, app=application)
    print('Serving HTTP on port 8888...')

    http_server.serve_forever()
