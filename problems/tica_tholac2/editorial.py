# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_tholac2
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def solve():
    import sys
    
    MOD = 10**6
    N = int(sys.stdin.readline().strip())
    
    q, r = divmod(N, 6)
    
    # Để tránh số quá to, ta cũng nên đưa q^2 về mod trước, 
    # nhưng về lý thuyết Python không sao. Tuy nhiên an toàn thì nên làm.
    q_mod = q % MOD
    q2_mod = (q_mod * q_mod) % MOD
    
    if r == 0:
        ans = (3*q2_mod + 3*q_mod + 1) % MOD
    elif r == 1:
        ans = (3*q2_mod + 4*q_mod + 1) % MOD
    elif r == 2:
        ans = (3*q2_mod + 5*q_mod + 2) % MOD
    elif r == 3:
        ans = (3*q2_mod + 6*q_mod + 3) % MOD
    elif r == 4:
        ans = (3*q2_mod + 7*q_mod + 4) % MOD
    else:  # r == 5
        ans = (3*q2_mod + 8*q_mod + 5) % MOD
    
    print(ans)
    
solve()
