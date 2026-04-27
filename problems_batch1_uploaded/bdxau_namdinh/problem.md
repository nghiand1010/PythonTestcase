# Unknown

**URL:** https://oj.tica.edu.vn/problem/bdxau_namdinh

---

# Câu 5: Biến đổi xâu

Cho xâu **S** gồm các kí tự thuộc tập `{1, 2, 3, 4, 5, 6, 7, 8, 9}`.
Bước 1, biến đổi xâu **S** thành xâu **S₁**.
Bước 2, biến đổi xâu **S₁** thành xâu **S₂**...
Bước **n**, biến đổi xâu **Sₙ₋₁** thành xâu **Sₙ**.

Quy tắc biến đổi như sau:
Ở mỗi bước, mỗi kí tự **'k'**, ở đúng vị trí đó của xâu, được thay thế
bằng **k** kí tự **'k'** liên tiếp.
Vị trí của kí tự trong xâu được đánh số bắt đầu từ **1**.

**Ví dụ:**
S = `"123"` → S₁ = `"122333"` → S₂ = `"12222333333333"`
Kí tự ở vị trí thứ **5** của xâu **S₂** là **2**.

------------------------------------------------------------------------

## Yêu cầu

Cho xâu **S** và hai số nguyên dương **n, i**.
Tìm kí tự thứ **i** của xâu **Sₙ**.

------------------------------------------------------------------------

## Dữ liệu vào

Từ tệp **BIENDOI.INP** gồm hai dòng: - Dòng thứ nhất chứa xâu **S**.
Chiều dài xâu **S** nằm trong đoạn `[1; 100]`. - Dòng thứ hai chứa hai
số nguyên dương **n, i** `(1 ≤ n, i ≤ 10^6)`, các số cách nhau bởi dấu
cách.

------------------------------------------------------------------------

## Lưu ý

-   Dữ liệu đầu vào đảm bảo rằng **Sₙ** có chiều dài tối thiểu là
    **i**.
-   Nếu **n < 10^6** thì dữ liệu đầu vào đảm bảo rằng xâu **Sₙ** có
    chiều dài không vượt quá **10^6** kí tự.
-   Nếu **n = 10^6** thì không có giới hạn gì thêm.

------------------------------------------------------------------------

## Kết quả

Đưa ra tệp **BIENDOI.OUT** gồm 1 dòng chứa kí tự thứ **i** của xâu
**Sₙ**.

------------------------------------------------------------------------

## Ví dụ

**BIENDOI.INP**

    123
    2 5

**BIENDOI.OUT**

    2