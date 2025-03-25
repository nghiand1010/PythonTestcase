def get_total(a,b):
    min_val=min(a,b)
    max_val=max(a,b)

    if min_val<2:
        return 0
    if min_val%2==1:
        return min_val//2
    if min_val%2==0 and min_val<max_val:
        return min_val//2
    return min_val//2-1


q = int(input())
for inp in range(q):
    a, b = list(map(int, input().split()))
    print(get_total(a,b))