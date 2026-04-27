# -*- coding: utf-8 -*-
"""
Editorial Solution for dayso10
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n = int(input())
ssh1 = (n - 2) // 9 + 1
ssh2 = (n - 4) // 9 + 1
sum = ssh1 * (2 + (2 + (ssh1 - 1) * 9)) // 2 + ssh2 * (4 + (4 + (ssh2 - 1) * 9)) // 2
print(sum % 1000)
