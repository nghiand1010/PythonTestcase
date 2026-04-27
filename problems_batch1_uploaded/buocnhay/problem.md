# Unknown

**URL:** https://oj.tica.edu.vn/problem/buocnhay

---

# BUOCNHAY -- Bước nhảy

## Đề bài

Trên một con đường thẳng các vị trí được đánh số từ 1 tới n, khoảng cách
giữa hai vị trí liên tiếp là một đơn vị độ dài.\
Có một con thỏ đang ở vị trí `x₁` và một củ cà rốt đang ở vị trí `x₂`.\
Cà rốt luôn là món ăn yêu thích của thỏ nên nó muốn nhảy thật nhanh đến
đó để lấp đầy chiếc bụng đói của mình.\
Tuy vậy, mỗi bước nhảy thỏ chỉ nhảy được **tối đa a đơn vị độ dài**.

------------------------------------------------------------------------

## Yêu cầu

Thỏ cần nhảy ít nhất bao nhiêu bước để tới vị trí của củ cà rốt?

------------------------------------------------------------------------

## Input

Chứa **3 số nguyên** `x₁, x₂, a`
với điều kiện `1 ≤ x₁ ≤ x₂ ≤ 10¹²`, `a ≤ 10³`.

------------------------------------------------------------------------

## Output

Ghi một số nguyên duy nhất -- số bước nhảy ít nhất mà thỏ cần để tới vị
trí của củ cà rốt.

------------------------------------------------------------------------

## Ví dụ

  Input:    
  -------- 
  1 
  6
  3    
  
  Output:
  --------
  2        
 
  Giải thích:
  -----------------------------------------
  Khoảng cách 5, mỗi bước 3 → cần 2 bước
  
  Input:    
  -------- 
  2 20 3  
  
  Output:
  --------
  6       
  
  Giải thích:
  -----------------------------------------
  Khoảng cách 18, mỗi bước 3 → cần 6 bước

------------------------------------------------------------------------

## Giới hạn

-   80% test có `x₂ ≤ 10⁶`
-   20% test không có ràng buộc gì thêm.