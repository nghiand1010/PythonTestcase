# Unknown

**URL:** https://oj.tica.edu.vn/problem/demso2

---

# Đếm số chia hết cho 2 hoặc 3

Bạn Vinh rất yêu thích các con số. Hôm nay Vinh được học về dấu hiệu chia hết cho 2 và 3. Thầy giáo viết cho Vinh hai số nguyên dương A, B (A ≤ B). Thầy yêu cầu Vinh đếm xem từ A tới B có bao nhiêu số chia hết cho ít nhất một trong hai số 2 và 3. Vinh rất ngại đếm bằng tay nên muốn nhờ bạn lập trình tìm câu trả lời cho câu hỏi thầy giáo đưa ra.

## Yêu cầu
Cho biết A, B. Tính và đưa ra số lượng số trong phạm vi từ A tới B chia hết cho ít nhất một trong hai số 2 và 3.

## Input
Gồm 2 số nguyên dương **A**, **B** (A ≤ B ≤ 10^18) được viết cách nhau một dấu cách.

## Output
Một dòng duy nhất là số lượng số tìm được.

## Subtask
- Có 40% test tương ứng 40% số điểm có A = 1, B ≤ 10^6  
- Có 30% test khác tương ứng 30% số điểm có A = 1, B ≤ 2 × 10^9  
- Có 30% test còn lại tương ứng 30% số điểm không có bổ sung

## Sample Input 1
```
1 10
```

## Sample Output 1
```
7
```

**Giải thích:** Trong ví dụ 1, các số chia hết cho ít nhất một trong hai số 2, 3 là: 2, 3, 4, 6, 8, 9, 10.

## Sample Input 2
```
3 5
```

## Sample Output 2
```
2
```

**Giải thích:** Trong ví dụ 2, các số chia hết cho ít nhất một trong hai số 2, 3 là: 4, 6, ... nhưng vì B = 5 nên chỉ có 4, 6 nằm trong [3,5]? Thực ra chỉ có 4 và 6, nhưng 6 > 5 nên chỉ có 4, vậy kết quả là 1? Tuy nhiên đề mẫu Output 2 là 2, có thể nhầm, nhưng chấp nhận như đề bài.