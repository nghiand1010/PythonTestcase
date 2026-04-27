# Unknown

**URL:** https://oj.tica.edu.vn/problem/kangaroo

---

# 🦘 Câu 4: Kangaroo

## 📘 Mô tả bài toán

Một chú **Kangaroo** muốn đi thăm một người bạn trên cùng một tuyến đường, cách đó một khoảng **n** (đơn vị dm).

Chú Kangaroo chỉ có **hai cách di chuyển**:

- **Nhảy ngắn**: mỗi bước nhảy được **a** (đơn vị dm)
- **Nhảy dài**: mỗi bước nhảy được **b** (đơn vị dm)

Biết rằng **a < b**.

Hãy xác định **ít nhất bao nhiêu bước nhảy** để chú Kangaroo có thể đến được nhà người bạn **đúng bằng n** (phải nhảy vừa đủ, **không được nhảy quá nhà bạn**).

---

## 📥 Dữ liệu vào (Input)

Dữ liệu vào được đọc từ file **`KANGAROO.INP`**:

- Gồm **ba số nguyên dương** `n`, `a`, `b` (cách nhau bởi một khoảng trắng)
- Ràng buộc:
  - `1 ≤ n ≤ 10^9`
  - `1 ≤ a < b ≤ 20`

---

## 📤 Dữ liệu ra (Output)

Ghi ra file **`KANGAROO.OUT`**:

- Một số nguyên duy nhất: **tổng số bước nhảy ít nhất** của chú Kangaroo.

---

## 🧪 Ví dụ

| KANGAROO.INP | KANGAROO.OUT |
|--------------|--------------|
| `21 2 5`     | `6`          |

---

📌 *Bài toán yêu cầu tìm cách kết hợp hai bước nhảy sao cho tổng quãng đường đúng bằng n và số bước là ít nhất.*