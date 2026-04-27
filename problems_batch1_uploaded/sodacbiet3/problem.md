# Unknown

**URL:** https://oj.tica.edu.vn/problem/sodacbiet3

---

# 🧮 Bài toán: Số đặc biệt

Một số nguyên dương được gọi là **số đặc biệt** nếu tổng bình phương các chữ số của số đó là một **số nguyên tố**.

### Ví dụ:
- Số 12 là số đặc biệt vì 1² + 2² = 5 là số nguyên tố.
- Số 21 là số đặc biệt vì 2² + 1² = 5 là số nguyên tố.
- Số 24 không phải là số đặc biệt vì 2² + 4² = 20 không phải là số nguyên tố.

### Yêu cầu:
Cho một số nguyên dương `n`. Hãy kiểm tra xem `n` có phải là số đặc biệt hay không và tính tổng bình phương các chữ số của nó.

### Dữ liệu vào:
- Một dòng duy nhất chứa số nguyên dương `n` (10 ≤ n ≤ 10¹⁸).

### Dữ liệu ra:
- Dòng đầu ghi ra `1` nếu `n` là số đặc biệt, ngược lại ghi `-1`.
- Dòng thứ hai ghi ra tổng bình phương các chữ số của `n`.

### Ví dụ:
#### Input 1
```
21
```
#### Output 1
```
1
5
```
#### Input 2
```
24
```
#### Output 2
```
-1
20
```