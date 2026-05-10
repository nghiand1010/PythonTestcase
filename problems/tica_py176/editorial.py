# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py176
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


s,n=map(int,input().split()); d=[tuple(map(int,input().split())) for _ in range(n)]; d.sort(); left=0
for x,y in d:
    if s>x: s+=y
    else: left+=1
print('YES' if left==0 else 'NO')
if left: print(left)
