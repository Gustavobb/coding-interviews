# https://leetcode.com/problems/valid-square/

# Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.
# The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.
# A valid square has four equal sides with positive length and four equal angles (90-degree angles).

# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: true

# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
# Output: false

# Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
# Output: true

def valid_square(p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
    """
    Return True if the four points construct a square
    """
    point = [p1, p2, p3, p4]
    hypotenuse = 0
    cathetus = dist(p1, p2)
    
    for i in range(len(point)):
        for j in range(i + 1, len(point)):
            d = dist(point[i], point[j])
            if d > hypotenuse: hypotenuse = d
            elif d < cathetus: cathetus = d
    
    if hypotenuse == cathetus: return False
    return hypotenuse == (cathetus * 2)

def dist(p0: list[int], p1: list[int]) -> float:
    """
    Return the distance between two points
    """
    return (p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2
    
def main() -> int:
    """
    Main function
    """
    assert valid_square([0,0], [1,1], [1,0], [0,1]) == True
    assert valid_square([0,0], [1,1], [1,0], [0,12]) == False
    assert valid_square([1,0], [-1,0], [0,1], [0,-1]) == True

    return 0

if __name__ == "__main__":
    exit(main())