# Unknown

**URL:** https://oj.tica.edu.vn/problem/tica_git133

---

# SSAM019B - SỐ ĐẦU TIÊN BỊ LẶP


## Đề bài

Cho dãy số A[] gồm có N phần tử. Nhiệm vụ của bạn là hãy tìm số xuất hiện nhiều hơn 1 lần trong dãy số và có vị trí xuất hiện đầu tiên nhỏ nhất.

## Input

- Dòng đầu tiên là số lượng bộ test T (T ≤ 10).
- Mỗi test gồm:
  - Dòng đầu tiên chứa số nguyên N (1 ≤ N ≤ 100.000) — số lượng phần tử trong dãy số ban đầu.
  - Dòng tiếp theo gồm N số nguyên A[i] (0 ≤ A[i] ≤ 10^9).

## Output

Với mỗi test, in ra đáp án của bài toán trên một dòng. Nếu không tìm được đáp án, in ra NO.

## Ví dụ

### Input

```
2
7
10 5 3 4 3 5 6
4
1 2 3 4
```

### Output

```
5
NO
```

*Giải thích test 1:* Cả 5 và 3 đều xuất hiện 2 lần, nhưng số 5 có vị trí xuất hiện đầu tiên nhỏ hơn.