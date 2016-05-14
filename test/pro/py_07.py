# -*- coding: utf-8 -*-
from lib2to3.pgen2 import parse
from urllib import request
import http.cookiejar
from urllib.parse import urlencode

# 网络爬虫
# =========================================================================
# 添加特殊情景的处理器：
#   1.需要用户登录：HTTPCookieProcessor
#   2.需要代理服务器：ProxyHandler
#   3.使用https加密访问的：HTTPSHandler
#   4.url之间自动的跳转关系：HTTPRedirectHandler


cj = http.cookiejar.CookieJar()  # 创建cookie对象
cookie_support = request.build_opener(request.HTTPCookieProcessor(cj))  # 创建opener
request.install_opener(cookie_support)  # 给request安装opener
resp2 = request.urlopen('http://www.baidu.com')  # 使用带有cookie的request访问网页
# print(resp2.read().decode('utf-8'))
for cookie in cj:
    # print(cookie)
    pass

# 使用代理服务器
# proxy_support = request.ProxyHandler({'http': 'http://xx.xx.xx.xx:xx'})
# opener = request.build_opener(proxy_support, request.HTTPHandler)
# request.install_opener(opener)
#
# content = request.urlopen('http://www.baidu.com/').read().decode('utf-8')
# print(content)

# =========================================================================
# 表单的处理：post请求
# post_data = urlencode({
#     'username': 'Near',
#     'password': '123456',
# })
# print(post_data)
#
# req2 = request.Request(
#     url='http://www.verycd.com/',
#     data=post_data
# )
# content = request.urlopen(req2).read()
# print(content)

# get请求
# get_data = 'password=123456&username=Near'
# full_url = 'http://xxxxxxxxxxxxxxx/index?%s' % get_data
# req = request.Request(full_url)


# =========================================================================
# 反”反盗链”：把headers的referer改成该网站即可，
# headers = {
#     'Referer': 'http://www.cnbeta.com/articles'
# }
# 用selenium直接控制浏览器来进行站点访问，类似的还有pamie，watir，...
