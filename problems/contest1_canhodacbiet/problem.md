# Unknown

**URL:** https://oj.tica.edu.vn/problem/contest1_canhodacbiet

---

Có một tòa nhà gồm ~10,000~ căn hộ, được đánh số từ ~1~ đến ~10,000~.

Gọi một căn hộ là "đặc biệt" nếu số của nó bao gồm các chữ số giống nhau. Ví dụ về các căn hộ đặc biệt là ~11~, ~2~, ~777~, và ~9999~.

Một con capybara trong tòa nhà này rất quậy phá, và con capybara đấy tên là Tôm. Tôm gọi đến tất cả các căn hộ đặc biệt cho đến khi có người trả lời cuộc gọi, theo thứ tự sau:

Đầu tiên, Tôm sẽ gọi tất cả các căn hộ gồm chữ số ~1~, theo thứ tự tăng dần (~1, 11, 111, 1111~).

Sau đó, Tôm sẽ gọi tất cả các căn hộ gồm chữ số ~2~, theo thứ tự tăng dần (~2, 22, 222, 2222~).

Và cứ như thế, tiếp tục với các chữ số từ ~3~ đến ~9~.

Cư dân của căn hộ đặc biệt có số ~X~ sẽ trả lời cuộc gọi, và lúc đấy Tôm sẽ dừng lại và không gọi thêm bất kỳ căn hộ nào nữa.

Tôm muốn biết tổng của các chữ số của các số của các căn hộ mà bạn ấy đã gọi. Nhưng Tôm khá là lười, và không thích tính toán. Bạn hãy giúp Tôm tính tổng này.

Ví dụ, nếu cư dân của căn hộ đặc biệt số 22 trả lời, thì Tôm đã gọi các căn hộ có số: ~1, 11, 111, 1111, 2, 22~. Tổng của các chữ số của các số của các căn hộ là ~1 + 2 + 3 + 4 + 2 + 4 = 16~.

----------

**Input:**
----------

Nhập vào số nguyên dương ~X~ ~(1 ≤ X ≤ 9999)~

**Output:** 
----------

In ra tổng chữ số của số của các căn hộ mà Tôm đã gọi

**Ví dụ 1:**
----------

Input:
----------



```
666
```


Output:
----------



```
186
```


**Ví dụ 2:**
----------

Input:
----------



```
3333
```


Output:
----------



```
60
```