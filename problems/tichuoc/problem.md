# Unknown

**URL:** https://oj.tica.edu.vn/problem/tichuoc

---

**Bài toán: Tích các ước số chẵn**

**Đề bài**

Cho số nguyên dương N (\(1 < N < 250\)). Một số M) được gọi là **ước số chẵn** của N nếu thỏa mãn ba điều kiện:

1. N chia hết cho M;  
2. M là số chẵn;  
3. 0 < M < N.

Yêu cầu: Tìm tích của tất cả các ước số chẵn của N. Nếu không có ước số chẵn nào thỏa mãn, in ra 0.

---

**Dữ liệu đầu vào**

- Gồm duy nhất số nguyên dương N (1 < N < 250).

**Dữ liệu đầu ra**

- Gồm một số nguyên duy nhất là đáp án của bài toán (tích của các ước số chẵn của N, hoặc 0 nếu không có ước số chẵn nào.

---

**Ví dụ**

Ví dụ 1:
```
Input:
16

Output:
64
```
**Giải thích:** Các ước của 16 là 1,2,4,8,16. Các ước chẵn thỏa mãn điều kiện (chẵn và nhỏ hơn 16) là 2,4,8. Tích 2 x 4 x 8 = 64.