# Unknown

**URL:** https://oj.tica.edu.vn/problem/nuoica

---

# Nuôi cá cảnh

BigZero có một bể cá với đàn cá nhiều màu sắc. Hằng ngày sau những giờ học bài, cậu thường ngồi ngắm đàn cá và cho chúng ăn.  
Thức ăn của cá được đựng trong các gói đóng sẵn.

Mỗi ngày đàn cá ăn hết **đúng 3 gói**, giá bán thức ăn thường xuyên biến động.  
Cửa hàng cho biết **giá bán trong n ngày** lần lượt là:

a1, a2, ..., an

Mỗi ngày được mua **nhiều gói** với **giá bán của ngày đó**, thức ăn thừa **có thể dùng cho các ngày tiếp theo**.

BigZero đang lên kế hoạch để mua thức ăn cho đàn cá trong **n ngày sao cho tiết kiệm nhất**.

---

## Yêu cầu

Cho số nguyên dương **n** và các số nguyên dương **a1, a2, ..., an**, trong đó:

- `ai` là giá bán một gói thức ăn trong ngày thứ `i`

Hãy xác định **số tiền tối thiểu** để mua thức ăn cho đàn cá trong `n` ngày.

---

## Dữ liệu vào

Vào từ tệp văn bản **FISH.INP**:

- Dòng thứ nhất chứa một số nguyên dương `n`  
  `(1 ≤ n ≤ 10^6)`
- Dòng thứ hai chứa `n` số nguyên dương `a1, a2, ..., an`  
  `(1 ≤ ai ≤ 10^9)`

---

## Kết quả

Ghi ra tệp văn bản **FISH.OUT** một số nguyên duy nhất là **số tiền tối thiểu** để mua thức ăn cho đàn cá trong `n` ngày.

---

## Ràng buộc

- Có **30% số test** tương ứng **30% số điểm** của bài thỏa mãn:  
  `a1 ≤ a2 ≤ ... ≤ an`
- Có **30% số test khác** tương ứng **30% số điểm** của bài thỏa mãn:  
  `a1 ≥ a2 ≥ ... ≥ an`
- **40% số test còn lại** không có ràng buộc gì thêm.

---

## Ví dụ

### Ví dụ 1

**FISH.INP**
```
3
2 3 5
```

**FISH.OUT**
```
18
```

**Giải thích:**  
Ngày 1 mua 9 gói với giá 2.  
Ngày 2, 3 không mua thêm.  
Tổng tiền: `9 × 2 = 18`.

---

### Ví dụ 2

**FISH.INP**
```
3
5 3 2
```

**FISH.OUT**
```
30
```

**Giải thích:**  
Mỗi ngày mua 3 gói với giá ngày đó.  
Tổng tiền: `3×5 + 3×3 + 3×2 = 30`.

---

### Ví dụ 3

**FISH.INP**
```
3
5 2 3
```

**FISH.OUT**
```
27
```

**Giải thích:**  
- Ngày 1 mua 3 gói giá 5  
- Ngày 2 mua 6 gói giá 2  
- Ngày 3 không mua  

Tổng tiền: `3×5 + 6×2 = 27`.