# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py170
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def tm(x): return (x//100)*60+x%100
t=int(input())
for _ in range(t):
    n=int(input()); a=list(map(tm,map(int,input().split()))); b=list(map(tm,map(int,input().split()))); e=[]
    for x in a: e.append((x,1))
    for x in b: e.append((x,-1))
    e.sort(key=lambda z:(z[0],z[1])); cur=ans=0
    for _,v in e: cur+=v; ans=max(ans,cur)
    print(ans)
