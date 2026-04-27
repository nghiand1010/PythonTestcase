# Unknown

**URL:** https://oj.tica.edu.vn/problem/cachnhiet

---

# Cách nhiệt

## Mô tả
Cho một dãy **n** viên gạch lần lượt có độ cách nhiệt là các số **a₁, a₂, …, aₙ**.

Nếu xếp các viên gạch theo một thứ tự nào đó, độ cách nhiệt của cả khối được tính theo công thức:

\[
A = a_1 + a_2 + \dots + a_n
    + \max(0, a_2 - a_1)
    + \max(0, a_3 - a_2)
    + \dots
    + \max(0, a_n - a_{n-1})
\]

## Yêu cầu
Nhiệm vụ của em là **tìm cách sắp xếp các viên gạch** sao cho **độ cách nhiệt của cả khối là lớn nhất có thể**.

---

## Dữ liệu đầu vào
Gồm **hai phần**:

- Dòng đầu ghi số nguyên dương **n** \((0 < n \le 10^5)\).
- **n dòng tiếp theo**, mỗi dòng ghi một số nguyên dương **aᵢ** \((1 \le aᵢ \le 10000)\).

---

## Dữ liệu đầu ra

- Gồm **một dòng duy nhất**, ghi ra **giá trị độ cách nhiệt lớn nhất** tìm được.

---

## Ví dụ

### Ví dụ 1

**Input**
```
4
5
4
1
7
```

**Output**
```
24
```

---

## Ghi chú
- Thứ tự ban đầu của các viên gạch **có thể thay đổi**.
- Cần chọn cách sắp xếp sao cho tổng các phần tăng thêm \(\max(0, a_i - a_{i-1})\) là lớn nhất.
- Bài toán yêu cầu thuật toán tối ưu, phù hợp với giới hạn **n lớn (lên đến 10⁵)**.