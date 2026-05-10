# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py155
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


q=int(input())
for _ in range(q):
    n=int(input()); a=list(map(int,input().split())); first=10**18; second=10**18; ok=False
    for x in a:
        if x<=first: first=x
        elif x<=second: second=x
        else: ok=True
    print('YES' if ok else 'NO')
