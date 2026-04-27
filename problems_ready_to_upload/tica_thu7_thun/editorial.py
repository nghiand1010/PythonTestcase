# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_thu7_thun
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n = int(input())
if n == 1:
    print(0)
else:
# tính tổng 3 + 4 + 5 + ... k
    ssh = n - 1
    shc = 3 + (n - 2)
    sum = ssh * (3 + shc) // 2
    print(sum)
