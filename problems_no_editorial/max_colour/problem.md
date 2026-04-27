# Unknown

**URL:** https://oj.tica.edu.vn/problem/max_colour

---

# Tối đa hóa số lượng màu

## Đề bài
Đối với mắt người, ba màu cơ bản là **đỏ**, **xanh lá cây**, và **xanh dương**.

Khi trộn 1 giọt của **bất kỳ hai màu cơ bản** nào, ta sẽ tạo ra một loại màu phụ mới.  
Ví dụ: 
- Trộn đỏ và xanh lá → vàng  
- Trộn xanh lá và xanh dương → lục lam (cyan)  
- Trộn đỏ và xanh dương → đỏ tím (magenta)

Bạn có **X, Y, Z** giọt màu đỏ, xanh lá và xanh dương tương ứng. Hãy tìm số lượng tối đa các **màu phân biệt** (bao gồm cả màu cơ bản và màu phụ) mà bạn có thể tạo ra tại một thời điểm.

⚠️ **Lưu ý**: Không thể tiếp tục trộn màu phụ với màu cơ bản hay màu phụ khác để tạo thêm màu mới.

---

## Input Format
- Dòng đầu tiên chứa một số nguyên **T**, số lượng test case.  
- Mỗi test case gồm 3 số nguyên **X, Y, Z** – số giọt màu đỏ, xanh lá, xanh dương tương ứng.

## Output Format
Với mỗi test case, in ra trên một dòng số lượng tối đa màu **phân biệt** có thể có.

---

## Ràng buộc
- 1 ≤ T ≤ 10^5  
- 0 ≤ X, Y, Z ≤ 100  

---

## Ví dụ

**Input**
```
4
1 0 1
3 3 0
1 1 1
0 0 0
```

**Output**
```
2
3
3
0
```

---

## Giải thích

**Test case 1:** Có 1 giọt đỏ và 1 giọt xanh dương. Nếu trộn, ta được đỏ tím (magenta) nhưng mất đỏ và xanh dương → chỉ còn 1 màu. Giữ nguyên thì có 2 màu khác nhau. Kết quả = 2.

**Test case 2:** Có 3 giọt đỏ và 3 giọt xanh lá. Có thể trộn để tạo thêm màu vàng → lúc này có 3 loại màu (đỏ, xanh lá, vàng). Kết quả = 3.

**Test case 3:** Nếu trộn bất kỳ, sẽ mất 2 màu cơ bản và chỉ thêm 1 màu phụ → tổng số loại không tăng. Do đó giữ nguyên cả 3 màu cơ bản. Kết quả = 3.

**Test case 4:** Không có giọt màu nào → 0 màu.