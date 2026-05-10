# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py180
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n=int(input()); seg=[tuple(map(int,input().split())) for _ in range(n)]; seg.sort(); ans=0; r=-10**18
for a,b in seg:
    if a>r: ans+=1; r=b
    else: r=max(r,b)
print(ans)
