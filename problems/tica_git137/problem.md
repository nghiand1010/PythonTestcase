# Unknown

**URL:** https://oj.tica.edu.vn/problem/tica_git137

---

## Đề bài

FJ suy nghĩ rằng dãy các con bò này sẽ càng ấn tượng hơn nếu như có một nhóm các con bò có cùng mã giống đứng cạnh nhau. Để thực hiện được điều này, FJ quyết định loại bỏ những con bò có mã giống được ông ta chỉ định. Hãy giúp FJ tìm ra độ dài lớn nhất của dãy các con bò có cùng mã giống mà ông ta có thể xếp được bằng cách bỏ các con bò có cùng mã giống mà ông ta chỉ định.

## Input

- Dòng đầu tiên chứa số bộ test `T`.
- Tiếp theo là `T` bộ test, mỗi bộ test có dạng:
  - Dòng 1: Số tự nhiên `N` (N ≤ 1000).
  - Dòng 2 đến dòng `N+1`: Dòng thứ `i+1` chứa số `B(i)` là mã giống của con bò thứ `i`, nằm trong khoảng 0 đến 1.000.000.

## Output

Với mỗi bộ test, in ra một dòng chứa độ dài lớn nhất của một nhóm các con bò có cùng mã giống mà FJ có thể tạo được.

## Ví dụ

### Input

```
1
9
2
7
3
7
7
3
7
5
7
```

### Output

```
4
```

**Giải thích:**

Trong dãy `7 3 7 7 3 7`, nếu FJ loại bỏ các con bò có mã giống bằng 3, ta thu được dãy `7 7 7 7` với độ dài bằng 4.