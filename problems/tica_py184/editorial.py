# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py184
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n=int(input()); last={}; ans=0
for _ in range(n):
    c,s=map(int,input().split())
    if c in last and last[c]!=s: ans+=1
    last[c]=s
print(ans)
