# Unknown

**URL:** https://oj.tica.edu.vn/problem/tica_tht24tka4

---

Một cửa hàng sữa đang có bán loại sữa 1 lít chứa trong hộp giấy với giá A
 đồng và 1 lít chứa trong chai thủy tinh với giá B
 đồng. Nhằm hạn chế rác thải nên nếu khách hàng trả lại chai thủy tinh rỗng cho cửa hàng thì sẽ nhận lại C đồng ~(C<B)~.

**Yêu cầu:** Tom có N
 đồng và nhờ các bạn tính xem số lít sữa nhiều nhất mà bạn ấy có thể mua.

##INPUT
1 dòng gồm 4 số nguyên N,A,B,C
 cách nhau bởi dấu cách.

##OUTPUT
Số lít sữa nhiều nhất mà Tom mua.



## Subtask
1≤N,A≤1000000000000000000

1≤C<B≤1000000000000000000



## Sample Input 1


```
10 11 9 8

```
##Sample Output 1


```
2
```

##Giải thích 1
Tom có thể mua 1
 chai thủy tinh, sau đó trả lại và mua thêm 1
 chai thủy tinh. Như vậy Tom sẽ mua được 2
 lít

##Sample Input 2


```
10 5 6 1
```

##Sample Output 2


```
2
```

##Giải thích 2
Tom có thể mua 1 trong 2 cách:

* Mua 2 hộp giấy
* hoặc: mua 1 chai thủy tinh, sau đó trả lại và mua một hộp giấy => Cả 2 cách đều mua được 2 lít.