# -*- coding: utf-8 -*-
"""
Editorial Solution for vitri_robot
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


a, b, k = map(int, input().split())
t = k // 2
x = t * (a - b) + (k % 2) * a
print(x)

