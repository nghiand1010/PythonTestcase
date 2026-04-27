# Unknown

**URL:** https://oj.tica.edu.vn/problem/denled

---

# Bài toán: ĐÈN LED QUẢNG CÁO

Một công ty quảng cáo muốn làm biển hiệu số nhà bằng **bóng đèn LED**.  
Mỗi chữ số từ `0` đến `9` được tạo bởi số bóng LED nhất định như sau:

```
0: 6 bóng   1: 2 bóng   2: 5 bóng   3: 5 bóng   4: 4 bóng
5: 5 bóng   6: 6 bóng   7: 3 bóng   8: 7 bóng   9: 6 bóng
```

Công ty đã làm sẵn một số hiệu **N** (100 ≤ N ≤ 999).  
Tổng số bóng LED để làm số hiệu này là **M**.  

Câu hỏi: Với đúng **M bóng LED** đó, công ty có thể lắp được những số hiệu nào có đúng 3 chữ số?  
Hãy tìm **số nhỏ nhất** và **số lớn nhất** có thể lắp được.  

---

### Input
- Một số nguyên **N** (100 ≤ N ≤ 999).  

### Output
- Gồm 2 số nguyên: số nhỏ nhất và số lớn nhất tìm được.  

---

### Ví dụ

**Input**
```
275
```

**Output**
```
111 999
```

**Giải thích**  
- Số `275` cần `5 + 5 + 5 = 15` bóng LED.  
- Với 15 bóng LED, ta thử tất cả số có 3 chữ số, tìm được số nhỏ nhất là `111`, số lớn nhất là `999`.