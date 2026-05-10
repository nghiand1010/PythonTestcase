# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py158
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n=int(input()); a=sorted(map(int,input().split())); b=sorted(map(int,input().split())); print('Yes' if all(x>y for x,y in zip(a,b)) else 'No')
