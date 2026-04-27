# Unknown

**URL:** https://oj.tica.edu.vn/problem/dembanco

---

# DEMO Đếm ô

## Đề bài
Cho bàn cờ vua kích thước N × N gồm N hàng và N cột. Các hàng được đánh số từ trên xuống dưới, các cột được đánh số từ trái sang phải. Ô tại vị trí (1, 1) là ô đen. Các ô kề nhau (ngang hoặc dọc) có màu xen kẽ trắng – đen.

![](/martor/d12f27d3-5356-4131-9d9a-1f374fdf338c.png)

### Yêu cầu
Cho tọa độ của hai ô: (x₁, y₁) và (x₂, y₂), là góc trên bên trái và góc dưới bên phải của một hình chữ nhật. Tính số ô đen và số ô trắng nằm trong hình chữ nhật đó.

### Dữ liệu đầu vào
Gồm 5 dòng, mỗi dòng là một số tự nhiên:
1. Một số tự nhiên N là kích thước bàn cờ (1 ≤ N ≤ 10⁹).
2. Một số tự nhiên x₁ là chỉ số hàng của ô trên bên trái.
3. Một số tự nhiên y₁ là chỉ số cột của ô trên bên trái.
4. Một số tự nhiên x₂ là chỉ số hàng của ô dưới bên phải (1 ≤ x₁, y₁, x₂, y₂ ≤ N, và x₁ ≤ x₂, y₁ ≤ y₂).
5. Một số tự nhiên y₂ là chỉ số cột của ô dưới bên phải.


### Dữ liệu đầu ra
Gồm 2 dòng, mỗi dòng là một số tự nhiên:
- Dòng 1: số lượng ô đen.
- Dòng 2: số lượng ô trắng.

### Ràng buộc
- 30% test với N ≤ 100.
- 30% test với x₁ = x₂.
- 40% test không có giới hạn thêm.


### Ví dụ
#### Input
```
7
2
3
6
5
```
#### Output
```
7
8
```
Giải thích: Hình chữ nhật gồm 15 ô, có 7 ô đen và 8 ô trắng.

---
#### Input
```
5
1
1
5
5
```
#### Output
```
13
12
```
Giải thích: Cả bàn cờ 5×5 có 25 ô, bắt đầu bằng ô (1,1) đen ⇒ 13 đen, 12 trắng.