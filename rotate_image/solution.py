# https://leetcode.com/problems/rotate-image/
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

def rotate(matrix: list[list[int]]) -> list[list[int]]:
    """
    Rotate a matrix by 90 degrees
    """
    transpose_matrix(matrix)
    reverse_matrix(matrix)
    return matrix
    
def transpose_matrix(matrix: list[list[int]]) -> None:
    """
    Transpose a matrix
    """
    n = len(matrix)
    for row in range(n):
        for column in range(row + 1, n):
            matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]

def reverse_matrix(matrix: list[list[int]]) -> None:
    """
    Reverse a matrix
    """
    n = len(matrix)
    for row in range(n):
        matrix[row] = matrix[row][::-1]

def main() -> int:
    """
    Main function
    """
    assert rotate([[1,2,3],[4,5,6],[7,8,9]]) == [[7,4,1],[8,5,2],[9,6,3]]
    assert rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]) == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    return 0

if __name__ == "__main__":
    exit(main())