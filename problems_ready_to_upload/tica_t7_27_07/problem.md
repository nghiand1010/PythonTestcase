# Unknown

**URL:** https://oj.tica.edu.vn/problem/tica_t7_27_07

---

![](/martor/1415b121-34fc-4944-b381-579f2e80a9a1.png)

Gợi ý:
Cho 2 số A và B. Xem số nào nhỏ hơn theo dạng xâu ký tự.
Ví dụ: A = 14, B = 2
thì số A chưa ký tự 1 sẽ nhỏ hơn là số B

Gọi x là số lần xuất hiện số A
Gọi y là số lần xuất hiện số B

Ta có số lần xuất hiện x, y tối đa là 9
Vậy for x in range(1, 10):
for y in range(1, 10)

==> tạo ra 1 số number với số lần x, y xuất hiện
==> kiểm tra number có chia hết cho 9
==> thêm number vào 1 danh sách kết quả
==> tìm min của danh sách kết quả.

#Test case mẫu
##Đầu vào mẫu 1


```
14
2
```

##Đầu ra mẫu 1


```
1422
```

##Đầu vào mẫu 2


```
9
3
```

##Đầu ra mẫu 2


```
3339
```