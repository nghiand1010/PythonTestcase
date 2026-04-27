def solve():
    n, S = map(int, input().split())
    a = list(map(int, input().split()))

    cnt = [0] * (S + 1)
    ans = 0

    for x in a:
        need = S - x
        if 1 <= need <= S:
            ans += cnt[need]
        if 1 <= x <= S:
            cnt[x] += 1

    print(ans)

solve()