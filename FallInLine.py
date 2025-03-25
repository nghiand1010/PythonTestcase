from collections import defaultdict
from fractions import Fraction

def max_points_on_line(points):
    def slope(p1, p2):
        if p1[0] == p2[0]:  # Trường hợp đặc biệt: đường thẳng đứng
            return 'inf'
        return Fraction(p2[1] - p1[1], p2[0] - p1[0])

    max_points = 0
    n = len(points)

    for i in range(n):
        slopes = defaultdict(int)
        duplicate = 1
        for j in range(i + 1, n):
            if points[i] == points[j]:
                duplicate += 1
                continue
            slope_value = slope(points[i], points[j])
            slopes[slope_value] += 1

        current_max = duplicate
        for count in slopes.values():
            current_max = max(current_max, count + duplicate)

        max_points = max(max_points, current_max)

    return max_points

# Tập hợp các điểm
points = [(2, 4), (7, 2), (6, 10), (0, 1), (3, 4), (4, 8)]
print("Số điểm tối đa trên một đường thẳng là:", max_points_on_line(points))
