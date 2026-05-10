# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py162
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n,t=map(int,input().split()); a=[]
for _ in range(n):
    name,point=input().split(); a.append((-int(point),name))
a.sort()
for _,name in a[:t]: print(name)
