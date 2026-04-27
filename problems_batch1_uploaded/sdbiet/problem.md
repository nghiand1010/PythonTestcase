# Unknown

**URL:** https://oj.tica.edu.vn/problem/sdbiet

---

## Đề bài: Số đặc biệt thứ N

### Mô tả
Số **X** được gọi là *số đặc biệt* nếu tất cả các chữ số của **X** đều thuộc tập hợp {1, 3, 5, 7, 9}. Người ta tạo ra các số đặc biệt này, sau đó sắp xếp chúng theo thứ tự tăng dần để được dãy số **A**.

Ví dụ 20 số đặc biệt đầu tiên: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 31, 33, 35, 37, 39, 51, 53, 55, 57, 59.

### Yêu cầu
Cho số nguyên dương **N**, hãy tìm số đặc biệt thứ **N** trong dãy số **A**.

### Dữ liệu đầu vào
Một dòng duy nhất chứa số nguyên **N** (1 ≤ N ≤ 10^18).

### Dữ liệu đầu ra
In ra số đặc biệt thứ **N** trong dãy **A**.

### Ràng buộc dữ liệu
- 50% số điểm: N ≤ 10^6  
- 30% số điểm: 10^6 < N ≤ 10^9  
- 20% số điểm: không có ràng buộc gì thêm.

### Ví dụ
#### Input
```
8
```
#### Output
```
15
```
Giải thích: Số đặc biệt thứ 8 trong dãy là 15.

#### Input
```
29
```
#### Output
```
97
```
Giải thích: Số đặc biệt thứ 29 trong dãy là 97.

---

### Lời giải Python
```python
N = int(input().strip())
digits = []
x = N
while x > 0:
    d = (x - 1) % 5 + 1
    digits.append(d)
    x = (x - 1) // 5
res_chars = []
for d in reversed(digits):
    res_chars.append(str(2 * d - 1))
print("".join(res_chars))
```