# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py171
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n=int(input()); a=list(map(int,input().split())); b=list(map(int,input().split())); s=set(a[1:])|set(b[1:]); print('YES' if len(s)==n else 'NO')
