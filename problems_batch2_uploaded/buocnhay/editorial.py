# -*- coding: utf-8 -*-
"""
Editorial Solution for buocnhay
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


x1 = int(input())
x2 = int(input())
a = int(input())
distance = abs(x2 - x1)
steps = (distance + a - 1) // a
print(steps)
