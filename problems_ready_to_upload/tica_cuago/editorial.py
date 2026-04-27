# -*- coding: utf-8 -*-
"""
Editorial Solution for tica_cuago
Auto-generated from editorial.txt
"""

import sys
from io import StringIO


def can_cut(lengths, k, mid):
    """Kiểm tra xem có thể cắt được ít nhất k đoạn với độ dài mid không."""
    count = 0
    for length in lengths:
        count += length // mid
        if count >= k:  # Không cần đếm thêm nếu đã đủ
            return True
    return count >= k

def max_cut_length(n, k, lengths):
    """Tìm độ dài lớn nhất của đoạn gỗ có thể nhận được."""
    low, high = 1, max(lengths)  # Khoảng tìm kiếm nhị phân
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if can_cut(lengths, k, mid):
            result = mid  # Lưu lại độ dài hợp lệ
            low = mid + 1  # Tìm độ dài lớn hơn
        else:
            high = mid - 1  # Tìm độ dài nhỏ hơn

    return result

# Đọc dữ liệu đầu vào
def main():
    n, k = map(int, input().split())  # Số thanh gỗ và số đoạn cần cắt
    lengths = [int(input()) for _ in range(n)]  # Độ dài từng thanh gỗ

    # Tính độ dài lớn nhất của đoạn gỗ
    result = max_cut_length(n, k, lengths)
    print(result)

if __name__ == "__main__":
    main()
