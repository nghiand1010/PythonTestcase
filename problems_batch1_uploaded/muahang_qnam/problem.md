# Unknown

**URL:** https://oj.tica.edu.vn/problem/muahang_qnam

---

# MUA HÀNG

Tâm mở một cửa hàng bán văn phòng phẩm. Trong ngày khai trương, để *mua may bán đắt*, Tâm quan niệm rằng khi khách hàng mua một sản phẩm nào đó thì phải trả **đúng số tiền của sản phẩm** để Tâm không phải trả lại tiền thừa cho khách hàng.

Nam là bạn thân của Tâm đến mua hàng. Nam hiện có **N tờ tiền**, mỗi tờ tiền **M** đều có giá trị khác nhau. Giả thiết rằng với số tiền của Nam hiện có **đều có thể mua được một số sản phẩm** trong cửa hàng.

---

## Yêu cầu
Vì Nam không quen với việc tính toán, em hãy giúp Nam tính xem với **N tờ tiền** như vậy thì Nam **không thể mua** sản phẩm có **giá trị nhỏ nhất (Min)** là bao nhiêu?

---

## Dữ liệu vào (BUY.INP)
- Dòng thứ nhất là số **N** `(0 < N ≤ 100)`  
- Dòng thứ hai gồm **N** số, mỗi số là giá trị một tờ tiền **M**, các số cách nhau một khoảng trắng `(0 < M ≤ 10^9)`

---

## Dữ liệu ra (BUY.OUT)
- Gồm **một số nguyên dương Min** cần tìm

---

## Ví dụ

### Ví dụ 1
**Input (BUY.INP):**
```
5
1 2 4 9 100
```

**Output (BUY.OUT):**
```
8
```

### Ví dụ 2
**Input (BUY.INP):**
```
3
1 2 3
```

**Output (BUY.OUT):**
```
7
```