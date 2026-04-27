# Unknown

**URL:** https://oj.tica.edu.vn/problem/contest1_caudo

---

Một bạn của con capybara Moon đã thách bạn ấy tham gia một trò chơi. Trong trò chơi này, Moon sẽ nhận được một mảng các số nguyên dương có độ dài ~N~: ~a_1, a_2, a_3, ..., a_N~.


Moon có thể thực hiện thao tác sau đây trên mảng bất kỳ số lần nào:

- Lấy hai chỉ số ~i~ và ~j~ (~1 ≤ i < j ≤ N~)
- Chọn hai số nguyên dương ~x~ và ~y~ sao cho ~x * y~ = ~a_i * a_j~
- Thay ~a_i~ bằng ~x~ và ~a_j~ bằng ~y~.

Cuối cùng, Moon sẽ nhận được số tiền bằng tổng các phần tử của mảng cuối cùng. Moon muốn nhận được số tiền tối đa có thể. Tuy nhiên, Moon không thông minh lắm, nên bạn ấy không chắc liệu câu trả lời của mình có phải là tối đa hay không. Hãy giúp Moon tính số tiền tối đa mà bạn ấy có thể nhận được.

----------

**Input:**
----------

Dòng đầu tiên chứa một số nguyên dương ~N~ (~1 ≤ N ≤ 20~)

Dòng tiếp theo chứa ~N~ số nguyên dương ~a_1, a_2, a_3, ..., a_N~ (~1 ≤ a_i ≤ 50~)
 
**Output:** 
----------

In ra số tiền tối đa Moon có thể nhận được

**Ví dụ 1:**
----------

Input:
----------



```
3
2 3 2
```


Output:
----------



```
14
```


**Ví dụ 2:**
----------

Input:
----------



```
13
1 4 8 3 8 9 2 5 4 10 2 7 9
```


Output:
----------



```
348364812
```