# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py149
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def cnt(x,k): return str(x).count(str(k))
q=int(input())
for _ in range(q):
    n,k=map(int,input().split()); a=list(map(int,input().split())); print(sum(cnt(x,k) for x in a))
