# -*- coding: utf-8 -*-
"""
Editorial Solution for toan_hoc
Auto-generated from editorial.txt
"""

import sys
from io import StringIO

s = input().strip()
parts = s.split('+')
parts.sort()
print('+'.join(parts))
