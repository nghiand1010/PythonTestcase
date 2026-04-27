# Unknown

**URL:** https://oj.tica.edu.vn/problem/sothuvi

---

## Đề bài: Số thú vị thứ N

### Mô tả
Một số **X** được gọi là *số thú vị* nếu tất cả các chữ số của **X** đều thuộc tập hợp {2, 4, 6, 8}. Người ta tạo ra các số thú vị, sau đó sắp xếp chúng theo thứ tự tăng dần để được dãy số **B**.

Ví dụ 20 số thú vị đầu tiên: 2, 4, 6, 8, 22, 24, 26, 28, 42, 44, 46, 48, 62, 64, 66, 68, 82, 84, 86, 88.

### Yêu cầu
Cho số nguyên dương **N**, hãy tìm số thú vị thứ **N** trong dãy số **B**.

### Dữ liệu đầu vào
Một dòng duy nhất chứa số nguyên **N** (1 ≤ N ≤ 10^18).

### Dữ liệu đầu ra
In ra số thú vị thứ **N** trong dãy **B**.

### Ràng buộc dữ liệu
- 50% số điểm: N ≤ 10^6  
- 30% số điểm: 10^6 < N ≤ 10^9  
- 20% số điểm: không có ràng buộc gì thêm.

### Ví dụ
#### Input
```
5
```
#### Output
```
22
```
Giải thích: Số thú vị thứ 5 trong dãy là 22.

#### Input
```
10
```
#### Output
```
28
```
Giải thích: Số thú vị thứ 10 trong dãy là 28.

---

### Lời giải Python
```python
N = int(input().strip())
digits = []
x = N
while x > 0:
    d = (x - 1) % 4 + 1
    digits.append(d)
    x = (x - 1) // 4
res_chars = []
for d in reversed(digits):
    res_chars.append(str(2 * d))
print("".join(res_chars))
```