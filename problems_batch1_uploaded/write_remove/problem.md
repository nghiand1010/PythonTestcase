# Unknown

**URL:** https://oj.tica.edu.vn/problem/write_remove

---

# VIẾT RỒI XOÁ (WNE)

## Mô tả bài toán

Hai bạn **Tí** và **Tèo** cùng chơi một trò chơi như sau:

- Ban đầu trên bảng đã được xoá, **không còn một số nào**.
- Tí và Tèo thực hiện **n lượt chơi**.

Ở lượt chơi thứ `i` (`1 ≤ i ≤ n`):

- Tí đọc to một số nguyên `A_i`.
- Tèo kiểm tra trên bảng:
  - Nếu **chưa có** số `A_i` trên bảng, Tèo **viết số `A_i` lên bảng**.
  - Nếu **đã có** số `A_i` trên bảng, Tèo **xoá tất cả các số `A_i`** đã viết trên bảng.

Sau khi kết thúc trò chơi, hãy cho biết **trên bảng còn lại bao nhiêu số**.

---

## Dữ liệu vào

Đọc từ tệp văn bản **`WNE.INP`**:

- Dòng 1: Số nguyên `n` (`1 ≤ n ≤ 10^5`) – số lượt chơi.
- `n` dòng tiếp theo, mỗi dòng ghi một số nguyên `A_i`  
  (`1 ≤ A_i ≤ 10^9`), là số Tí đọc ở lượt chơi thứ `i`.

---

## Dữ liệu ra

Ghi ra tệp văn bản **`WNE.OUT`** **một số nguyên duy nhất** –  
**số lượng các số còn lại trên bảng sau `n` lượt chơi**.

---

## Subtasks

| STT | Điểm | Ràng buộc |
|----|------|-----------|
| 1 | 25% | `n ≤ 10` |
| 2 | 25% | `n ≤ 2000` |
| 3 | 50% | Không có ràng buộc bổ sung |

---

## Ví dụ

### Input
```
3
1
2
1
```

### Output
```
1
```

### Giải thích

- Sau lượt 1: Bảng có `{1}`  
- Sau lượt 2: Bảng có `{1, 2}`  
- Sau lượt 3: Bảng có `{2}`  

Cuối cùng, trên bảng chỉ còn **1 số**.

---

## Ghi chú

- Mỗi số nếu xuất hiện **lẻ lần** thì còn trên bảng.
- Mỗi số nếu xuất hiện **chẵn lần** thì bị xoá hết.
- Bài toán phù hợp với tư duy **Toán → Tin**, sử dụng cấu trúc dữ liệu **Set**.