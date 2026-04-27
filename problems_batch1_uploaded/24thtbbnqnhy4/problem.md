# Unknown

**URL:** https://oj.tica.edu.vn/problem/24thtbbnqnhy4

---

# Trò chơi xóa xâu

Hôm nay là ngày sinh nhật của Bob, mẹ của Bob tặng cho cậu một xâu ký tự `s`.  
Thích thú với món quà trên tay, Bob liền chạy đi tìm Alice để chơi trò **xóa xâu**.

---

## Luật chơi

- Bob và Alice chơi lần lượt.
- **Bob là người đi trước**.
- Mỗi lượt chơi, người chơi được chọn **hai ký tự liên tiếp giống nhau** trong xâu `s` và **xóa** chúng khỏi xâu.
- Người **không thực hiện được thao tác xóa** ở lượt của mình sẽ **bị xử thua**.

Bob và Alice đều chơi **tối ưu**.  
Hãy xác định **ai là người chiến thắng**.

---

## Dữ liệu vào

- Một dòng duy nhất chứa xâu `s`.
- Độ dài của xâu `s` không vượt quá `10^5`.
- Xâu chỉ chứa các chữ cái thường từ `a` đến `z`.

---

## Kết quả

- In ra **một xâu duy nhất**:
  - `Bob` nếu Bob là người chiến thắng
  - `Alice` nếu Alice là người chiến thắng

---

## Ví dụ

### Ví dụ 1

**Input**
```
abacaba
```

**Output**
```
Alice
```

---

### Ví dụ 2

**Input**
```
aabb
```

**Output**
```
Bob
```

---

## Ràng buộc

- Subtask 1 (16% số điểm):  
  Xâu `s` chỉ chứa **một loại ký tự**.

- Subtask 2 (84% số điểm):  
  Không có ràng buộc gì thêm.