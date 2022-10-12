# You have an integer matrix representing a plot of land, where the value at that location represents the height above sea level. 
# A value of zero indicates water. A pond is a region of water connected vertically, horizontally, or diagonally. 
# The size of the pond is the total number of connected water cells. Write a method to compute the sizes of all ponds in the matrix.

# Input:
# 0 2 1 0
# 0 1 0 1
# 1 1 0 1
# 0 1 0 1

# Output: 2, 4, 1 (in any order)
import copy

def compute_pond_sizes(land: list[list[int]]) -> list[int]:
    """
    Compute the sizes of all ponds in the matrix
    """
    land_copy = copy.deepcopy(land)
    pond_sizes = []

    def compute_pond_size(row: int, col: int) -> int:
        """
        Compute the size of a pond
        """
        nonlocal land_copy
        if (row < 0 or row >= len(land_copy)) or (col < 0 or col >= len(land_copy[0])) or (land_copy[row][col] != 0): return 0

        land_copy[row][col] = -1
        size = 1

        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                size += compute_pond_size(r, c)
        
        return size

    for row in range(len(land_copy)):
        for col in range(len(land_copy[row])):
            if land_copy[row][col] == 0:
                pond_sizes.append(compute_pond_size(row, col))
    
    print(land_copy, land)
    return pond_sizes

def main() -> int:
    """
    Main function
    """
    assert compute_pond_sizes([[1]]) == []
    assert compute_pond_sizes([[0]]) == [1]
    assert compute_pond_sizes([[0, 2, 1, 0], 
                               [0, 1, 0, 1], 
                               [1, 1, 0, 1], 
                               [0, 1, 0, 1]]) == [2, 4, 1]

    assert compute_pond_sizes([[0, 2, 1, 0],
                               [0, 1, 0, 1],
                               [1, 1, 0, 1],
                               [0, 1, 0, 1]]) == [2, 4, 1]

    assert compute_pond_sizes([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                               [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                               [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                               [1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
                               [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
                               [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
                               [1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
                               [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                               [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == [16, 16]

    assert compute_pond_sizes([[0, 1, 1, 0, 0, 0, 1, 1, 0, 1],
                               [0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
                               [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                               [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
                               [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                               [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
                               [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                               [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
                               [0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                               [1, 0, 0, 0, 1, 1, 0, 1, 1, 0]]) == [19, 19, 10]

    return 0

if __name__ == "__main__":
    exit(main())