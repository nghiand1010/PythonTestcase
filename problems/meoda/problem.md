# Unknown

**URL:** https://oj.tica.edu.vn/problem/meoda

---

# Mèo đá cục len

Green có một đàn mèo gồm **n** con.

Cứ mỗi buổi chiều, Green sẽ cho các con mèo ngồi thành một hàng ngang, đánh số từ **1** đến **n** từ trái sang phải. Green sẽ đưa con mèo số **1** (bên trái nhất) một cục len. Con mèo số 1 sẽ bắt đầu đá cục len cho con mèo số **2**, con mèo số **2** khi nhận được cục len sẽ đá sang cho con mèo số **3**, ..., cho đến khi con mèo số **n** nhận được cục len sẽ đá ngược lại về cho con mèo số **n - 1**.

Các con mèo sẽ đá cục len theo hướng ngược lại với hướng mà nó nhận được cục len, trừ **2** con mèo ở hai đầu của hàng. Mỗi lần đá cục len sẽ mất **1 giây** để cục len lăn tới con mèo tiếp theo.
 
Green sẽ cho **n** con mèo chơi trong **k** giây. Để tiết kiệm thời gian đi tìm và thu hồi cục len, Nam sẽ cố gắng tính trước sau **k** giây thì **con mèo số mấy** sẽ giữ cục len để đi thẳng ra lấy.

## Yêu cầu
Hãy tìm **số hiệu của con mèo** giữ cục len sau **k** giây.

## Input
Một dòng duy nhất chứa hai số nguyên dương `n, k` (*2 ≤ n ≤ 10^15*, *1 ≤ k ≤ 10^15*).

## Output
Gồm **1 dòng duy nhất** chứa một **số nguyên dương** là **số hiệu của con mèo** giữ cục len sau **k** giây.