# -*- coding: utf-8 -*-
"""
Editorial Solution for 24thtbbnqnhy4
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


s = input().strip()

st = []
cnt = 0

for c in s:
    if st and st[-1] == c:
        st.pop()
        cnt += 1
    else:
        st.append(c)

print("Bob" if cnt % 2 == 1 else "Alice")

