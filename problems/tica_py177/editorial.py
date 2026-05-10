# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py177
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n=int(input()); a=[]; b=[]
for _ in range(n):
    x,y=map(int,input().split()); a.append(x); b.append(y)
a.sort(); b.sort(); score=0; used=[False]*n
for x in a:
    j=next((i for i,y in enumerate(b) if not used[i] and y>x), None)
    if j is not None: used[j]=True; score+=2
for x in a:
    j=next((i for i,y in enumerate(b) if not used[i] and y==x), None)
    if j is not None: used[j]=True; score+=1
print(score)
