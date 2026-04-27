# Unknown

**URL:** https://oj.tica.edu.vn/problem/lehoiphim

---

## Bài toán: Lễ hội phim

### Mô tả
Trong một lễ hội phim, **n** bộ phim sẽ được chiếu. Bạn biết thời gian bắt đầu và kết thúc của mỗi bộ phim. Số lượng phim tối đa bạn có thể xem trọn vẹn là bao nhiêu?

### Input
- Dòng đầu vào đầu tiên có một số nguyên **n**: số lượng bộ phim.
- Sau này, có **n** dòng mô tả các bộ phim. Mỗi dòng có hai số nguyên **a** và **b**: thời gian bắt đầu và kết thúc của một bộ phim.

### Output
- In một số nguyên: số lượng phim tối đa.

### Constraints
- 1 ≤ n ≤ 2 × 10⁵
- 1 ≤ a < b ≤ 10⁹

### Example
#### Sample input
```
3
3 5
4 9
5 8
```
#### Sample output
```
2
```

#### Giải thích

- Bạn có thể xem được tối đa 2 bộ phim:

- Xem phim (3, 5)

- Sau đó xem phim (5, 8)