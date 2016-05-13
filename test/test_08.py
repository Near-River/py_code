# -*- coding: utf-8 -*-
import os
import re
import urllib.request

# 简单的网络爬虫
url = 'http://tieba.baidu.com/p/3002502381'
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
html = resp.read()
# print(html)

pattern = re.compile(r'<img [\s\S]+?src="(http:[\s\S]+?)"')
url_list = re.findall(pattern, str(html))
print(len(url_list))
i = 1
for url in url_list:
    # print(url)
    img_path = os.path.join('D:/demo/imgs/', '%d.jpg' % i)
    # urllib.request.urlretrieve(url, img_path)  # 远程下载
    i += 1
