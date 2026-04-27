# -*- coding: utf-8 -*-
"""
Editorial Solution for file_name
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n = int(input().strip())
s = input().strip()

ans = 0
cnt = 0

for ch in s:
    if ch == 'x':
        cnt += 1
    else:
        if cnt >= 3:
            ans += cnt - 2
        cnt = 0

# xử lý nếu chuỗi kết thúc bằng 'x'
if cnt >= 3:
    ans += cnt - 2

print(ans)

