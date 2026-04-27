# Unknown

**URL:** https://oj.tica.edu.vn/problem/toan_hoc

---

# A. Mathematics to the Rescue (Toán học cứu nguy)

## Giới hạn
- **Thời gian:** 2 giây
- **Bộ nhớ:** 256 MB

---

## 📘 Mô tả bài toán

Ksenia là một cô bé yêu thích toán học và đang học lớp 3. Hiện tại, em đang học **phép cộng** ở trường.

Cô giáo đã viết lên bảng một phép tính gồm nhiều số và yêu cầu Ksenia tính kết quả. Để đơn giản hơn, phép tính **chỉ sử dụng các số 1, 2 và 3**.

Tuy nhiên, Ksenia mới chỉ đang học đếm nên **chỉ có thể tính được phép cộng nếu các số trong phép cộng được sắp xếp theo thứ tự không giảm** (tức là số sau **không nhỏ hơn** số trước).

Ví dụ:
- ❌ Ksenia **không thể** tính: `1 + 3 + 2 + 1`
- ✅ Ksenia **có thể** tính: `1 + 1 + 2` và `3 + 3`

---

## 🎯 Yêu cầu

Bạn được cho một phép cộng viết trên bảng.

Hãy **sắp xếp lại các số** trong phép cộng đó sao cho Ksenia **có thể tính được**, rồi in ra phép cộng mới.

---

## 📥 Dữ liệu vào (Input)

- Dòng đầu tiên chứa một chuỗi **không rỗng** `s` — là phép cộng mà Ksenia cần tính.
- Chuỗi `s`:
  - Không chứa dấu cách
  - Chỉ gồm các chữ số `1`, `2`, `3` và dấu `+`
  - Là một phép cộng hợp lệ của các số `1`, `2`, `3`
  - Độ dài không vượt quá **100 ký tự**

---

## 📤 Dữ liệu ra (Output)

- In ra một phép cộng mới mà Ksenia **có thể tính được** (các số được sắp xếp theo thứ tự không giảm).

---

## 🧪 Ví dụ

### Ví dụ 1
**Input**
```
3+2+1
```
**Output**
```
1+2+3
```

---

### Ví dụ 2
**Input**
```
1+1+3+1+3
```
**Output**
```
1+1+1+3+3
```

---

### Ví dụ 3
**Input**
```
2
```
**Output**
```
2
```