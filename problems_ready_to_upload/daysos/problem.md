# Unknown

**URL:** https://oj.tica.edu.vn/problem/daysos

---

Cho 2 dãy số:
- Dãy số A gồm các số nguyên dương lẻ (1, 3, 5, 7, 9, …)
- Dãy số B gồm các số nguyên dương chẵn (2, 4, 6, 8, 10, …)

Dãy số S được tạo thành bằng cách:
- Lấy 1 số đầu tiên từ dãy A (1),
- Lấy 2 số đầu tiên từ dãy B xếp theo thứ tự ngược lại (4, 2),
- Tiếp tục lấy 3 số tiếp theo từ dãy A (3, 5, 7),
- Lấy 4 số tiếp theo từ dãy B xếp theo thứ tự ngược lại (12, 10, 8, 6),
- …

Một số số đầu của dãy S như sau:
1, 4, 2, 3, 5, 7, 12, 10, 8, 6, 9, 11, 13, 15, 17, 24, 22, 20, 18, 16, 14, 19, …

Cho số N. Hãy tính tổng các số trong dãy S từ số đầu tiên cho đến số N (bao gồm cả N).

Input Specification
- Một dòng chứa số nguyên N (1 ≤ N ≤ 10^15)

Output Specification
- Một dòng chứa một số nguyên duy nhất là phần dư khi chia tổng cần tìm cho 10007.

Scoring
- Có 60% số test ứng với 60% số điểm với N ≤ 10^6;
- 40% số test còn lại ứng với 40% số điểm có 10^6 < N ≤ 10^15

### Ví dụ 1:

### Input:
2

### Output:
7

### Giải thích:
1 + 4 + 2 = 7

### Ví dụ 2:

### Input:
5

### Output:
15

### Giải thích:
1 + 4 + 2 + 3 + 5 = 15