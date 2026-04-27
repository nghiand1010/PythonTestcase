# Unknown

**URL:** https://oj.tica.edu.vn/problem/demsodep

---

# Bài 2: Đếm số đẹp trong dãy số

## Đề bài
Cho một dãy gồm **T** số nguyên dương.  
Một số nguyên **n** được gọi là **số đẹp** khi **mỗi chữ số x (0 ≤ x ≤ 9)**  
hoặc **không xuất hiện trong n**,  
hoặc **xuất hiện với số lần chẵn**.

### Yêu cầu
Hãy viết chương trình để đếm xem trong dãy có bao nhiêu số đẹp.

---

## Dữ liệu vào
- Dòng đầu tiên chứa số nguyên dương **T** (1 ≤ T ≤ 1000).  
- **T dòng tiếp theo**, mỗi dòng chứa một số nguyên dương **n** (1 ≤ n ≤ 10⁹).

## Dữ liệu ra
- Một số nguyên duy nhất là **số lượng các số đẹp** trong dãy.

---

## Ví dụ

### Input (`SODEP.INP`)
```
3
1234
422666
232003
```

### Output (`SODEP.OUT`)
```
1
```

---

## Giải thích ví dụ
- `1234`: mỗi chữ số xuất hiện 1 lần → không đẹp.  
- `422666`: chữ số 4 và 6 xuất hiện lẻ lần → không đẹp.  
- `232003`: các chữ số 0, 2, 3 đều xuất hiện 2 lần → **đẹp**.

➡️ Kết quả: có **1** số đẹp trong dãy.

---

## Gợi ý thuật toán (dành cho học sinh lớp 5–6)
1. Với mỗi số, tạo mảng `count[10]` để đếm số lần xuất hiện của từng chữ số.  
2. Duyệt qua từng chữ số trong số đó, tăng `count[d]` tương ứng.  
3. Sau khi đếm xong, kiểm tra xem **mọi chữ số** có số lần xuất hiện chẵn (hoặc 0) hay không.  
4. Nếu đúng → đó là số đẹp.  
5. Đếm tổng số lượng các số đẹp và in ra.

---

## Độ phức tạp
- **Thời gian:** O(T)  
- **Bộ nhớ:** O(1)  
Vì mỗi số có tối đa 10 chữ số, thuật toán rất nhanh.

---

## Code mẫu (Python)
```python
T = int(input().strip())
result = 0

for _ in range(T):
    s = input().strip()
    count = [0] * 10

    for ch in s:
        d = int(ch)
        count[d] += 1

    is_beautiful = True
    for i in range(10):
        if count[i] % 2 == 1:
            is_beautiful = False
            break

    if is_beautiful:
        result += 1

print(result)
```