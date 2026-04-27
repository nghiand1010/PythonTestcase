# Unknown

**URL:** https://oj.tica.edu.vn/problem/23kvatestthmatma

---

# Mật mã Caesar

## Mô tả

Trong mật mã học, **Mật mã Caesar** (hay còn được gọi là *Mật mã của Caesar*, *Mật mã chuyển vị*, *Chuyển vị Caesar*) là một trong những kỹ thuật mã hóa đơn giản và phổ biến nhất.

Đây là một dạng **mật mã thay thế**, trong đó mỗi ký tự trên văn bản gốc sẽ được thay bằng một ký tự khác, có vị trí cách nó một khoảng xác định trong bảng chữ cái.

Ví dụ, nếu dịch chuyển sang trái 3 bước:
- D → A  
- E → B  

## Quy tắc mã hóa

Để mã hóa, người ta chọn một **khóa k** – chính là số bước dịch chuyển sang phải.

Ví dụ với `k = 4`, ta có bảng chuyển đổi:

```
Plain  : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Cipher : E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
```

Khi mã hóa, ta thay chữ cái ở dòng **Plain** bằng chữ cái tương ứng ở dòng **Cipher**.

## Yêu cầu

Cho trước khóa `k` và xâu tin nhắn `S`, hãy mã hóa xâu theo quy luật trên.

---

## Input

- Dòng đầu chứa số nguyên `k` (`|k| ≤ 10^6`)
- Dòng tiếp theo chứa xâu `S` (`1 ≤ |S| ≤ 1000`)  
  - Chỉ gồm **dấu cách** hoặc các **ký tự Latin in hoa** (`A–Z`)

## Output

- Một dòng duy nhất chứa **xâu đã được mã hóa**

---

## Chấm điểm

- **Subtask 1 (50%)**: `k < 10`
- **Subtask 2 (50%)**: `k ≤ 10^6`

---

## Ví dụ

### Input
```
2
ACCEPTED
```

### Output
```
CEEGVRGF
```

---

## Lưu ý

- **Dấu cách** được giữ nguyên, **không mã hóa**.
- Giá trị `k` có thể rất lớn, vì vậy cần lấy `k mod 26` khi xử lý.

---

## Minh họa

![](/martor/8c7b9562-d4d1-4246-92d3-365a4f9bfd9c.png)

- Vòng ngoài: ký tự gốc  
- Vòng trong: ký tự sau khi mã hóa  
- Số ở giữa: khoảng cách dịch chuyển

Mật mã Caesar hoạt động dựa trên nguyên lý xoay vòng bảng chữ cái.