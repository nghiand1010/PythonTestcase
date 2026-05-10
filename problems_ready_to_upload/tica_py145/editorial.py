# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py145
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


from collections import Counter
q=int(input())
for _ in range(q):
    n=int(input()); a=list(map(int,input().split())); c=Counter(a); best=max([x for x in c if c[x]>=4], default=-1)
    print(-1 if best==-1 else f'{best*best} {c[best]//4}')
