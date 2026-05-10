# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py198
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


q=int(input())
for _ in range(q):
    n=int(input()); a=list(map(int,input().split())); c=[0,0,0]
    for x in a: c[x%3]+=1
    ans=c[0]+min(c[1],c[2]); m=min(c[1],c[2]); c[1]-=m; c[2]-=m; ans+=c[1]//3+c[2]//3; print(ans)
