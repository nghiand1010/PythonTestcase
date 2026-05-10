# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py195
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


q=int(input())
for _ in range(q):
    n,k=map(int,input().split()); a=list(map(int,input().split())); pos=[i+1 for i,x in enumerate(a) if x%2]
    if len(pos)<k or (len(pos)-k)%2: print('NO')
    else: print('YES'); print(*pos[:k-1], n)
