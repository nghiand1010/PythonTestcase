# -*- coding: utf-8 -*-
"""
Editorial Solution for muahang_qnam
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n = int(input())
a = list(map(int, input().split()))
a.sort()
cur = 0
ans = 0
for x in a:
    if x > cur + 1:
        break
    cur += x
ans = cur + 1
print(ans)

