# Unknown

**URL:** https://oj.tica.edu.vn/problem/tica_tht24dna6

---

# Bài: BẢNG XOẮN ỐC 3

Cho bảng hình vuông kích thước `N x N`. Người ta điền `N x N` số đầu tiên của dãy số lẻ:

`1, 3, 5, 7, ...`

vào bảng theo hình xoắn ốc từ ngoài vào trong, theo chiều kim đồng hồ, bắt đầu từ ô góc trên bên trái.

## Yêu cầu

Hãy tính tổng hiệu giữa số lớn nhất và số nhỏ nhất trên mỗi dòng của bảng.

## Dữ liệu vào

Gồm một số nguyên dương `N` với:

`1 <= N <= 10000`

## Kết quả

In ra một số nguyên là kết quả cần tìm.

## Ví dụ 1

**Input**
```text
4
```

**Output**
```text
50
```

**Giải thích**

Bảng `4 x 4` là:

| 1  | 3  | 5  | 7  |
|----|----|----|----|
| 23 | 25 | 27 | 9  |
| 21 | 31 | 29 | 11 |
| 19 | 17 | 15 | 13 |

Xét từng dòng:
- dòng 1: lớn nhất `7`, nhỏ nhất `1`, hiệu `6`
- dòng 2: lớn nhất `27`, nhỏ nhất `9`, hiệu `18`
- dòng 3: lớn nhất `31`, nhỏ nhất `11`, hiệu `20`
- dòng 4: lớn nhất `19`, nhỏ nhất `13`, hiệu `6`

Tổng là `6 + 18 + 20 + 6 = 50`.

## Ví dụ 2

**Input**
```text
3
```

**Output**
```text
18
```

**Giải thích**

Bảng `3 x 3` là:

| 1  | 3  | 5  |
|----|----|----|
| 15 | 17 | 7  |
| 13 | 11 | 9  |

Xét từng dòng:
- dòng 1: `5 - 1 = 4`
- dòng 2: `17 - 7 = 10`
- dòng 3: `13 - 9 = 4`

Tổng là `4 + 10 + 4 = 18`.