# Unknown

**URL:** https://oj.tica.edu.vn/problem/qninh_bdxau

---

# Biến đổi Xâu

Cho một xâu ký tự **S** chỉ bao gồm các chữ cái tiếng anh viết thường từ `a` đến `z`.

Một xâu được gọi là *hợp lệ* nếu trong xâu đó không có bất kỳ 3 ký tự liên tiếp nào giống hệt nhau (ví dụ: các cụm `aaa`, `bbb`, `zzz` là không hợp lệ).

## Yêu cầu

Hãy tìm số lần thay đổi ký tự ít nhất để biến xâu **S** ban đầu thành một xâu *hợp lệ*.

## Dữ liệu

- Một dòng chứa xâu **S** có độ dài **N** (`3 ≤ N ≤ 10^5`)

## Kết quả

- Một số nguyên duy nhất là số lần thay đổi ký tự ít nhất.

## Ví dụ 1

### Nhập vào

```text
aaabbb
```

### In ra

```text
2
```

### Giải thích

- Thay đổi 1 ký tự `a` và 1 ký tự `b`.

## Ví dụ 2

### Nhập vào

```text
aabcc
```

### In ra

```text
0
```