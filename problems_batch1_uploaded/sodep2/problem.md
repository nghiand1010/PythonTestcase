# Unknown

**URL:** https://oj.tica.edu.vn/problem/sodep2

---

# Bài toán: SỐ ĐẸP

## Đề bài

Bình và An đang học luyện thi, gặp một bài toán thú vị về **"Số đẹp"**. Một số được gọi là **số đẹp** nếu **không có chữ số 0 ở tận cùng**.

Cho hai số nguyên dương **a** và **b** (với a < b). Gọi:

S = a × (a + 1) × (a + 2) × ... × b 

Hãy cho biết **số lượng chữ số 0 ở tận cùng** của S — tức là cần xóa bao nhiêu chữ số 0 ở cuối để S trở thành một số đẹp.

### Ví dụ:
Với a = 4, b = 15 thì:
S = 4 × 5 × 6 × ... × 15 = 217945728000 
→ Có **3 chữ số 0 ở cuối**, nên kết quả là **3**.

---

## Dữ liệu vào
- Dòng đầu tiên chứa số nguyên **T** (1 ≤ T ≤ 10⁵) — số lượng bộ test.
- T dòng tiếp theo, mỗi dòng gồm hai số nguyên dương **a, b** (1 ≤ a < b ≤ 10¹⁶).

## Dữ liệu ra
- Gồm **T dòng**, mỗi dòng in ra **số lượng chữ số 0 tận cùng** của tích S tương ứng.
- Kết quả rất lớn nên cần in ra **phần dư chia cho 10⁹ + 7**.

---

## Giải thích
Một số có chữ số 0 ở cuối nếu chia hết cho 10. Mà **10 = 2 × 5**, nên số chữ số 0 ở cuối bằng số lượng **cặp (2,5)** trong phân tích thừa số của S.

---

## Ví dụ minh họa
| Input | Output | Giải thích |
|--------|---------|-------------|
| 1 6 | 1 | Tích 1×2×3×4×5×6 = 720 → 1 số 0 cuối |
| 1 10 | 2 | Tích 1×...×10 = 3628800 → 2 số 0 cuối |
| 2 4 | 0 | Tích 2×3×4 = 24 → không có số 0 cuối |
| 10 20 | 3 | Tích 10×...×20 có 3 số 0 cuối |

---

## Giới hạn
- 40% test: 1 ≤ T ≤ 10, a, b ≤ 10¹⁸
- 30% test: T = 1, a, b ≤ 10⁵
- 20% test: 1 ≤ T ≤ 10⁴, a, b ≤ 10⁵
- 10% test: 10⁴ < T ≤ 10⁵, a, b ≤ 10¹⁶