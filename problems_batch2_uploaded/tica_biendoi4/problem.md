# Unknown

**URL:** https://oj.tica.edu.vn/problem/tica_biendoi4

---

## Trò chơi phép nhân và chia

Một số tự nhiên **K** được dùng trong trò chơi như sau:

- Nếu **K chia hết cho 4**, thì **K được thay bằng K chia cho 4**.  
- Nếu **K không chia hết cho 4**, thì **K được thay bằng K nhân với 5**.

Quá trình lặp lại liên tục cho đến khi **K = 1** hoặc không thể tiếp tục theo quy tắc mà không lặp vô hạn.

---

### Yêu cầu
Hãy xác định **số lần biến đổi** cần thực hiện để đưa số **K** về 1 theo quy tắc trên.  
Nếu không thể đưa **K** về 1, in ra **-1**.

---

### Dữ liệu
Một dòng duy nhất chứa số nguyên dương **K**  
(1 ≤ K ≤ 10⁹).

---

### Kết quả
In ra một số nguyên duy nhất là **số lần biến đổi** cần để đưa K về 1, hoặc **-1** nếu không thể.

---

### Ví dụ

| Dữ liệu | Kết quả | Giải thích |
|:--------:|:--------:|:-----------|
| 16 | 2 | 16 chia 4 → 4; 4 chia 4 → 1. |
| 5  | -1 | 5 nhân 5 = 25; 25 nhân 5 = 125; ... không thể về 1. |

---

### Gợi ý
- Chỉ khi **K** là lũy thừa của 4 (K = 4^t) thì mới chia được về 1.  
- Nếu K không phải lũy thừa của 4, sẽ bị nhân 5 vô hạn.

---

### Mã minh họa (Python)
```python
K = int(input())

step = 0
while K % 4 == 0:
    K //= 4
    step += 1

print(step if K == 1 else -1)
```