# Unknown

**URL:** https://oj.tica.edu.vn/problem/dschinhphuong

---

# Bài toán: Đếm số chính phương

## Đề bài
Trong toán học, **số chính phương** là số tự nhiên có thể viết được dưới dạng bình phương của một số tự nhiên nào đó, tức là tồn tại số tự nhiên k sao cho a = k².

### Yêu cầu
Nhập vào một dãy gồm n số tự nhiên và cho biết có bao nhiêu số trong dãy đó là số chính phương.

## Dữ liệu đầu vào
Gồm hai dòng:
- **Dòng 1:** Một số nguyên n (1 ≤ n ≤ 10⁵) – số lượng phần tử trong dãy.
- **Dòng 2:** n số nguyên a₁, a₂, …, aₙ (0 ≤ aᵢ ≤ 10⁹) – các phần tử của dãy.

## Dữ liệu đầu ra
Gồm một số nguyên duy nhất – là **số lượng số chính phương** trong dãy đã cho.

## Ví dụ
### Ví dụ 1
**Input:**
```
5
49 6 9 5 2
```
**Output:**
```
2
```
**Giải thích:** 49 = 7², 9 = 3² ⇒ có 2 số chính phương.

---

### Ví dụ 2
**Input:**
```
6
18 26 19 5 2 3
```
**Output:**
```
0
```
Không có số nào trong dãy là số chính phương.

---

```