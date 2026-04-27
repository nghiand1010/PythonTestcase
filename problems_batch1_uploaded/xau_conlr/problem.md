# Unknown

**URL:** https://oj.tica.edu.vn/problem/xau_conlr

---

#  Xâu con 2

## Mô tả bài toán

Xác định **xâu con** `x` của xâu `y` trong đoạn chỉ số từ **L** tới **R**.

Cho một xâu ký tự **y** chỉ gồm các ký tự latin viết thường (có thể chứa dấu cách) và **N truy vấn**. Mỗi truy vấn gồm hai số nguyên **L, R** \((0 \le L \le R < len(y))\).

---

## Yêu cầu

Với **mỗi truy vấn**, hãy **in ra xâu con của xâu y từ chỉ số L đến chỉ số R** (tính cả L và R).

---

## Dữ liệu vào (Input)

- Dòng đầu ghi xâu **y**, có độ dài **không quá \(10^6\)** ký tự; xâu gồm các ký tự latin và chữ số.
- Dòng thứ hai ghi số nguyên **N** – số lượng truy vấn \((1 \le N \le 100)\).
- **N dòng tiếp theo**, mỗi dòng ghi hai số nguyên **L, R**.

---

## Dữ liệu ra (Output)

- Với mỗi truy vấn, in ra **xâu con của xâu y từ chỉ số L đến chỉ số R**.
- Mỗi kết quả in trên **một dòng**.

---

## Ví dụ

### Input
```
0123456
3
2 5
2 3
0 6
```

### Output
```
234
23
0123456
```