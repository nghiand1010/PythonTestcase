a = [[0] * 101 for _ in range(101)]
check = [0] * 101
v = [[] for _ in range(101)]


def dfs(node):
    check[node] = 1
    for neighbor in v[node]:
        if not check[neighbor]:
            dfs(neighbor)


def main():
    t = int(input())
    while t > 0:
        n = int(input())
        s = 0
        ans = 0

        for i in range(1, n + 1):
            check[i] = 0
            v[i].clear()

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                a[i][j] = int(input())
                if i >= j and a[i][j]:
                    v[i].append(j)
                    v[j].append(i)

        for i in range(1, n + 1):
            if not check[i]:
                s += 1
                dfs(i)

        for i in range(1, n + 1):
            check = [0] * 101  # Reset check array
            k = 0
            check[i] = 1
            for j in range(1, n + 1):
                if not check[j]:
                    k += 1
                    dfs(j)
            if k > s:
                s = k
                ans = i

        print(ans)
        t -= 1


if __name__ == "__main__":
    main()
