# -*- coding: utf-8 -*-
"""
Editorial Solution for lehoiphim
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n = int(input())
movies = []
for _ in range(n):
    a, b = map(int, input().split())
    movies.append([a, b])


# Sắp xếp theo thời gian kết thúc (phần tử thứ hai)
for i in range(n - 1):
    for j in range(i + 1, n):
        if movies[i][1] > movies[j][1]:
            movies[i], movies[j] = movies[j], movies[i]


c = 0
e = -10**18
for a, b in movies:
    if a >= e:
        c += 1
        e = b
print(c)
