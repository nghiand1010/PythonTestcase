# -*- coding: utf-8 -*-
"""
Editorial Solution for xoayvong
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


s = input().strip()
t = input().strip()

if len(s) == len(t) and t in s + s:
    print("YES")
else:
    print("NO")
