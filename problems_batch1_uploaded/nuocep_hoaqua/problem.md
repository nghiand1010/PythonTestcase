# Unknown

**URL:** https://oj.tica.edu.vn/problem/nuocep_hoaqua

---

# NƯỚC ÉP HOA QUẢ (AJUICE)

Bữa trưa ở căng-tin trường VY có:
- **a** cốc nước ép anh đào,
- **b** cốc nước ép bưởi,
- **c** cốc nước ép cam.

Mỗi học sinh khi đến sẽ lấy **một cốc nước ép**, ưu tiên theo thứ tự sau:

1. Nếu còn nước ép anh đào, học sinh sẽ lấy nước ép anh đào.
2. Nếu không còn nước ép anh đào, học sinh sẽ lấy nước ép bưởi.
3. Nếu không còn nước ép bưởi, học sinh sẽ lấy nước ép cam.
4. Nếu cả ba loại nước ép đều đã hết, học sinh sẽ không lấy cốc nào.

Sau khi **x cốc nước ép bất kỳ** đã được lấy đi, hãy xác định **mỗi loại nước ép còn lại bao nhiêu cốc**.

---

## Dữ liệu vào
- Dòng đầu tiên chứa số nguyên **a** `(0 ≤ a ≤ 1000)` — số cốc nước ép anh đào ban đầu.
- Dòng thứ hai chứa số nguyên **b** `(0 ≤ b ≤ 1000)` — số cốc nước ép bưởi ban đầu.
- Dòng thứ ba chứa số nguyên **c** `(0 ≤ c ≤ 1000)` — số cốc nước ép cam ban đầu.
- Dòng thứ tư chứa số nguyên **x** `(0 ≤ x ≤ a + b + c)` — tổng số cốc nước ép đã được lấy đi.

---

## Kết quả
- Gồm **3 dòng**, mỗi dòng ghi một số nguyên:
  - Dòng 1: số cốc nước ép anh đào còn lại  
  - Dòng 2: số cốc nước ép bưởi còn lại  
  - Dòng 3: số cốc nước ép cam còn lại

---

## Subtask

| Subtask | Ràng buộc bổ sung | Điểm |
|--------|------------------|------|
| 1 | x = 1 | 20% |
| 1 | x ≤ c | 30% |
| 2 | Không có ràng buộc bổ sung | 50% |

---

## Ví dụ

### Ví dụ 1
**Input**
```
3
2
1
2
```

**Output**
```
1
2
1
```

**Giải thích:**  
2 cốc đầu tiên học sinh lấy là nước ép anh đào, còn lại 1 cốc anh đào, 2 cốc bưởi và 1 cốc cam.

---

### Ví dụ 2
**Input**
```
3
2
1
3
```

**Output**
```
0
2
1
```

**Giải thích:**  
3 học sinh đầu lấy hết 3 cốc nước ép anh đào, còn lại 0 anh đào, 2 bưởi và 1 cam.