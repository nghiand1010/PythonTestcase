# -*- coding: utf-8 -*-
"""
Editorial Solution for write_remove
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n = int(input())
st = set()
for _ in range(n):
    x = int(input())
    if x in st:
        st.remove(x)
    else:
        st.add(x)
print(len(st))

