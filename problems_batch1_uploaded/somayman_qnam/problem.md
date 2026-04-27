# Unknown

**URL:** https://oj.tica.edu.vn/problem/somayman_qnam

---

# SỐ MAY MẮN

Công ty Tin học ACB tổ chức buổi hội thảo nhằm giới thiệu phần mềm mới của công ty. Buổi hội thảo có **N** khách mời tham dự và trên mỗi ghế ngồi có ghi số ghế là **M**.

Trước khi kết thúc hội thảo, công ty yêu cầu các khách mời tự tìm cho mình một **số cuối cùng** dựa trên số ghế mình ngồi.  
*Số cuối cùng* được xác định như sau:  
- Tính **tổng các chữ số** của số ghế đó.  
- Sau đó lại tiếp tục tính tổng các chữ số của số mới tạo được.  
- Lặp lại cho đến khi chỉ còn **một chữ số duy nhất**.

Sau khi kết thúc hội thảo, công ty tổ chức trao quà cho các khách mời có **số cuối cùng trùng với số may mắn**.  
*Số may mắn* là số có **số lượng số cuối cùng nhiều nhất** do các khách mời tìm được.

**Ví dụ:**  
Số ghế `M = 29` thì số cuối cùng được tạo ra là `2`  
(29 → 11 → 2)

---

## Yêu cầu
Gọi **K** là số may mắn. Hãy tìm số may mắn đó.  
(Nếu có nhiều số có cùng số lượng số cuối cùng bằng nhau thì **chọn số cuối cùng có giá trị nhỏ nhất**).

---

## Dữ liệu vào (LUCKY.INP)
- Dòng thứ nhất là số **N** `(1 ≤ N ≤ 10^5)`  
- **N** dòng tiếp theo, mỗi dòng là số ghế **M** của một khách mời `(0 ≤ M ≤ 10^9)`

---

## Dữ liệu ra (LUCKY.OUT)
- Gồm một số **K** cần tìm

---

## Ví dụ

### Input (LUCKY.INP)
```
5
0
3
29
21
20
```

### Output (LUCKY.OUT)
```
2
```