# Unknown

**URL:** https://oj.tica.edu.vn/problem/xenke_vongtron

---

# XEN KẼ VÒNG TRÒN

## Mô tả
Cho một xâu ký tự **vòng tròn** chỉ gồm các ký tự `a`, `b`, `c`, `d` và ký tự đặc biệt `?`.

- Xâu được coi là **vòng tròn**, tức là ký tự cuối có thể nối với ký tự đầu.
- Mỗi ký tự `?` có thể được thay bằng **một trong bốn ký tự** `a`, `b`, `c`, `d`.

---

## Định nghĩa đoạn con xen kẽ
Một **đoạn con liên tiếp** được gọi là **xen kẽ** nếu:

> **Hai ký tự đứng cạnh nhau không được giống nhau**.

### Ví dụ
- `abac` là đoạn xen kẽ.
- `abbc` *không* là đoạn xen kẽ (vì có hai ký tự `b` đứng cạnh nhau).

---

## Yêu cầu
Sau khi **thay các ký tự `?` một cách tối ưu** và **xét xâu theo dạng vòng tròn**, hãy tìm:

> **Độ dài lớn nhất của một đoạn con xen kẽ**.

---

## Dữ liệu vào (Input)
- Một dòng duy nhất chứa xâu `S`.
- Xâu chỉ gồm các ký tự `a`, `b`, `c`, `d` và `?`.
- Độ dài của xâu không vượt quá **100**.

---

## Dữ liệu ra (Output)
- In ra **một số nguyên duy nhất** là độ dài lớn nhất của đoạn con xen kẽ.

---

## Ví dụ
### Input
```
a?bb?a
```

### Output
```
3
```

### Giải thích
- Các ký tự `?` có thể được thay sao cho không trùng với ký tự đứng cạnh.
- Đoạn xen kẽ dài nhất (xét theo vòng tròn) có độ dài là **3**.

---

## Ghi chú
- Ký tự `?` luôn có thể chọn thành ký tự khác để tránh trùng lặp.
- Đoạn con xen kẽ không được dài hơn độ dài xâu ban đầu.

---