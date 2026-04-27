# Unknown

**URL:** https://oj.tica.edu.vn/problem/xau_thaythe

---

# BÀI TOÁN THAY THẾ XÂU (REPLACE)

Giả sử hàm `y.replace(x1, x2)` tạo ra một xâu mới từ xâu `y` bằng cách **thay thế xâu con `x1` của `y` bằng xâu `x2`**.  
Tất cả các xâu con bằng `x1` **không giao nhau** đều được thay bằng xâu `x2`.

---

## YÊU CẦU

Cho `Q` truy vấn, mỗi truy vấn gồm **3 dòng**:

- Dòng thứ nhất ghi xâu `y`
- Dòng thứ hai ghi xâu `x1`
- Dòng thứ ba ghi xâu `x2`

Với mỗi truy vấn, hãy in ra xâu thu được bằng cách **thay thế tất cả các xâu con `x1` trong `y` bằng `x2`**.

Việc thay thế được thực hiện từ **trái sang phải**, các xâu con được thay **không được giao nhau**.

---

## INPUT

- Dòng đầu ghi số nguyên `Q` – số truy vấn  
  `1 ≤ Q ≤ 100`
- `3 × Q` dòng tiếp theo, mỗi nhóm 3 dòng mô tả một truy vấn như trên
- Các xâu chỉ gồm **chữ thường và dấu cách**

---

## OUTPUT

- Với mỗi truy vấn, in ra **một dòng** là xâu kết quả sau khi thay thế

---

## VÍ DỤ

### Input
```
2
truc xinh truc moc dau dinh
dau dinh
bo ao
em xinh em dung mot minh cung xinh
mot minh
noi nao
```

### Output
```
truc xinh truc moc bo ao
em xinh em dung noi nao cung xinh
```

---

## GIẢI THÍCH

- Ở truy vấn 1:
  - Xâu `dau dinh` trong xâu `y` được thay bằng `bo ao`
- Ở truy vấn 2:
  - Xâu `mot minh` được thay bằng `noi nao`
- Các lần xuất hiện của `x1` **không bị chồng lấn** khi thay thế

---

## GỢI Ý

- Duyệt xâu `y` từ trái sang phải
- Nếu tại vị trí đang xét xuất hiện `x1`:
  - Thay bằng `x2`
  - Bỏ qua `len(x1)` ký tự
- Ngược lại, giữ nguyên ký tự hiện tại