# -*- coding: utf-8 -*-
"""
Editorial Solution for tongdayso
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n = int(input())
m = int(input())

k = m//2

if m % 2 == 0:
ssh = (k - 1) + 1
s1 = (1 + k) * ssh //2
else:
ssh = (k+1 -1) + 1
s1 = (1 + k + 1) * ssh //2

k1 = n - k + 1
ssh = (n - k1) + 1
s2 = (k1 + n) * ssh //2

print(s1 + s2)
