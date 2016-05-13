#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re


# regex: match
test = '0512-88228866'
m = re.match(r'\d{4}\-\d{6,8}', test)
if m:
    print('ok')
else:
    print('failed')


# split()
print(re.split(r'[\s,]+', 'a,b,  c    d'))


# Match.group() / groups()
m = re.match(r'^(\d{4})\-(\d{6,8})$', test)
print(m.group(0))
print(m.group(1), m.group(2))
print(m.groups())
print(m.span())  # return: (start(group), end(group))
print(m.expand(r'\2 \1'))


# search & findall
s = 'aa123 bb456 cc789'
p = r'[0-9]+'
print(re.search(p, s).group(0))
print(re.findall(p, s))
