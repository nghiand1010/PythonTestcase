# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py189
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


t=int(input())
for _ in range(t):
    n=int(input()); a=list(map(int,input().split())); first={}; ans=0
    for i,x in enumerate(a):
        if x not in first: first[x]=i
        else: ans=max(ans,i-first[x])
    print(ans)
