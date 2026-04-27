# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_git4
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


import math

X = int(input())
Y = int(input())
H = int(input())

print(math.ceil(H / (X - Y)))
