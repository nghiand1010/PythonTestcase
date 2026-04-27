# -*- coding: utf-8 -*-
"""
Editorial Solution for xenke_vongtron
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


s = input().strip()
n = len(s)

# Nhân đôi xâu để xử lý vòng tròn
s2 = s + s

best = 1
cur = 1

for i in range(1, len(s2)):
    # Nếu hai ký tự liên tiếp là chữ thật và giống nhau
    if s2[i] != '?' and s2[i-1] != '?' and s2[i] == s2[i-1]:
        cur = 1
    else:
        cur += 1

    # Không được vượt quá độ dài xâu ban đầu
    if cur > n:
        cur = n

    best = max(best, cur)

print(best)

