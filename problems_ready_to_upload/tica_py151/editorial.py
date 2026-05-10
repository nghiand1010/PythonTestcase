# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py151
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


q=int(input())
for _ in range(q):
    n=int(input()); a=list(map(int,input().split())); b=list(map(int,input().split())); a.sort(reverse=True); b.sort(); print(sum(x*y for x,y in zip(a,b)))
