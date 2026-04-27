# Unknown

**URL:** https://oj.tica.edu.vn/problem/tica_git135

---

## Đề bài

Cho số nguyên dương `a` có `N` chữ số và dãy số `s` có `M` chữ số. Chữ số ở vị trí `j` (`1 ≤ j ≤ M`) của dãy `s` có thể chọn bất kỳ vị trí `i` (`1 ≤ i ≤ N`) trong số `a` và thay thế bằng `s_j`. Mỗi chữ số của dãy `s` chỉ được thay thế không quá một lần.

Nhiệm vụ của bạn là hãy tìm cách thay thế sao cho số `a` đạt giá trị lớn nhất. Bạn có thể không cần sử dụng tất cả các chữ số trong `s`.

## Input

- Dòng đầu tiên chứa số nguyên dương `a` có độ dài `N` (không bắt đầu bằng chữ số 0).
- Dòng thứ hai chứa dãy `s` có độ dài `M`.

**Ràng buộc:**
- `1 ≤ N, M ≤ 100.000`

## Output

In ra số `a` lớn nhất có thể đạt được sau khi thay thế.

## Ví dụ

### Input

```
1024
010
```

### Output

```
1124
```

### Input

```
987
1234567
```

### Output

```
987
```