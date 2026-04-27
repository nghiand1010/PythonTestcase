# Unknown

**URL:** https://oj.tica.edu.vn/problem/sokhao_tongdayso4

---

# Đề bài: Tổng các số trong dãy nhóm 8

Cho dãy số vô hạn được sắp xếp theo quy luật sau:

\[
1, 2, 3, 4, 8, 7, 6, 5,\ 9, 10, 11, 12, 16, 15, 14, 13,\ 17, 18, 19, 20, 24, 23, 22, 21,\dots
\]

Ta thấy dãy được chia thành các **nhóm 8 số liên tiếp**:

- Nhóm 1: `1 2 3 4 8 7 6 5`
- Nhóm 2: `9 10 11 12 16 15 14 13`
- Nhóm 3: `17 18 19 20 24 23 22 21`

Trong mỗi nhóm 8 số:

- 4 số đầu giữ nguyên thứ tự tăng dần
- 4 số cuối viết theo thứ tự giảm dần

## Yêu cầu

Cho hai số nguyên dương `L` và `R`.  
Hãy tính tổng các số từ vị trí `L` đến vị trí `R` của dãy trên.

## Dữ liệu vào

Gồm hai số tự nhiên `L` và `R` (`1 ≤ L ≤ R ≤ 10^8`), mỗi số trên một dòng.

## Kết quả

In ra một số nguyên duy nhất là tổng cần tìm.

## Chấm điểm

- Có 50% số test ứng với 50% số điểm với `R ≤ 10^5`
- 50% số test còn lại không có ràng buộc gì thêm

## Ví dụ

### Sample Input

```text
3
10
```

### Sample Output

```text
52
```

## Giải thích ví dụ

Dãy bắt đầu là:

```text
1, 2, 3, 4, 8, 7, 6, 5, 9, 10, ...
```

Các số từ vị trí `3` đến vị trí `10` là:

```text
3, 4, 8, 7, 6, 5, 9, 10
```

Tổng là:

\[
3 + 4 + 8 + 7 + 6 + 5 + 9 + 10 = 52
\]