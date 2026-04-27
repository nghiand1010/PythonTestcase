# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_23ldoa3
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


a = int(input())
b = int(input())
k = int(input())
p = int(input())
x = a
y = b
while x % y != 0 and y % x != 0:
    if y > x:
        y = y%x
    else:
        x = x%y
if y < x:
    uoc = y
else:
    uoc = x
n = a*b//uoc
kq = n+(k*p)
s = 0
for item in str(kq):
    s += int(item)
print(s)
