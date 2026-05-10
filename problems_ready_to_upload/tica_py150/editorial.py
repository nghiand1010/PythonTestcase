# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py150
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


q=int(input())
for _ in range(q):
    n=int(input()); a=list(map(int,input().split())); a.sort(); print(*a)
