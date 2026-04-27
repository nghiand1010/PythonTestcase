# Unknown

**URL:** https://oj.tica.edu.vn/problem/kiemtra_hoanhao

---

# 🧮 Bài toán: Kiểm tra số hoàn hảo

## 🔹 Đề bài
Số **hoàn hảo** là số mà **tổng các ước của nó bằng 2 lần chính nó**.

**Ví dụ:**  
- 6 là số hoàn hảo vì các ước của 6 là 1, 2, 3, 6  
  → Tổng = 1 + 2 + 3 + 6 = 12 = 2 × 6  

---

## 🔹 Yêu cầu
Viết chương trình nhập vào số nguyên **n**.  
In ra:
- `YES` nếu **n** là số hoàn hảo  
- `NO` nếu không phải

---

## 🔹 Input
- Một số nguyên dương `n` (n ≤ 10¹²)

## 🔹 Output
- In ra chữ `YES` hoặc `NO`.

---

## 🔹 Ví dụ

### ✅ Test 1
**Input:**
```
6
```
**Output:**
```
YES
```

### ✅ Test 2
**Input:**
```
36
```
**Output:**
```
NO
```

---

## 🔹 Gợi ý cách giải
- Duyệt tất cả các ước của `n` từ `1 → √n`.
- Cộng tổng các ước theo cặp `(i, n//i)`.
- Nếu tổng các ước thực sự (không tính `n`) bằng `n` → là số hoàn hảo.

---