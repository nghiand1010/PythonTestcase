# Unknown

**URL:** https://oj.tica.edu.vn/problem/ngaytieptheo2

---

Viết chương trình nhập vào một ngày dưới dạng chuỗi 8 ký tự số (định dạng DDMMYYYY). Tìm ngày tiếp theo của ngày vừa nhập. Nếu không tìm được ngày hợp lệ theo yêu cầu thì xuất ra "Khong tim duoc".

### Định dạng dữ liệu

- **Đầu vào**: Chuỗi 8 ký tự số liên tiếp:
  - 2 ký tự đầu: ngày (DD)
  - 2 ký tự tiếp: tháng (MM)
  - 4 ký tự cuối: năm (YYYY)

- **Đầu ra**:
  - Chuỗi 8 ký tự số biểu diễn ngày tiếp theo (DDMMYYYY)
  - Hoặc chuỗi "Khong tim duoc" nếu không hợp lệ

### Quy tắc ngày tháng

- Tháng có 31 ngày: 1, 3, 5, 7, 8, 10, 12
- Tháng có 30 ngày: 4, 6, 9, 11
- Tháng 2:
  - 28 ngày (năm thường)
  - 29 ngày (năm nhuận)

**Năm nhuận** là năm:
- Chia hết cho 4 và không chia hết cho 100
- Hoặc chia hết cho 400

### Phạm vi hợp lệ

Thời gian sử dụng trong bài từ:
- Ngày 01/01/2000
- Đến ngày 04/06/2023

Nếu ngày nhập vào nằm ngoài phạm vi này hoặc không hợp lệ, trả về "Khong tim duoc".

## Ví dụ

### Ví dụ 1

**Input**:

### Ví dụ 1

**Input**:



```
31122021
```


**Output**:


```
01012022
```


### Ví dụ 2

**Input**:



```
04062023
```


**Output**:




```
Khong tim duoc
```


## Lưu ý



```
- Chữ "Khong tim duoc" phải viết hoa chữ K đầu tiên
- Chuỗi ngày phải đúng 8 ký tự số
- Kiểm tra cả tính hợp lệ của ngày tháng năm và phạm vi cho phép
```