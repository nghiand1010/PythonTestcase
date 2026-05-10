# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py159
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n=int(input()); a=list(map(int,input().split())); from collections import Counter; c=Counter(a); print(max(c.values()), len(c))
