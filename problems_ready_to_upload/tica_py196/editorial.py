# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py196
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


q=int(input())
for _ in range(q):
    n=int(input()); a=list(map(int,input().split())); mn=10**18; ans=0
    for x in reversed(a):
        if x>mn: ans+=1
        mn=min(mn,x)
    print(ans)
