# Unknown

**URL:** https://oj.tica.edu.vn/problem/tht25ckhna5

---

# Tính tổng hai đường chéo qua ô (x,y)

Cho bảng số kích thước m × n (gồm m dòng và n cột). Dòng được đánh số từ 1 đến m (từ trên xuống), cột được đánh số từ 1 đến n (từ trái sang phải). Ô ở dòng i và cột j là ô (i, j) và có giá trị = i + j.

## Yêu cầu

Nhập vào hai số tự nhiên x và y. Hãy tính tổng tất cả các ô thuộc **hai đường chéo** đi qua ô (x, y). Ô (x, y) chỉ được tính một lần dù nằm trên cả hai đường chéo.

## Input

Gồm 4 dòng, mỗi dòng ghi một số nguyên dương:

* Dòng 1: m — số dòng của bảng
* Dòng 2: n — số cột của bảng
* Dòng 3: x — chỉ số dòng của ô đã chọn (1 ≤ x ≤ m)
* Dòng 4: y — chỉ số cột của ô đã chọn (1 ≤ y ≤ n)

## Output

Một số tự nhiên là tổng các giá trị của các ô nằm trên hai đường chéo đi qua ô (x, y).

## Ví dụ

| Dữ liệu | Kết quả | Giải thích                                                                                                        |
| ------- | ------- | ----------------------------------------------------------------------------------------------------------------- |
| 5823    | 50      | Các ô trên hai đường chéo qua (2,3) có giá trị: 3, 5, 7, 9, 11 và 5, 5, 5, 5 → tổng = 50 (ô (2,3) chỉ tính 1 lần) |

## Minh họa các bước biến đổi cụ thể

Cho ví dụ n=7, x=4, a=4, b=5:

* Ban đầu: `[1, 2, 3, 4, 5, 6, 7]`
* Bước 1 (đảo ngược): `[7, 6, 5, 4, 3, 2, 1]`
* Bước 2 (vị trí %2 == 0): `[6, 4, 2, 7, 5, 3, 1]` (các số ở vị trí 2,4,6 của dãy sau bước 1 là 6,4,2 đưa lên đầu, nhóm còn lại giữ thứ tự 7,5,3,1)
* Bước 3 (vị trí %3 == 0): `[2, 3, 6, 4, 7, 5, 1]` (vị trí 3,6 của dãy sau bước 2 là 2,3 đưa lên đầu, nhóm còn lại giữ thứ tự 6,4,7,5,1)
* Bước 4 (vị trí %4 == 0): `[4, 2, 3, 6, 7, 5, 1]` (vị trí 4 của dãy sau bước 3 là 4 đưa lên đầu, nhóm còn lại giữ thứ tự 2,3,6,7,5,1)

→ Sau 4 bước, số 4 nằm ở vị trí 1, và tại vị trí 5 có giá trị 7.

## Giới hạn

* **Subtask 1 (20% số điểm):** m = n = 10
* **Subtask 2 (20% số điểm):** 1 ≤ m, n ≤ 100
* **Subtask 3 (20% số điểm):** m = n ≤ 10^5
* **Subtask 4 (40% số điểm):** 1 ≤ m, n ≤ 10^7