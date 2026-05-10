# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py85
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n, k = map(int, input().split())
lo = 1
hi = n
while lo < hi:
    mid = (lo + hi) // 2
    con = mid * (mid + 1) // 2 - (n - mid)
    if con >= k:
        hi = mid
    else:
        lo = mid + 1
print(n - lo)
