# -*- coding: utf-8 -*-
"""
Editorial Solution for vienda
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n = int(input().strip())
s = input().strip()

ans = 0
for i in range(n - 1):
    if s[i] == s[i + 1]:
        ans += 1

print(ans)

