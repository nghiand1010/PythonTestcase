# Unknown

**URL:** https://oj.tica.edu.vn/problem/sodacbiet4

---

# Bài toán: Số đặc biệt

## Đề bài
Một số nguyên dương được gọi là **số đặc biệt** nếu **tổng bình phương các chữ số của nó** là **một số nguyên tố**.

### Ví dụ:
- Số 12 là số đặc biệt vì \(1^2 + 2^2 = 5\) là số nguyên tố.
- Số 21 là số đặc biệt vì \(2^2 + 1^2 = 5\) là số nguyên tố.
- Số 24 **không** là số đặc biệt vì \(2^2 + 4^2 = 20\) không phải là số nguyên tố.

### Yêu cầu
Cho một số nguyên dương **n**. Hãy kiểm tra xem **n** có phải là số đặc biệt hay không và tính **tổng bình phương các chữ số** của nó.

---

## Dữ liệu đầu vào
- Một dòng duy nhất chứa số nguyên dương **n** (10 ≤ n ≤ 10¹⁸).

## Dữ liệu đầu ra
- Dòng 1: ghi ra **1** nếu n là số đặc biệt, ngược lại ghi **-1**.
- Dòng 2: ghi ra **tổng bình phương các chữ số của n**.

---

## Ví dụ
### Ví dụ 1
**Input:**
```
21
```
**Output:**
```
1
5
```
**Giải thích:** 2² + 1² = 5 là số nguyên tố → n là số đặc biệt.

---

### Ví dụ 2
**Input:**
```
24
```
**Output:**
```
-1
20
```
**Giải thích:** 2² + 4² = 20 không phải số nguyên tố → không là số đặc biệt.

---