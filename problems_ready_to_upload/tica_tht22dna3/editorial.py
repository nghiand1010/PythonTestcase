# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_tht22dna3
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


n = int(input())
firstnumber = (n - 1) ** 2 + 1
lastnumber = n ** 2
numbers = (lastnumber - firstnumber) + 1
print((firstnumber + lastnumber) * numbers // 2)
