# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py165
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


t=int(input())
for _ in range(t):
    n=int(input()); a=list(map(int,input().split())); cur=best=a[0]
    for x in a[1:]: cur=min(x,cur+x); best=min(best,cur)
    print(best)
