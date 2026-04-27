# Unknown

**URL:** https://oj.tica.edu.vn/problem/kytu1

---

# Câu 2: Ký tự giống nhau

Cho hai xâu ký tự `x` và `y` cùng độ dài `L (L ≤ 10^5)` chỉ bao gồm các chữ cái in thường.  
Các ký tự được đánh số từ 1 đến L.  
Cho `Q` truy vấn, mỗi truy vấn gồm hai số nguyên `u, v` lần lượt là loại truy vấn và vị trí cần truy vấn.

## Yêu cầu
Với mỗi truy vấn, trả lời như sau:
- **Truy vấn loại 1 (u = 1):** Ký tự ở vị trí `v` trong `x` và `y` có giống nhau không?
- **Truy vấn loại 2 (u = 2):** Ký tự ở vị trí `v` trong `x` có giống ký tự ở vị trí **đối xứng** của `v` trong chuỗi `y` hay không?

Vị trí đối xứng của `v` là vị trí `L - v + 1` (vị trí đối xứng qua trung tâm của chuỗi).

### Ví dụ
Giả sử có hai chuỗi cùng độ dài `L = 3`:  
`x = "lao"`, `y = "cai"` → vị trí ảnh xạ:
- 1 ↔ 3
- 2 ↔ 2
- 3 ↔ 1

## Dữ liệu vào
- Dòng đầu tiên: hai chuỗi `x, y` có cùng độ dài.
- Dòng thứ hai: số nguyên `Q` — số lượng truy vấn.
- Q dòng tiếp theo: mỗi dòng gồm hai số `u, v (1 ≤ u ≤ 2; 1 ≤ v ≤ L)`.

## Dữ liệu ra
- Gồm Q dòng, mỗi dòng in ra `"YES"` nếu hai ký tự cần so sánh giống nhau, `"NO"` nếu khác nhau.

### Ví dụ

#### Input
```
abc cba
1
1 2
```

#### Output
```
YES
```

#### Input
```
icpc cici
3
1 2
2 3
2 4
```

#### Output
```
NO
NO
YES
```

## Giới hạn
- `1 ≤ L ≤ 10^5`
- `1 ≤ Q ≤ 10^5`