# https://leetcode.com/problems/rectangle-area/description/

# Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.
# The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).
# The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

# Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
# Output: 45

# Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
# Output: 16

def compute_area(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    """
    Compute the area of the two rectangles
    """
    area_a = (ay2 - ay1) * (ax2 - ax1)
    area_b = (by2 - by1) * (bx2 - bx1)

    x_overlap = max(0, min(ax2, bx2) - max(ax1, bx1))
    y_overlap = max(0, min(ay2, by2) - max(ay1, by1))

    return area_a + area_b - x_overlap * y_overlap

def main() -> int:
    """
    Main function
    """
    assert compute_area(-3, 0, 3, 4, 0, -1, 9, 2) == 45
    assert compute_area(-2, -2, 2, 2, -2, -2, 2, 2) == 16

    return 0

if __name__ == "__main__":
    exit(main())