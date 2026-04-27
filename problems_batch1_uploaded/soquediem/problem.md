# Unknown

**URL:** https://oj.tica.edu.vn/problem/soquediem

---

# SỐ QUE DIÊM – SỐ CHIA HẾT

## 📌 Mô tả
Các chữ số từ **0 đến 9** được hiển thị theo dạng **7 đoạn** và mỗi chữ số cần một số lượng **que diêm** nhất định để tạo thành.

Bảng số que diêm tương ứng với từng chữ số:

| Chữ số | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|------|---|---|---|---|---|---|---|---|---|---|
| Que diêm | 6 | 2 | 5 | 5 | 4 | 5 | 6 | 3 | 7 | 6 |

---

## 🎯 Yêu cầu
Cho các số nguyên:
- **K** – số chữ số của một số
- **M** – số cần chia hết
- **P** – điều kiện về tính chẵn / lẻ của tổng số que diêm

Hãy xác định:

> **Có bao nhiêu số có đúng K chữ số khác nhau, chia hết cho M, và tổng số que diêm dùng để tạo các chữ số là thỏa mãn điều kiện P?**

---

## 📥 Input
- Một dòng gồm ba số nguyên:
```
K M P
```
Trong đó:
- `1 ≤ K ≤ 6`
- `1 ≤ M ≤ 10`
- `P = 0` nếu yêu cầu **tổng que diêm là số chẵn**
- `P = 1` nếu yêu cầu **tổng que diêm là số lẻ**

---

## 📤 Output
- In ra **một số nguyên duy nhất** là **số lượng các số thỏa mãn yêu cầu**

---

## 📌 Điều kiện của số được tính
Một số hợp lệ nếu:
1. Có **đúng K chữ số**
2. **Các chữ số đôi một khác nhau**
3. **Chữ số đầu tiên khác 0**
4. **Chia hết cho M**
5. **Tổng số que diêm**:
   - chẵn nếu `P = 0`
   - lẻ nếu `P = 1`

---

## 🧪 Ví dụ

### Ví dụ 1
**Input**
```
3 5 0
```

**Output**
```
66
```

---

## 💡 Gợi ý thuật toán
- Duyệt tất cả các số có K chữ số (hoặc sinh hoán vị chữ số)
- Kiểm tra lần lượt các điều kiện
- Đếm số lượng thỏa mãn

---

## 🎓 Phân hóa trình độ
- 🟢 Tiểu học: cố định `K = 2` hoặc `K = 3`
- 🟡 THCS: `K = 3, 4`
- 🔴 Nâng cao: `K ≥ 4`, cần tối ưu (DP, bitmask)