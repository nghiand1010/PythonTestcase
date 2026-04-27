# -*- coding: utf-8 -*-
"""
Editorial Solution for dembanco
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


N = int(input())
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())


h = x2 - x1 + 1
w = y2 - y1 + 1
A = h * w


if (x1 + y1) % 2 == 0:
    black = (A + 1) // 2
else:
    black = A // 2


white = A - black
print(black)
print(white)
