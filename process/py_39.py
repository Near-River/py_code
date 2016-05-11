#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess


# subprocess:

# print('$ nslookup www.python.org')
print('> ping www.python.org')
r = subprocess.call(['ping', 'www.python.org'])
print('Exit code:', r)


# Works on Unix / Linux
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode(encoding='utf-8', errors='ignore'))
print('Exit code:', p.returncode)
