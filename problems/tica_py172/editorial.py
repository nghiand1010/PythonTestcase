# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py172
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n=int(input()); a=list(map(int,input().split())); mn=min(a); mx=max(a); d=mx-mn
if d==0: print(0, n*(n-1)//2)
else: print(d, a.count(mn)*a.count(mx))
