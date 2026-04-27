# Unknown

**URL:** https://oj.tica.edu.vn/problem/nhomhocsinh

---

# PHÂN NHÓM HỌC SINH THEO CHIỀU CAO

## Mô tả
Trong buổi biểu diễn văn nghệ cuối năm của một trường trung học cơ sở, có **n** học sinh tham gia và được đánh số từ 1 đến n. Các học sinh có chiều cao lần lượt là **h1, h2, …, hn**.

Ban tổ chức muốn:
- Xếp các học sinh **có cùng chiều cao** vào **cùng một nhóm múa** để có đội hình đẹp.
- Các học sinh có **chiều cao riêng biệt** (không trùng với bất kỳ học sinh nào khác) sẽ được xếp chung vào **một nhóm kịch**.

## Yêu cầu
Hãy xác định:
- Chiều cao và số học sinh của **từng nhóm múa**.
- Riêng **nhóm kịch** chỉ cần xác định **có bao nhiêu học sinh**.

## Dữ liệu vào
Gồm hai dòng:
- Dòng thứ nhất chứa một số nguyên **n** *(1 ≤ n ≤ 10^5)*.
- Dòng thứ hai chứa **n** số nguyên dương **h1, h2, …, hn** *(1 ≤ hi ≤ 10^9)*, giữa hai số cách nhau một khoảng trắng.

## Kết quả
Gồm nhiều dòng:
- Các dòng đầu: mỗi dòng ghi **hai số nguyên** lần lượt là **chiều cao** và **số lượng học sinh** của từng nhóm múa, theo **thứ tự tăng dần theo chiều cao**. Nếu không có nhóm múa nào thì không có các dòng này.
- Dòng cuối ghi **một số nguyên** là **số học sinh của nhóm kịch**.

## Ví dụ

### Ví dụ 1

**Input**
```
7
165 164 150 150 164 165 165
```

**Output**
```
150 2
164 2
165 3
0
```