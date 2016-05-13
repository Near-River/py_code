#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re


# regex: match
t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())


s = 'aa123 bb456 cc789'
# compile: return an Regex Expression object
s_pattern = re.compile(r'[0-9]+')
# substitute
ns = re.sub(s_pattern, '999', s)
print(ns)


print(re.match(r'^(\d+)(0*)$', '102300').groups())  # greedy mode
print(re.match(r'^(\d+?)(0*)$', '102300').groups())
