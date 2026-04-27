# Unknown

**URL:** https://oj.tica.edu.vn/problem/zigzag

---

# Trò chơi Zig-Zag Marble

Một viên bi được đẩy trên hai hàng song song gồm `N` ô (hàng trên và hàng dưới), mô tả như sau:

* Hàng trên có `N` ô đánh số từ `1` đến `N` từ trái sang phải.
* Hàng dưới cũng có `N` ô đánh số từ `1` đến `N` từ trái sang phải.
* Viên bi khởi đầu ở ô hàng trên số `1`.
* Mỗi lần đẩy, viên bi di chuyển theo quy tắc Zig-Zag:

  1. Nếu đang ở **hàng trên cột** `i` thì đi xuống **hàng dưới cột** `i`.
  2. Nếu đang ở **hàng dưới cột** `i` và **đang hướng xuôi** (chưa đến cột `N`) thì đi lên **hàng trên cột** `i+1`.
  3. Khi chạm **hàng trên cột** `N` → đi xuống **hàng dưới cột** `N` → đổi chiều sang ngược:

     * Từ **hàng dưới cột** `i` đi lên **hàng trên cột** `i`.
     * Từ **hàng trên cột** `i` (và `i > 1`) đi xuống **hàng dưới cột** `i-1`.
     * Tiếp tục như vậy cho đến cột `1`, rồi lại đổi chiều sang xuôi, và lặp lại vô tận.

## Yêu cầu

Cho biết sau `K` lần đẩy, viên bi đang ở **hàng nào** và **cột số mấy**?

---

## Input

Hai số nguyên:

* Dòng 1: `N` — số ô mỗi hàng (`N` chẵn, `4 ≤ N ≤ 10^{15}`)
* Dòng 2: `K` — số lần đẩy (`1 ≤ K ≤ 10^{15}`)

## Output

Hai số nguyên:

* Số `r ∈ {1,2}` cho biết hàng (1 = trên, 2 = dưới)
* Số `c ∈ [1..N]` cho biết cột

## Ví dụ

**Ví dụ 1**

```
Input:
8
4

Output:
1 5
```

**Giải thích**: Chu kỳ đầy đủ gồm `(N-1)+(N-3)=12` bước. Với `K=4` (trong đoạn xuôi) vị trí là hàng 1, cột `1+4=5`.

**Ví dụ 2**

```
Input:
8
10

Output:
2 3
```

**Giải thích**: `K mod 12 = 10` nằm ở giai đoạn ngược, bước `d=10-7=3` lẻ → từ hàng dưới cột 8 đi lên → kết thúc ở hàng 2, cột `3`.