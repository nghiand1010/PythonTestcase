# Unknown

**URL:** https://oj.tica.edu.vn/problem/rutthe2

---

# Trò chơi rút thẻ (phiên bản đơn giản từ Codeforces 381A)

## Mô tả bài toán

Có **N** tấm thẻ được đánh số từ **1 đến N**, xếp theo thứ tự từ trái sang phải:

```
1, 2, 3, ..., N-1, N
```

Hai bạn **Sereja** và **Dima** lần lượt chơi một trò chơi với các tấm thẻ này.

- Sereja là người chơi trước.
- Ở mỗi lượt, người chơi được rút **một tấm thẻ** ở:
  - Bên **trái ngoài cùng**, hoặc
  - Bên **phải ngoài cùng** của dãy.
- Cả hai bạn đều chơi theo chiến thuật **tham lam**:
  - Luôn chọn tấm thẻ có **giá trị lớn hơn** trong hai tấm ở hai đầu.
- Giá trị trên tấm thẻ được cộng vào **tổng điểm** của người chơi.
- Trò chơi kết thúc khi **không còn tấm thẻ nào**.

## Yêu cầu

Hãy tính **tổng điểm của Sereja và Dima** sau khi trò chơi kết thúc.

---

## Dữ liệu vào (INPUT)

- Một số nguyên dương **N**  
  1 ≤ N ≤ 10⁹

## Kết quả (OUTPUT)

- In ra **hai số nguyên**:
  - Tổng điểm của **Sereja**
  - Tổng điểm của **Dima**

---

## Ví dụ

### Ví dụ 1

**Input**
```
4
```

**Output**
```
6 4
```

### Ví dụ 2

**Input**
```
5
```

**Output**
```
9 6
```

---

## Ghi chú

- Không cần sử dụng mảng để lưu dãy thẻ.
- Có thể khai thác quy luật của dãy số từ **1 đến N** để giải bài toán với độ phức tạp **O(1)**.
- Bài toán được xây dựng dựa trên ý tưởng của bài **Codeforces 381A – Sereja and Dima**, nhưng đã được đơn giản hóa.