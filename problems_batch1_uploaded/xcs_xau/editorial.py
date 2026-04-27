# -*- coding: utf-8 -*-
"""
Editorial Solution for xcs_xau
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


s = input().rstrip()      # đọc xâu

res = ""
for ch in s:
    if not ch.isdigit():  # nếu không phải chữ số thì giữ lại
        res += ch

print(res)

