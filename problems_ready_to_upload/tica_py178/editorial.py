# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py178
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n=int(input()); a=list(map(int,input().split())); from collections import Counter; c=Counter(a); m=max(c.values()); print(*sorted(x for x in c if c[x]==m))
