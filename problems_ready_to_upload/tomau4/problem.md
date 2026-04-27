# Unknown

**URL:** https://oj.tica.edu.vn/problem/tomau4

---

# Đề bài: Đếm ô tô màu trong một hàng của lưới

Cho một lưới vuông kích thước N. Ta tô màu từng cột theo thứ tự từ cột 1 đến cột N với quy tắc như sau:

- **Cột 1 (k=1, lẻ)**: tô từ hàng 1 xuống hàng N, tô N ô.  
- **Cột 2 (k=2, chẵn)**: tô từ hàng N lên hàng 2, tô N-1 ô.  
- **Cột 3 (k=3, lẻ)**: tô từ hàng 1 xuống hàng N-1, tô N-2 ô.  
- **Cột 4 (k=4, chẵn)**: tô từ hàng N lên hàng 3, tô N-3 ô.  
- …  
- **Cột \(k\)**: tô N - (k-1) ô; nếu k lẻ thì tô từ hàng 1 lên, nếu k chẵn thì tô từ hàng N xuống.

![](/martor/88c28ab2-c15f-4494-8471-15d05f0f7b04.png)

Ví dụ với \(N = 7\), ta có:
```
Cột 1 (k=1, lẻ):    tô hàng 1→7 (7 ô)
Cột 2 (k=2, chẵn):  tô hàng 7→2 (6 ô)
Cột 3 (k=3, lẻ):    tô hàng 1→5 (5 ô)
Cột 4 (k=4, chẵn):  tô hàng 7→4 (4 ô)
Cột 5 (k=5, lẻ):    tô hàng 1→3 (3 ô)
Cột 6 (k=6, chẵn):  tô hàng 7→6 (2 ô)
Cột 7 (k=7, lẻ):    tô hàng 1→1 (1 ô)
```

## Yêu cầu
Cho N và một chỉ số cột r (1 <= r <= N), hãy đếm xem có bao nhiêu ô trong cột r đã được tô màu theo quy tắc trên.

## Input
- Dòng đầu tiên chứa một số tự nhiên N ( 1 <= N <= 10^12).  
- Dòng thứ hai chứa một số tự nhiên r (1 <= r <= N ), là chỉ số cột cần đếm ô tô màu.

## Output
- In ra một số nguyên duy nhất: số ô ở hàng r đã được tô màu.

## Ví dụ

**Ví dụ 1**  
```
Input:
7
3

Output:
5
```


**Ví dụ 2**  
```
Input:
7
6

Output:
2
```