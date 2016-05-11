# -*- coding: utf-8 -*-
import random


num = random.randint(0, 100)
# print(num)
# 猜数字游戏
while True:
    try:
        n = int(input('Enter 1~100: '))
    except Exception as e:
        print('Enter Error!')
        continue
    else:
        if n == num:
            print('Success!!!')
            break
        elif n > num:
            print('guess Big...')
        else:
            print('guess Small...')
