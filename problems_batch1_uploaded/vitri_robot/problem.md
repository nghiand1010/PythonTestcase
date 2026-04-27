# Unknown

**URL:** https://oj.tica.edu.vn/problem/vitri_robot

---

## Bài 1. Vị trí robot 

### Đề bài
Một robot bắt đầu ở vị trí 0 trên trục tọa độ Ox. Robot thực hiện các bước di chuyển:

1. Bước 1: sang phải a đơn vị.  
2. Bước 2: sang trái b đơn vị.  
3. Bước 3: sang phải a đơn vị.  
4. Bước 4: sang trái b đơn vị.  

... và cứ lặp lại như vậy.

Hãy xác định vị trí cuối cùng của robot sau k bước.

### Dữ liệu (nhập từ bàn phím)
Một dòng gồm ba số nguyên a, b, k  đơn vị dịch chuyển và số bước (1 ≤ a, b, k ≤ 10^9).

### Kết quả (ghi ra màn hình)
Một dòng duy nhất là vị trí cuối cùng của robot trên trục Ox sau k bước.

### Ví dụ
| Input | Output | Giải thích |
|--------|---------|-------------|
| 5 2 3 | 8 | Robot đi: +5 (b1), -2 (b2), +5 (b3) → Tổng 5-2+5=8 |