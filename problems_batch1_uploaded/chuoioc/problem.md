# Unknown

**URL:** https://oj.tica.edu.vn/problem/chuoioc

---

# Bài 1. CHUOI1 Chuỗi vỏ ốc

Do trúng tuyển vào lớp 10 chuyên Tin học với số điểm cao. Mình được bố mẹ cho đi chơi Cồn Nổi. Tại đây, Mình nhặt được một số vỏ ốc có màu trắng và một số vỏ ốc có màu xám. Khi về nhà, Mình quyết định xâu những vỏ ốc này thành các chuỗi vòng để tặng bạn. Biết rằng số vỏ ốc màu trắng là m, số vỏ ốc màu xám là n và Mình dùng tất cả số vỏ ốc mà mình đã nhận được để xâu các chuỗi vòng.

**Yêu cầu:** Hãy giúp Mình chia các vỏ ốc này thành nhiều chuỗi nhất sao cho tất cả các chuỗi vòng này có số vỏ ốc mỗi màu đều bằng nhau.

**Input:** gồm hai số nguyên không âm m và n cách nhau một khoảng trắng (0 ≤ m, n ≤ 10^18), lần lượt là số lượng vỏ ốc màu trắng và vỏ ốc màu xám.

**Output:** ghi một số nguyên là số lượng chuỗi nhiều nhất có thể.

## Ràng buộc
- Có 20% số test tương ứng với 20% số điểm với 0 ≤ m, n ≤ 10^3.  
- Có 40% số test tiếp theo tương ứng với 40% số điểm với 10^3 ≤ m, n ≤ 10^9.  
- Có 40% số test tiếp theo tương ứng với 40% số điểm với 10^9 ≤ m, n ≤ 10^18.

## Ví dụ

### Input
```
10 6
```

### Output
```
2
```

**Giải thích:**  
Có 2 cách để xâu các chuỗi:
- Cách 1: Chỉ xâu 1 chuỗi có 10 vỏ ốc màu trắng và 6 vỏ ốc màu xám;  
- Cách 2: Xâu thành 2 chuỗi, mỗi chuỗi đều có 5 vỏ ốc màu trắng và 3 vỏ ốc màu xám;  

Chọn cách 2 vì số lượng chuỗi nhiều hơn.