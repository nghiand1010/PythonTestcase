# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py191
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n=int(input()); a=list(map(int,input().split())); b=list(map(int,input().split())); pos={x:i for i,x in enumerate(a)}; mx=-1; ans=0
for x in b:
    if pos[x]<mx: ans+=1
    else: mx=pos[x]
print(ans)
