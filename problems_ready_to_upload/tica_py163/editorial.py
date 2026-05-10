# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py163
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


s=input().strip(); from collections import Counter; c=Counter(s)
for ch in sorted(c): print(f'{ch}: {c[ch]}')
