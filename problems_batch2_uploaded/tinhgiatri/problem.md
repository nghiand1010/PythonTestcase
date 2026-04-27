# Unknown

**URL:** https://oj.tica.edu.vn/problem/tinhgiatri

---

## Đề bài: Tính giá trị

### Mô tả

Cho số nguyên dương **N**. Hãy tính giá trị của biểu thức:

 S = 1 x 2 + 2 x 3 + 3 x 4 + ... + N x (N + 1) 

### Input

Một dòng duy nhất ghi số **N** (( N \le 10^9 )).

### Output

In ra **số dư của S** khi chia cho (10^6 + 7).

### Ràng buộc

* 60% số test có ( N \le 10^3 )
* 30% số test có ( N \le 10^6 )
* 10% số test có ( N \le 10^9 )

### Phân tích & công thức đúng

Viết lại:

`S = sum_{k=1..N} k(k+1) = sum_{k=1..N} (k^2 + k)`

Công thức quen thuộc:
`sum k^2 = N(N+1)(2N+1)/6`, `sum k = N(N+1)/2`.

Cộng lại từng bước:
`S = N(N+1)(2N+1)/6 + N(N+1)/2`
`   = N(N+1)*[(2N+1)+3]/6`
`   = N(N+1)*2*(N+2)/6`
`   = N(N+1)(N+2)/3`.

**Lưu ý:** luôn chia hết cho 3 vì trong ba số liên tiếp `N, N+1, N+2` có đúng một số là bội của 3. Do đó khi lấy modulo `10^6+7`, hãy chia 3 cho một trong ba thừa số rồi mới nhân và lấy mod.

### Kiểm chứng nhanh

* `N=1`: `S=2`; công thức: `1*2*3/3=2`.
* `N=3`: `S=20`; công thức: `3*4*5/3=20`.

### Ví dụ

**Input:**

```
3
```

**Output:**

```
20
```

### Lời giải (Python)

```python
M = 1_000_007
n = int(input())

if n % 3 == 0:
    a = (n // 3) % M
    b = (n + 1) % M
    c = (n + 2) % M
elif (n + 1) % 3 == 0:
    a = n % M
    b = ((n + 1) // 3) % M
    c = (n + 2) % M
else:
    a = n % M
    b = (n + 1) % M
    c = ((n + 2) // 3) % M

ans = (a * b) % M
ans = (ans * c) % M
print(ans)
```

### Độ phức tạp

* Thời gian: ( O(1) )
* Bộ nhớ: ( O(1) )