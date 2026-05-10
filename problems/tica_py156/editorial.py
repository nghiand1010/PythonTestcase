# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py156
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


q=int(input())
for _ in range(q):
    n=int(input()); a=list(map(int,input().split())); print(*(sorted([x for x in a if x%2==0])+sorted([x for x in a if x%2])))
