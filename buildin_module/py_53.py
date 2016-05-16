#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request, parse


# build-in: urllib
def get():
    with request.urlopen('https://api.douban.com/v2/book/2129653') as resp:
        print('Status:', resp.status, resp.reason)
        for k, v in resp.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', resp.read().decode('utf-8'))


# Imitate browser(Phone) to sends a GET request
def imitate_get():  # Request
    req = request.Request('http://www.douban.com')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as resp:
        print('Status:', resp.status, resp.reason)
        for k, v in resp.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', resp.read().decode('utf-8'))


def post():
    print('Login to weibo')
    # username = input('Email: ')
    # password = input('Password: ')
    username = input('Phone: ')
    password = input('password: ')
    login_data = parse.urlencode([
        ('username', username),
        ('password', password),
        ('savestate', '1'),
        ('ec', ''),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('pagerefer', '')
    ])

    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0')
    req.add_header('Referer',  'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=5399_0013&r=http%3A%2F%2Fm.weibo.cn%2Fm.weibo.cn')

    with request.urlopen(req, data=login_data.encode()) as resp:
        print('Status:', resp.status, resp.reason)
        for k, v in resp.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', resp.read().decode('utf-8'))


def proxy():
    proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:6666/'})
    proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
    proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
    opener = request.build_opener(proxy_handler, proxy_auth_handler)
    with opener.open('http://www.example.com/login.html') as f:
        pass


if __name__ == '__main__':
    # get()
    # imitate_get()
    post()
    # proxy()
