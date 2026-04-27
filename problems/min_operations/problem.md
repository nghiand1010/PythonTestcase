# Unknown

**URL:** https://oj.tica.edu.vn/problem/min_operations

---

# Tìm Số Phép Toán Tối Thiểu



Bạn được cho hai số nguyên `n` và `k`. Trong một phép toán, bạn có thể trừ bất kỳ lũy thừa nào của `k` khỏi `n`. Cụ thể, trong một phép toán, bạn có thể thay `n` bằng `n - k^x` với `x` là số nguyên không âm.

Hãy tìm số phép toán tối thiểu cần thiết để biến `n` thành `0`.

## Input

Dòng đầu tiên chứa số lượng bộ test `t` (1 ≤ t ≤ 10^4).
Mỗi bộ test gồm một dòng chứa hai số nguyên `n` và `k` (1 ≤ n, k ≤ 10^9).

## Output

Với mỗi bộ test, in ra số phép toán tối thiểu trên một dòng.

## Ví dụ

```
Input
6
5 2
3 5
16 4
100 3
6492 10
10 1

Output
2
3
1
4
21
10
```

## Chú thích

* Trong test thứ nhất, n = 5 và k = 2. Các bước:

  1. Trừ 2^0 = 1 khỏi 5; kết quả n = 4.
  2. Trừ 2^2 = 4 khỏi 4; kết quả n = 0.
     Không thể làm trong ít hơn 2 phép, do đó đáp án là 2.
* Trong test thứ hai, n = 3 và k = 5. Các bước:

  1. Trừ 5^0 = 1 khỏi 3; n = 2.
  2. Trừ 5^0 = 1 khỏi 2; n = 1.
  3. Trừ 5^0 = 1 khỏi 1; n = 0.
     Không thể làm trong ít hơn 3 phép, do đó đáp án là 3.