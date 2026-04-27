# Unknown

**URL:** https://oj.tica.edu.vn/problem/xau_adn

---

# ĐOẠN ADN CON DÀI NHẤT

## Mô tả bài toán

Bạn có một dãy ADN: một xâu ký tự chỉ gồm các chữ cái **A, T, G, C**.

Hãy tìm **độ dài của đoạn ADN con dài nhất** (đoạn con **liên tiếp**) mà **chỉ gồm các ký tự giống nhau**.

---

## Input

- Một dòng duy nhất chứa xâu `s`.

---

## Output

- In ra **độ dài của đoạn ADN con dài nhất** tìm được.

---

## Constraints

- `1 ≤ n ≤ 10^6`

---

## Example

### Sample input

```
ATTCGGGA
```

### Sample output

```
3
```

---

## Giải thích ví dụ

Xâu `ATTCGGGA` gồm các đoạn ký tự giống nhau liên tiếp:

- `A` → độ dài 1
- `TT` → độ dài 2
- `C` → độ dài 1
- `GGG` → độ dài 3
- `A` → độ dài 1

Đoạn dài nhất là `GGG` nên kết quả là **3**.