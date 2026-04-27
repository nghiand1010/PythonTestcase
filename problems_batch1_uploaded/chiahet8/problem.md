# Unknown

**URL:** https://oj.tica.edu.vn/problem/chiahet8

---

# TẠO SỐ LỚN NHẤT CHIA HẾT CHO 8

## 📌 Đề bài

Cho một số tự nhiên **n**.  
Hãy **sắp xếp lại các chữ số** của số **n** để tạo ra **số lớn nhất có thể chia hết cho 8**.

- Mỗi chữ số được sử dụng **đúng số lần xuất hiện trong n**.
- Số tạo ra **không được có chữ số 0 vô nghĩa ở đầu** (trừ khi số chỉ có một chữ số).
- Nếu **không thể tạo ra** số nào chia hết cho 8 thì in ra **-1**.

---

## 📥 Dữ liệu vào

- Một chuỗi ký tự biểu diễn số tự nhiên **n**.
- Độ dài chuỗi có thể lên đến **10⁵ chữ số**.

---

## 📤 Dữ liệu ra

- In ra **số lớn nhất chia hết cho 8** được tạo từ các chữ số của **n**.
- Nếu không tồn tại, in ra **-1**.

---

## 📘 Ví dụ

### Ví dụ 1

**Input**
```
345902
```

**Output**
```
954320
```

**Giải thích**

Ba chữ số cuối là `320`.  
`320` chia hết cho `8`, và đây là số lớn nhất có thể tạo ra.

---

### Ví dụ 2

**Input**
```
101
```

**Output**
```
-1
```

**Giải thích**

Không thể tạo ra số nào chia hết cho `8` từ các chữ số đã cho.

---

### Ví dụ 3

**Input**
```
8881
```

**Output**
```
888
```

**Giải thích**

`888` chia hết cho `8` và là số lớn nhất có thể tạo được.

---

## 💡 Gợi ý

- Một số chia hết cho **8** nếu **ba chữ số cuối** của nó chia hết cho **8**.
- Chỉ có **125** số trong khoảng từ `000` đến `999` chia hết cho `8`.
- Có thể thử tất cả các bộ **3 chữ số cuối hợp lệ**, sau đó:
  - Dùng **đếm phân phối (counting sort)** để sắp xếp các chữ số còn lại theo thứ tự giảm dần,
  - Ghép thêm ba chữ số cuối để tạo số lớn nhất.