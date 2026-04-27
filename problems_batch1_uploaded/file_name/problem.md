# Unknown

**URL:** https://oj.tica.edu.vn/problem/file_name

---

# B. File name (Tên tệp)

## Giới hạn
- **Thời gian:** 1 giây
- **Bộ nhớ:** 256 MB

---

## 📘 Mô tả bài toán

Bạn không thể gửi một tệp tin một cách tùy ý.

Khi cố gắng gửi một tệp tin trên mạng xã hội **"Codehorses"**, Polikarp đã gặp phải một sự cố bất ngờ. Nếu **tên tệp tin chứa ba hoặc nhiều hơn ba chữ cái `x` liên tiếp**, hệ thống sẽ cho rằng nội dung của tệp là **không phù hợp** với mạng xã hội.

Trong trường hợp đó, tệp tin sẽ **không được gửi** và một thông báo lỗi sẽ xuất hiện.

Nhiệm vụ của bạn là xác định **số ký tự ít nhất cần xóa** khỏi tên tệp sao cho **tên tệp không còn chứa chuỗi con `"xxx"`**.

- Nếu ban đầu tên tệp **không chứa** chuỗi con `"xxx"` thì hãy in ra `0`.
- Các ký tự có thể được **xóa ở bất kỳ vị trí nào** (không nhất thiết phải liên tiếp).

Khi xóa một ký tự, độ dài của chuỗi sẽ **giảm đi 1**.

**Ví dụ:**
- Xóa ký tự ở vị trí thứ 2 trong chuỗi `exxxii` sẽ thu được chuỗi `exxii`.

---

## 📥 Dữ liệu vào (Input)

- Dòng đầu tiên chứa số nguyên `n` (`3 ≤ n ≤ 100`) — độ dài của tên tệp.
- Dòng thứ hai chứa một chuỗi độ dài `n`, chỉ gồm **các chữ cái Latin thường** — chính là tên tệp.

---

## 📤 Dữ liệu ra (Output)

- In ra **số lượng ký tự nhỏ nhất** cần phải xóa để tên tệp **không còn chứa** chuỗi con `"xxx"`.
- Nếu tên tệp ban đầu không chứa `"xxx"`, hãy in ra `0`.

---

## 🧪 Ví dụ

### Ví dụ 1
**Input**
```
6
xxxiii
```
**Output**
```
1
```

---

### Ví dụ 2
**Input**
```
5
xxoxx
```
**Output**
```
0
```

---

### Ví dụ 3
**Input**
```
10
xxxxxxxxxx
```
**Output**
```
8
```

---

## 📝 Ghi chú

Trong ví dụ 1, Polikarp muốn gửi một tệp có chứa số **33** trong tên (viết bằng số La Mã là `XXX`). Tuy nhiên, anh ấy không thể gửi tệp vì tên tệp chứa **ba chữ `x` liên tiếp**. Để gửi thành công, anh ấy cần **xóa đi một trong các chữ `x` đó**.