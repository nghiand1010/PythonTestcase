# -*- coding: utf-8 -*-
"""
Editorial Solution for so_lonnhat
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


s = input().strip()

digits = list(s)
digits.sort(reverse=True)

print("".join(digits))

