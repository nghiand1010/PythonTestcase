# -*- coding: utf-8 -*-
"""
Editorial Solution for sapxepcs
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n_str = input().strip()

digits = sorted(n_str)
t = ''.join(digits)

t = t.lstrip('0')
if t == '':
    t = '0'

print(t)

