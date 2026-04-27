# Unknown

**URL:** https://oj.tica.edu.vn/problem/gamai

---

Trang trại gà mái - Thời gian để có đủ m quả trứng

Một trang trại có **n** con gà mái, mỗi con gà sẽ có thời gian để đẻ trứng là *a<sub>i</sub>*.  
Nghĩa là sau một khoảng thời gian là *a<sub>i</sub>* thì con gà sẽ đẻ một quả trứng. Giả sử trong đề rằng con gà mái sẽ đẻ trứng liên tục không ngừng nghỉ.

Hỏi sau ít nhất bao lâu thì trang trại sẽ có đủ **m** quả trứng.

---

## Đầu vào

- Dòng đầu tiên chứa 2 số nguyên `n`, `m` (1 ≤ n ≤ 10^5, 1 ≤ m ≤ 10^9)  
- Dòng thứ hai chứa `n` số nguyên `a1, a2, ..., an` (1 ≤ ai ≤ 10^9)

## Đầu ra

- In ra thời gian ít nhất cần phải chờ để có đủ **m** quả trứng.

---

## Ví dụ

| Input      | Output |
|------------|--------|
| `3 7`<br>`1 2 3` | `4`    |

**Giải thích:**  
- Sau 4 giây:  
  - Gà mái thứ nhất sẽ đẻ 4 quả trứng.  
  - Gà mái thứ hai sẽ đẻ ⌊4/2⌋ = 2 quả trứng.  
  - Gà mái thứ ba sẽ đẻ ⌊4/3⌋ = 1 quả trứng.  
  Tổng cộng được 4 + 2 + 1 = 7 quả trứng.