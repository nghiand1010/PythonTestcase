# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py194
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


t=int(input())
for _ in range(t):
    n,x,a,b=map(int,input().split()); d=abs(a-b); print(min(n-1,d+x))
