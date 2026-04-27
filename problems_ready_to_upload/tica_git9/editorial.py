# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git9
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


# Import thư viện math
import math

# Đọc dữ liệu đầu vào
m, n, k = map(int, input().split())

# Tính số đội tối đa ban đầu
max_doi = min(m // 2, n)

# Kiểm tra nếu tổng số người còn lại đủ để bù cho k
if (m - max_doi * 2 + n - max_doi) >= k:
    print(max_doi)
else:
    # Giảm số đội tối đa dần cho đến khi điều kiện đủ thỏa mãn
    while max_doi != 0 and (m - max_doi * 2 + n - max_doi < k):
        max_doi -= 1
    print(max_doi)
