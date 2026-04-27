# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_23thtmta3
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


a = int(input())
t = int(input())
k = input()
x = 0
for i in range(59 + 1):
    s = str(i)
    if len(s) == 1:
        s = "0" + s
    x += s.count(k)
y = str(a).count(k)
if a < 10 and k == "0":
    y += 1
soluong = (t // 60 * x)
for i in range(1 , t % 60 + 1):
    s = str((a + i) % 60)
    if len(s) == 1:
        s = "0" + s
    soluong += s.count(k)
print(y + soluong)
