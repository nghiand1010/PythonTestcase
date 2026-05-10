# -*- coding: utf-8 -*-
"""
Editorial Solution for nguocdong_tg
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def nhuan(y):
    if y % 400 == 0:
        return True
    if y % 4 == 0 and y % 100 != 0:
        return True
    return False


s = int(input())

x = s - 1

ck = x // 146097
y = 1 + ck * 400
x = x % 146097

while True:
    if nhuan(y):
        sn = 366
    else:
        sn = 365

    if x >= sn:
        x = x - sn
        y = y + 1
    else:
        break

t = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m = 1

for i in range(12):
    st = t[i]

    if i == 1 and nhuan(y):
        st = 29

    if x >= st:
        x = x - st
        m = m + 1
    else:
        break

d = x + 1

print(d, m, y)
