# Unknown

**URL:** https://oj.tica.edu.vn/problem/muahoa2

---

# Bài toán: Mua bó hoa giá trị lớn nhất (không vượt ngân sách)

**Mô tả**  
Nhân ngày Quốc tế Phụ nữ 8–3, An muốn mua một bó hoa thật có giá trị trong phạm vi số tiền mình có là `c` đồng để tặng cô giáo.  
Cửa hàng bán 2 loại hoa:
- Hoa hồng giá `a` đồng/bông.
- Hoa lay ơn giá `b` đồng/bông, với `a < b`.

**Yêu cầu**  
An muốn mua được bó hoa sao cho giá trị của bó hoa phải là lớn nhất (dĩ nhiên, không vượt quá số tiền mình hiện có).

Cho 3 số nguyên a, b, c. Hãy xác định giá trị của bó hoa An mua được.

---

## Input
Một dòng chứa ba số nguyên `a b c` (cách nhau bởi đúng một dấu cách).

**Ràng buộc**: `1 ≤ a < b ≤ 1000`, `0 ≤ c ≤ 100000`.

## Output
In ra **một số nguyên** là **tổng tiền lớn nhất** của bó hoa mà An có thể mua (không vượt `c`).

## Ví dụ
**Input**
```
2 3 11
```
**Output**
```
11
```
**Giải thích**: Mua 4 bông hồng (4×2 = 8) và 1 bông lay ơn (1×3 = 3), tổng 11 đồng.