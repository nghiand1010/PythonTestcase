# Unknown

**URL:** https://oj.tica.edu.vn/problem/vong_tay

---

# Vòng tay

Để có tiền đi chơi lễ hội trong mùa xuân năm nay, Bo quyết định làm các vòng tay để bán cho du khách.
Bo tham gia khóa học kết các vòng tay của một cửa hàng. Bo muốn ghi chép lại các kiểu kết vòng tay nên quy ước mỗi loại hạt dùng để kết vòng tay là một con số từ **1 đến 9**.

Một vòng tay được kết từ **một dãy các hạt mẫu lặp đi lặp lại k lần** và **luôn kết thúc bằng hạt cùng loại với hạt bắt đầu**.

Hãy giúp Bo tìm **số lượng các hạt trong dãy hạt mẫu** để Bo dễ dàng kết vòng tay nhé.

---

## Yêu cầu

Cho biết số lượng hạt **N** và dãy các hạt tạo thành vòng tay, hãy xác định **độ dài của dãy hạt mẫu**.

---

## Input

- Số nguyên **N** (1 ≤ N ≤ 100)
- Một dãy gồm **N số nguyên** `a_i` (1 ≤ a_i ≤ 9) biểu thị các hạt trong vòng tay

---

## Output

- Một số nguyên duy nhất là **số lượng các hạt trong dãy hạt mẫu**.

---

## Ví dụ

### Input

```
13
5 3 1 3 5 2 5 3 1 3 5 2 5
```

### Output

```
6
```

---

## Giải thích

Dãy hạt mẫu là:

```
5 3 1 3 5 2
```

Gồm **6 hạt**, dãy này được lặp lại và kết thúc bằng hạt giống hạt đầu tiên để tạo thành vòng tay.