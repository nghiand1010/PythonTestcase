# Unknown

**URL:** https://oj.tica.edu.vn/problem/stickers

---

# STICKERS



![](/martor/bba1e57b-30d0-47e0-b39f-7de82174b812.png)


---

## Yêu cầu

Cho hai dãy số **T** và **S** (mỗi dãy gồm các chữ số từ 0 đến 9, độ dài không quá \(10^5\)).

Hãy tính **số lượng dãy số S có thể tạo được nhiều nhất** bằng cách sử dụng các chữ số từ dãy **T**, với quy ước:

- Sticker **2** có thể dùng thay cho **5** và ngược lại
- Sticker **6** có thể dùng thay cho **9** và ngược lại
- Các sticker khác **không thay thế cho nhau**

---

## Input

Từ tập tin văn bản **STICKERS.INP**

- Dòng thứ nhất chứa dãy số **T**
- Dòng thứ hai chứa dãy số **S**

---

## Output

Ghi ra tập tin văn bản **STICKERS.OUT** một số nguyên duy nhất là **số lượng dãy số S tạo được nhiều nhất**.

---

## Ví dụ

### Ví dụ 1
**Input**
```
4444223
445
```

**Output**
```
2
```

### Ví dụ 2
**Input**
```
668888
899
```

**Output**
```
1
```

---

## Ghi chú

- Mỗi sticker chỉ được sử dụng **một lần**
- Có thể **lật ngược** sticker 2 ↔ 5 và 6 ↔ 9 để thay thế cho nhau
- Bài toán phù hợp với tư duy **Toán → Tin**, sử dụng thuật toán **Greedy + đếm tần suất**