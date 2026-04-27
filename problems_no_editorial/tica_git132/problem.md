# Unknown

**URL:** https://oj.tica.edu.vn/problem/tica_git132

---

# SSAM019C - TẬP QUÂN SỰ



## Đề bài

Tại Chương Mỹ Resort, vào nửa đêm, cả trung đội nhận lệnh tập trung ở sân. Mỗi chiến sỹ được đánh số từ 1 đến N (1 < N < 40). Giám thị yêu cầu chọn ra một dãy K chiến sỹ để tập đội ngũ và cứ lần lượt duyệt hết tất cả các khả năng chọn K người như vậy từ nhỏ đến lớn (theo số thứ tự). Bài toán đặt ra là cho một nhóm K chiến sỹ hiện đang phải tập đội ngũ, hãy tính xem trong lượt chọn K người tiếp theo thì mấy người trong nhóm cũ sẽ được tạm nghỉ. Nếu đã là nhóm cuối cùng thì tất cả đều sẽ được nghỉ.

## Input

- Dòng đầu ghi số bộ test, không quá 20.
- Mỗi bộ test viết trên hai dòng:
  - Dòng 1: Hai số nguyên dương N và K (K < N)
  - Dòng 2: K số thứ tự của các chiến sỹ đang phải tập đội ngũ (viết từ nhỏ đến lớn)

## Output

Với mỗi bộ dữ liệu, in ra số lượng chiến sỹ được tạm nghỉ.

## Ví dụ

### Input

```
3
5 3
1 3 5
5 3
1 4 5
6 4
3 4 5 6
```

### Output

```
1
2
4
```