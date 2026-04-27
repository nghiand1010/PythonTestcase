# Unknown

**URL:** https://oj.tica.edu.vn/problem/vo_oc

---

# Bài toán: Chuỗi vỏ ốc

## Mô tả bài toán

Do trúng tuyển vào lớp 10 chuyên Tin với số điểm cao, Minh được bố mẹ cho đi chơi Cồn Nổi. Tại đây, Minh nhặt được một số vỏ ốc có màu trắng và một số vỏ ốc có màu xám. Khi về nhà, Minh quyết định xâu những vỏ ốc này thành các chuỗi vòng để tặng bạn. Biết rằng số vỏ ốc màu trắng là m, số vỏ ốc màu xám là n và Minh dùng tất cả số vỏ ốc mà mình đã nhặt được để xâu các chuỗi vòng.

### Yêu cầu:
Hãy giúp Minh chia các vỏ ốc này thành nhiều chuỗi nhất sao cho tất cả các chuỗi vòng này có số vỏ ốc mỗi màu đều bằng nhau.

## Dữ liệu vào

Tệp văn bản **CHUOI.INP** gồm hai số nguyên không âm m và n cách nhau một khoảng trắng (0 ≤ m,n ≤ 10¹⁸), lần lượt là số lượng vỏ ốc màu trắng và vỏ ốc màu xám.

## Dữ liệu ra

Tệp văn bản **CHUOI.OUT** ghi một số nguyên là số lượng chuỗi nhiều nhất có thể.

## Ví dụ

### Input
```
10 6
```

### Output
```
2
```

### Input
```
40 5
```

### Output
```
5
```

## Ràng buộc

- Có 20% số test tương ứng 20% số điểm với (0 ≤ m,n ≤ 10³)
- Có 40% số test tương ứng 40% số điểm với (0 ≤ m,n ≤ 10⁹)
- Có 40% số test tương ứng 40% số điểm với (0 ≤ m,n ≤ 10¹⁸)

## Phân tích bài toán

Giả sử có m vỏ ốc trắng và n vỏ ốc xám.

Ta cần chia thành k chuỗi sao cho mỗi chuỗi có cùng số lượng vỏ trắng và xám, tức là:
- m = k * a
- n = k * b

Do đó, k là **ước chung của m và n**. Để có nhiều chuỗi nhất, cần tìm **ước chung lớn nhất (GCD)** của m và n.

Công thức:
```
k = gcd(m, n)
```

## Độ phức tạp
O(log(max(m, n)))

## Lời giải mẫu (Python)
```python
import math
m, n = map(int, input().split())
print(math.gcd(m, n))
```

## Lời giải mẫu (C++)
```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    unsigned long long m, n;
    cin >> m >> n;
    cout << gcd(m, n);
    return 0;
}
```