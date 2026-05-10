# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py175
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n=int(input()); a=sorted(map(int,input().split())); print(max(a[-1]*a[-2]*a[-3], a[0]*a[1]*a[-1]))
