# https://leetcode.com/problems/circle-and-rectangle-overlapping/description/

# You are given a circle represented as (radius, xCenter, yCenter) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.
# Return true if the circle and rectangle are overlapped otherwise return false. In other words, check if there is any point (xi, yi) that belongs to the circle and the rectangle at the same time.

# Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
# Output: true
# Explanation: Circle and rectangle share the point (1,0).

# Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
# Output: false

# Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
# Output: true

def check_overlap(radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
    """
    Check if the circle and rectangle are overlapped.
    """
    rec_center_x = (x2 + x1) / 2
    rec_center_y = (y2 + y1) / 2
    
    diff_center_x = abs(x_center - rec_center_x) 
    diff_center_y = abs(y_center - rec_center_y)
    
    half_rec_x = (x2 - x1) / 2 
    half_rec_y = (y2 - y1) / 2
        
    diff = max(0, diff_center_x - half_rec_x) ** 2 + max(0, diff_center_y - half_rec_y) ** 2
    return (diff <= radius ** 2)

def main() -> int:
    """
    Main function
    """
    assert check_overlap(1, 0, 0, 1, -1, 3, 1) == True
    assert check_overlap(1, 1, 1, 1, -3, 2, -1) == False
    assert check_overlap(1, 0, 0, -1, 0, 0, 1) == True

if __name__ == "__main__":
    exit(main())
