# -*- coding: utf-8 -*-
"""
Editorial Solution for thttd_ds
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n = int(input())

nhom = n // 12      # mỗi nhóm 12 số có 4 số chia hết cho 6
du = n % 12         # số còn lại

ket_qua = nhom * 4

if du >= 3:
    ket_qua += 1
if du >= 8:
    ket_qua += 1
if du >= 11:
    ket_qua += 1

print(ket_qua)

