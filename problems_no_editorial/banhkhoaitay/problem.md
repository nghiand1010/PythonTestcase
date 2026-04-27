# Unknown

**URL:** https://oj.tica.edu.vn/problem/banhkhoaitay

---

Để chúc mừng sinh nhật của mình, Eris đã nướng một món bánh khoai tây dài ~n~ mét.

Hóa ra, Ben lại không thể chịu được khoai tây, nên anh ta quyết định làm hỏng bữa ăn của Eris. Anh ta đã cắt món bánh thành ~k~ miếng, có độ dài ~a_1, a_2, ..., a_k~ mét.

May mắn thay, mọi thứ đều có thể được sửa chữa. Để làm điều đó, Eris có thể thực hiện một trong các thao tác sau:

* Chọn một miếng có độ dài ~a_i ≥ 2~ và chia nó thành hai miếng có độ dài ~1~ và ~a_i - 1~.
* Chọn một miếng ~a_i~ và một miếng khác có độ dài ~a_j = 1 (i ≠ j)~ và ghép chúng thành một miếng có độ dài ~a_i + 1~.

Hãy giúp Eris tìm ra số thao tác tối thiểu mà bạn ấy cần thực hiện để ghép món bánh lại thành một miếng có độ dài ~n~.

----------

**Input:**
----------

Dòng đầu tiên chứa hai số nguyên dương, ~n~ và ~k~ (~1 ≤ n, k ≤ 100~)

Dòng tiếp theo chứa ~k~ số nguyên dương ~a_1, a_2, ..., a_k~ (~1 ≤ a_i ≤ n - k + 1~)
 
**Output:** 
----------

In ra một số nguyên dương: Số thao tác tối thiểu để ghép món bánh lại thành một miếng

**Ví dụ 1:**
----------

Input:
----------



```
5 3
3 1 1
```


Output:
----------



```
2
```


**Ví dụ 2:**
----------

Input:
----------



```
16 6
1 6 1 1 1 6
```


Output:
----------



```
15
```