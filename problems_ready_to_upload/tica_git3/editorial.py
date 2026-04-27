# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git3
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n = int(input())
a = -1
b = -1

k = n // 4
for i in range(k + 1):
    if (n - 4 * i) % 7 == 0:
        a = i
        b = (n - 4 * a) // 7
        break

if a == -1 and b == -1:
    print(-1)
else:
    print("4" * a + "7" * b)
