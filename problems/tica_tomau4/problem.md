# Unknown

**URL:** https://oj.tica.edu.vn/problem/tica_tomau4

---

# Tô màu các đường chéo chính và phụ

Cho ma trận vuông kích thước (N×N) (các hàng và cột đánh số từ 1 đến N) và một số tự nhiên K. Người ta tiến hành tô màu các ô vuông theo quy tắc sau:

1. **Tô đường chéo chính** (tập các ô i-j=0), sau đó lặp lại tô các đường chéo **song song** với nó, cách đều đúng K đường chéo **không tô** giữa hai lần tô, về cả hai phía, cho đến khi đường chéo cần tô nằm hoàn toàn ngoài ma trận.
2. **Tô đường chéo phụ** (tập các ô i+j=N+1), sau đó lặp lại tô các đường chéo **song song** với nó, cách đều đúng K đường chéo **không tô** giữa hai lần tô, về cả hai phía, cho đến khi đường chéo cần tô nằm hoàn toàn ngoài ma trận.

Hỏi: **tổng số ô** được tô màu trong toàn bộ quá trình (nếu một ô thuộc cả hai loại đường chéo thì chỉ tính một lần).

---

## Dữ liệu vào

Dòng đầu chứa hai số nguyên **N** và **K** (1 ≤ K < N ≤ 10^9), mỗi số trên một dòng hoặc cách nhau một dấu cách.

## Kết quả

In ra một số nguyên duy nhất — tổng số ô được tô màu.

## Ví dụ

**Ví dụ 1**

```
Input:
6 1
Output:
22
```


**Ví dụ 2**

```
Input:
5 2
Output:
17
```