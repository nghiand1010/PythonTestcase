# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_sodep
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n = int(input())
if n<=9:
    print(n)
elif n % 9 == 0:
    print(9)
else:
    print(n % 9)
