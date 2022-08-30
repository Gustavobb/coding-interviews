# https://leetcode.com/problems/largest-triangle-area/
# Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2.00000

# Input: points = [[1,0],[0,0],[0,1]]
# Output: 0.50000

# 3 <= points.length <= 50
# -50 <= xi, yi <= 50
# All the given points are unique.

def largest_triangle_area(points: list[list[int]]) -> float:  
    """
    Return the largest triangle area given an array of points on the X-Y plane points where points[i] = [xi, yi]
    """
    max_area = 0
    
    for p1 in points:
        for p2 in points:
            if p2 == p1: continue
            for p3 in points:
                if p3 == p1 or p3 == p2: continue
                max_area = max(max_area, compute_triangle_area(p1, p2, p3))
    
    return max_area

def compute_triangle_area(p1: int, p2: int, p3: int) -> float:
    """
    Compute triangle area based on Heron's formula
    """
    return (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2

def main() -> int:
    """
    Main function
    """
    assert largest_triangle_area([[0,0],[0,1],[1,0],[0,2],[2,0]]) == 2.00000
    assert largest_triangle_area([[1,0],[0,0],[0,1]]) == 0.50000

if __name__ == "__main__":
    main();
    exit(0);