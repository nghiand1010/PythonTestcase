# Unknown

**URL:** https://oj.tica.edu.vn/problem/qua_thieunhi

---

# Phát quà Tết thiếu nhi

## Mô tả

Nhân dịp Tết thiếu nhi ngày 1–6, Công đoàn của công ty VHP tổ chức phát quà cho các con của cán bộ công nhân viên có thành tích học tập tốt.  
Công đoàn muốn phát **k** phần quà. Mỗi phần quà gồm:

- 1 bó hoa  
- 1 hộp bút  
- 1 quyển vở  

Hiện tại, Công đoàn đã chuẩn bị được:

- `a` bó hoa  
- `b` hộp bút  
- `c` quyển vở  

---

## Yêu cầu

Tính **số lượng tối thiểu các món đồ** mà Công đoàn cần chuẩn bị **thêm** để đảm bảo có đủ `k` phần quà.

---

## Dữ liệu đầu vào

Gồm một dòng chứa bốn số nguyên `a, b, c, k`  
(`1 ≤ a, b, c, k ≤ 1000`) lần lượt là số bó hoa, số hộp bút, số quyển vở và số phần quà cần phát.

---

## Dữ liệu đầu ra

Gồm một số nguyên duy nhất là **số món đồ cần chuẩn bị thêm**.

---

## Ví dụ

### Ví dụ 1

**Input**
```
2 3 5 4
```

**Output**
```
3
```

---

### Giải thích

- Có 2 bó hoa, 3 hộp bút, 5 quyển vở nên hiện tại chỉ tạo được `min(2,3,5) = 2` phần quà.
- Để đủ 4 phần quà, cần chuẩn bị thêm:
  - 2 bó hoa
  - 1 hộp bút
- Tổng số món đồ cần chuẩn bị thêm là `2 + 1 = 3`.