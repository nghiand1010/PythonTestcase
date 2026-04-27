# Unknown

**URL:** https://oj.tica.edu.vn/problem/bsodientu

---

# Bảng số điện tử  
*(Đề thi HSG tỉnh lớp 12 năm 2012–2013)*

## Mô tả bài toán

Trong một số hoạt động xã hội, người ta thường dùng một **bảng điện tử** hiển thị các **số tự nhiên liên tiếp**.  
Mỗi số được hiển thị trong **1 giây**, sau đó bảng sẽ chuyển sang số tiếp theo.

Mỗi **chữ số** được hiển thị bằng một số **đoạn bóng đèn nhỏ**.  
Số đoạn bóng đèn cần bật sáng cho từng chữ số được cho trong bảng sau:

| Chữ số | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|------|---|---|---|---|---|---|---|---|---|---|
| Số đoạn bóng đèn | 6 | 2 | 5 | 5 | 4 | 5 | 6 | 3 | 7 | 6 |

Ví dụ:
- Khi hiển thị số **19** cần dùng `2 + 6 = 8` đoạn bóng đèn.
- Số **7** cần dùng `3` đoạn bóng đèn.

---

## Yêu cầu

Cho biết hai số **S** và **T** là số bắt đầu và số kết thúc cần hiển thị trên bảng điện tử.  
Hãy xác định **lượng điện tiêu thụ W** cần thiết để hiển thị **các số tự nhiên liên tiếp từ S đến T**.

Biết rằng:
- Mỗi đoạn bóng đèn khi sáng **tiêu thụ 1 đơn vị điện năng trong 1 giây**.
- Mỗi số được hiển thị trong **1 giây**.

---

## Dữ liệu vào

Từ tệp văn bản **DEN.INP**, chứa **nhiều dòng**,  
mỗi dòng gồm hai số nguyên **S, T**:

- `0 ≤ S < T ≤ 10000`
- Số dòng **không quá 10000**

---

## Dữ liệu ra

Ghi ra tệp **DEN.OUT**, gồm nhiều dòng,  
mỗi dòng là một số **W** – lượng điện năng cần thiết tương ứng với từng dòng dữ liệu vào.

---

## Ví dụ

### DEN.INP
```
8 12
9 11
```

### DEN.OUT
```
32
18
```

---

## Giải thích ví dụ

- Các số từ **8 đến 12**:
  - 8 → 7 đoạn
  - 9 → 6 đoạn
  - 10 → 6 + 2 = 8 đoạn
  - 11 → 2 + 2 = 4 đoạn
  - 12 → 2 + 5 = 7 đoạn  
  → Tổng = **32**

- Các số từ **9 đến 11**:
  - 9 → 6 đoạn
  - 10 → 8 đoạn
  - 11 → 4 đoạn  
  → Tổng = **18**