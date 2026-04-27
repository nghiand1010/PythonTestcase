# -*- coding: utf-8 -*-
"""
Editorial Solution for nenso
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


N = int(input())

if N == 0:
    ans = 0
else:
    ans = 1 + (N - 1) % 9   # công thức digital root

print(ans)

