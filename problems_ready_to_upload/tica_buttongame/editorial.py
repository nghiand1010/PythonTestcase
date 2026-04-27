# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_buttongame
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


a,b,c = map(int,input().split())
tmp = [a, b, c]
tmp.sort()

Max=tmp[2]
Mid=tmp[1]
Min=tmp[0]
print((Max-Mid)+(Mid-Min)*2)
