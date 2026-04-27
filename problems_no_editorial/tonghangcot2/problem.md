# Unknown

**URL:** https://oj.tica.edu.vn/problem/tonghangcot2

---

Cho bảng vuông kích thước N X N . Các số tự nhiên từ 1 đến N^2 được điền lần lượt từ phải qua trái, từ trên xuống dưới.

Ví dụ, với  N = 5, bảng được điền như sau:



Cho hai số tự nhiên X và Y. Hãy tính tổng các số thuộc hàng X và các số thuộc cột Y trong bảng, sau đó in ra tổng cộng của hai tổng này.

Lưu ý: không tính trùng số tại ô giao nhau giữa hàng và cột.

### Dữ liệu nhập vào từ bàn phím:

- Dòng 1: số nguyên dương N
- Dòng 2: số nguyên dương X
- Dòng 3: số nguyên dương Y (1 <= X, Y <= N <= 10^5)


### Kết quả:
- Một dòng ghi tổng các số ở hàng X và cột Y, trừ đi số giao nhau (vì bị tính hai lần).

### Ví dụ:

### Input:


```
5
2
4

```

### Output:



```
93
```

### Giải thích:



```
Hàng 2: 10 + 9 + 8 + 7 + 6 = 40
Cột 4: 2 + 7 + 12 + 17 + 22 = 60
Giao giữa hàng 2 và cột 4 là số 7, bị tính hai lần => kết quả: 40 + 60 - 7 = 93

```