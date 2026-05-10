# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py199
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n,m=map(int,input().split()); a=list(map(int,input().split())); res=[]; cur=[]; s=0
for x in a:
    need=0; ss=s
    for y in sorted(cur, reverse=True):
        if ss+x<=m: break
        ss-=y; need+=1
    res.append(need); cur.append(x); s+=x
print(*res)
