# https://leetcode.com/problems/rectangle-overlap/description/

# An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, 
# and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.
# Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.
# Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true

# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false

# Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
# Output: false

def is_rectangle_overlap(self, rec1: list[int], rec2: list[int]) -> bool:
    """
    Determine if two rectangles overlap
    """
    return compute_area_intersection(rec1, rec2) > 0

def compute_area_intersection(rec1: list[int], rec2: list[int]) -> int:
    """
    Compute the area of the intersection of two rectangles
    """
    x_overlap = max(0, min(rec1[2], rec2[2]) - max(rec1[0], rec2[0]))
    y_overlap = max(0, min(rec1[3], rec2[3]) - max(rec1[1], rec2[1]))

    return x_overlap * y_overlap

def main() -> int:
    """
    Main function
    """
    assert is_rectangle_overlap([0, 0, 2, 2], [1, 1, 3, 3]) is True
    assert is_rectangle_overlap([0, 0, 1, 1], [1, 0, 2, 1]) is False
    assert is_rectangle_overlap([0, 0, 1, 1], [2, 2, 3, 3]) is False

    return 0

if __name__ == "__main__":
    exit(main())