# Unknown

**URL:** https://oj.tica.edu.vn/problem/hsgioi

---

# Thi học sinh giỏi

## Đề bài

Một đội tuyển có **N** học sinh. Học sinh thứ i được đặc trưng bởi hai
tham số:\
- **Hệ số kỹ năng** `a_i`\
- **Chỉ số thông minh** `b_i`

Trong quá trình ôn luyện, mỗi khi giáo viên làm việc riêng với một học
sinh, hệ số kỹ năng của học sinh đó sẽ **tăng thêm đúng bằng chỉ số
thông minh** của học sinh đó.\
Tuy nhiên, do hạn chế thời gian, giáo viên chỉ có thể thực hiện **tối đa
C buổi làm việc riêng** (có thể chia cho nhiều học sinh, hoặc một học
sinh nhiều lần).

Một học sinh được coi là **đạt giải** nếu hệ số kỹ năng của em đó
**không nhỏ hơn K**.

------------------------------------------------------------------------

## Yêu cầu

Xác định **số lượng học sinh tối đa** có thể đạt giải sau khi phân bổ
tối ưu C buổi làm việc.

------------------------------------------------------------------------

## Input

-   Dòng đầu tiên chứa 3 số nguyên `N, C, K`\
    `(1 ≤ N ≤ 10³, 1 ≤ C, K ≤ 10⁹)`
-   Tiếp theo là **N dòng**, mỗi dòng chứa hai số nguyên `a_i` và `b_i`\
    `(0 ≤ a_i, b_i ≤ 10⁹)`

------------------------------------------------------------------------

## Output

In ra **một số nguyên duy nhất** --- số lượng học sinh tối đa có thể đạt
giải.

------------------------------------------------------------------------

## Ví dụ

### Input

    3 5 6
    1 1
    2 1
    4 2

### Output

    2

### Giải thích

-   Học sinh 1: cần tăng `6 - 1 = 5`, tốc độ 1 → cần 5 buổi\
-   Học sinh 2: cần tăng `6 - 2 = 4`, tốc độ 1 → cần 4 buổi\
-   Học sinh 3: cần tăng `6 - 4 = 2`, tốc độ 2 → cần 1 buổi

Tổng 5 buổi: giúp học sinh 3 và 2 đạt giải → kết quả là **2**.

------------------------------------------------------------------------

## Giới hạn

-   80% test có `C ≤ 10⁶`\
-   20% test không có ràng buộc gì thêm.