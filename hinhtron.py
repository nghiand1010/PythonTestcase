s = input().strip()
n = len(s)

bad = -1
for i in range(1, n):
    if int(s[i]) % 2 == int(s[i - 1]) % 2:
        bad = i
        break

if bad == -1:
    print(s)
else:
    kq = ""

    for i in range(bad, -1, -1):
        a = int(s[i])

        for d in range(a - 1, -1, -1):
            if i == 0 and d == 0:
                continue

            if i > 0 and d % 2 == int(s[i - 1]) % 2:
                continue

            kq = s[:i] + str(d)
            last = d

            for j in range(i + 1, n):
                if last % 2 == 0:
                    kq += "9"
                    last = 9
                else:
                    kq += "8"
                    last = 8

            break

        if kq != "":
            break

    if kq == "":
        for i in range(n - 1):
            if i % 2 == 0:
                kq += "9"
            else:
                kq += "8"

    print(kq)