# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py200
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


q=int(input())
for _ in range(q):
    n=int(input()); a=sorted(map(int,input().split()))
    if n<3 or a[-1]>=a[-2]+a[-3]: print('NO')
    else: print('YES'); print(*a[:-2], a[-1], a[-2])
