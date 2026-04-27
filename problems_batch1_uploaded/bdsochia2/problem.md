# Unknown

**URL:** https://oj.tica.edu.vn/problem/bdsochia2

---

# Biến đổi số

Cho một số nguyên dương **N** \((1 \le N \le 10^{18})\).  
Để biến đổi số **N** thành **1**, ta có thể thực hiện bằng cách sử dụng các phép toán sau:

- **Phép toán 1:** Nếu `N` là số **chẵn**, em chia `N` cho `2`.
- **Phép toán 2:** Nếu `N` là số **lẻ**, em có thể trừ đi `1` **hoặc** cộng thêm `1`.

---

## Yêu cầu

Em hãy viết chương trình tìm **số bước ít nhất** để biến đổi số `N` về `1`  
(có thể có nhiều cách biến đổi khác nhau, nhưng cần chọn cách có số bước nhỏ nhất).

---

## Dữ liệu vào

- Nhập vào **một số nguyên dương N**.

---

## Kết quả

- In ra **một số nguyên** – là **số bước ít nhất** để biến đổi `N` thành `1`.

---

## Ví dụ

### Ví dụ

**Dữ liệu vào**
```
15
```

**Dữ liệu ra**
```
5
```

**Giải thích**
```
15 → 16  (cộng 1)
16 → 8   (chia 2)
8  → 4   (chia 2)
4  → 2   (chia 2)
2  → 1   (chia 2)
```