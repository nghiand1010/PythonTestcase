# Unknown

**URL:** https://oj.tica.edu.vn/problem/sodacbiet5

---

# BÀI TOÁN: SỐ LẶP ĐẶC BIỆT

## 📌 Mô tả
Một số tự nhiên **n** được gọi là **số lặp đặc biệt** nếu thỏa mãn **đồng thời** các điều kiện sau:

1. Chỉ chứa **đúng hai chữ số khác nhau**.
2. Hai chữ số đó **thuộc tập {1, 2, 3, 4}**.
3. Hai chữ số xuất hiện **xen kẽ nhau** (dạng: a b a b a b ...).

---

## 📘 Ví dụ

### ✅ Số lặp đặc biệt
- `12`, `23`, `323`, `1212`, `31313`

### ❌ Không phải số lặp đặc biệt
- `1` (chỉ có một chữ số)
- `1122` (không xen kẽ)
- `1234` (nhiều hơn hai chữ số khác nhau)
- `787878` (chứa chữ số ngoài {1,2,3,4})

---

## 📋 Dãy số lặp đặc biệt (ban đầu)
```
12, 13, 14, 21, 23, 24, 31, 32, 34, 41, 42, 43,
121, 131, 141, 212, 232, 242, 313, 323, 343,
414, 424, 434, ...
```

---

## 🎯 Yêu cầu
Cho một số tự nhiên **n**.
- Nếu **n không phải số lặp đặc biệt**, in ra `NO`.
- Nếu **n là số lặp đặc biệt**, hãy in ra **vị trí của n trong dãy các số lặp đặc biệt** (đánh số từ 1).

---

## 📥 Input
- Một số tự nhiên duy nhất **n**  
- (1 < n < 10^15)

---

## 📤 Output
- In ra `NO` nếu n không phải số lặp đặc biệt  
- Ngược lại, in ra **vị trí của n trong dãy**

---

## 🧪 Ví dụ

| Dữ liệu | Kết quả |
|-------|--------|
| 1234 | NO |
| 121  | 13 |

---

## ⚙️ Ràng buộc
- 50% số test: (n < 10^4)
- 50% số test còn lại: không có ràng buộc thêm