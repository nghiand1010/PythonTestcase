# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git100
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


while 1:
  n = int(input())
  if n == 0:
    break
  a = [[0 for i in range(n+1)] for j in range(n + 1)]
  a[0][0] = 1
  for i in range(1, n + 1):
    a[i][0] = a[i - 1][i - 1]
    for j in range(1, i + 1):
      a[i][j] = a[i - 1][j - 1] + a[i][j - 1]
  print(n, a[n][0])
