# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py181
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n=int(input()); a=list(map(int,input().split())); pre=[0]
for x in a: pre.append(pre[-1]+x)
q=int(input())
for _ in range(q):
    l,r=map(int,input().split()); print(pre[r]-pre[l-1])
