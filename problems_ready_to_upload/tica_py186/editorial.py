# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_py186
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n=int(input()); a=list(map(int,input().split())); print(sum(1 for x in a if x%2==0))
