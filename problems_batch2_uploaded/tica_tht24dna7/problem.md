# Unknown

**URL:** https://oj.tica.edu.vn/problem/tica_tht24dna7

---

# Bài: XOẮN ỐC ĐƯỜNG CHÉO

Cho bảng hình vuông kích thước `N x N`. Người ta điền `N x N` số đầu tiên của dãy số lẻ:

`1, 3, 5, 7, ...`

vào bảng theo hình xoắn ốc từ ngoài vào trong, theo chiều kim đồng hồ, bắt đầu từ ô góc trên bên trái.

## Yêu cầu

Hãy tính:

**hiệu giữa tổng các số trên đường chéo chính và tổng các số trên đường chéo phụ** của bảng.

Cụ thể, cần tính:

`(tổng đường chéo chính) - (tổng đường chéo phụ)`

Trong đó:
- đường chéo chính gồm các ô `(1,1), (2,2), ..., (N,N)`
- đường chéo phụ gồm các ô `(1,N), (2,N-1), ..., (N,1)`

Lưu ý:
- nếu `N` lẻ thì ô chính giữa thuộc cả hai đường chéo,
- khi tính tổng mỗi đường chéo thì ô đó vẫn được tính trong cả hai tổng như bình thường.

## Dữ liệu vào

Gồm một số nguyên dương `N`.

Giới hạn:

`1 <= N <= 10000`

## Kết quả

In ra một số nguyên là kết quả cần tìm.

## Ví dụ 1

**Input**
```text
3
```

**Output**
```text
-8
```

**Giải thích**

Bảng `3 x 3` là:

| 1  | 3  | 5  |
|----|----|----|
| 15 | 17 | 7  |
| 13 | 11 | 9  |

- Tổng đường chéo chính = `1 + 17 + 9 = 27`
- Tổng đường chéo phụ = `5 + 17 + 13 = 35`

Hiệu là:

`27 - 35 = -8`

## Ví dụ 2

**Input**
```text
4
```

**Output**
```text
-16
```

**Giải thích**

Bảng `4 x 4` là:

| 1  | 3  | 5  | 7  |
|----|----|----|----|
| 23 | 25 | 27 | 9  |
| 21 | 31 | 29 | 11 |
| 19 | 17 | 15 | 13 |

- Tổng đường chéo chính = `1 + 25 + 29 + 13 = 68`
- Tổng đường chéo phụ = `7 + 27 + 31 + 19 = 84`

Hiệu là:

`68 - 84 = -16`