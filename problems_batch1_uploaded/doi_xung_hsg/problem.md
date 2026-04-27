# Unknown

**URL:** https://oj.tica.edu.vn/problem/doi_xung_hsg

---

# Bài 3: Đối xứng

## Mô tả bài toán

Cho xâu ký tự **S** chỉ gồm các ký tự **chữ in hoa**, **chữ in thường** và **chữ số**.

- **Xâu con** là xâu được lấy ra từ xâu S bằng cách chọn một số ký tự **liên tiếp**.
- Xâu S cũng được coi là xâu con của chính nó.
- Một xâu được gọi là **đối xứng** nếu đọc từ **trái sang phải** và từ **phải sang trái** đều giống nhau.

### Ví dụ

- Các xâu đối xứng: `madam`, `IOI`, `aba6aba`
- Các xâu không đối xứng: `Caab`, `92328`, `abda`

---

## Yêu cầu

Cho xâu **S** có độ dài không quá \(10^4\) ký tự, chỉ gồm chữ in hoa, chữ in thường và chữ số.

Hãy tìm **độ dài của xâu con đối xứng dài nhất** trong xâu S.

---

## Input

- Đọc từ bàn phím một dòng chứa xâu ký tự **S**.

---

## Output

- Ghi ra màn hình **một số nguyên duy nhất** là độ dài xâu con đối xứng dài nhất tìm được.

---

## Scoring

- **Subtask 1 (70%)**: Độ dài xâu S không quá 500 ký tự.
- **Subtask 2 (30%)**: Không có ràng buộc gì thêm \(N \le 10^4\).

---

## Ví dụ

### Input
```
Caaba1ababa
```

### Output
```
7
```