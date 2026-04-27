# -*- coding: utf-8 -*-
"""
Editorial Solution for caudo
Auto-generated from editorial.txt
"""

import sys
from io import StringIO

# Read input
N = int(input().strip())

# Convert to binary and remove '0b' prefix
binary = bin(N)[2:]

# Pad to at least 5 digits
if len(binary) < 5:
    binary = binary.zfill(5)

# Replace 1→A, 0→O
result = []
for bit in binary:
    if bit == '1':
        result.append('A')
    else:
        result.append('O')

# Print with spaces
print(' '.join(result))
