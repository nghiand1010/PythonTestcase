# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py192
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n,k=map(int,input().split()); a=list(map(int,input().split())); res=[]
for x in a:
    if x in res: continue
    res.insert(0,x)
    if len(res)>k: res.pop()
print(len(res)); print(*res)
