# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py174
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n=int(input()); a=list(map(int,input().split())); g=[[],[],[]]
for i,x in enumerate(a,1): g[x-1].append(i)
m=min(map(len,g)); print(m)
for i in range(m): print(g[0][i],g[1][i],g[2][i])
