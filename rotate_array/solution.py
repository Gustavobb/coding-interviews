# https://leetcode.com/problems/rotate-array/
# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# Input: nums = [1, 2, 3, 4], k = 3
# Output: [2, 3, 4, 1]
# Explanation: 
# rotate 1 steps to the right: [4, 1, 2, 3]
# rotate 2 steps to the right: [3, 4, 1, 2]
# rotate 2 steps to the right: [2, 3, 4, 1]

def rotate(nums: list[int], k: int) -> list[int]:
    """
    Rotate array
    """
    rotated_nums = nums.copy()

    for idx in range(len(nums)):
        nums[(idx + k) % len(nums)] = rotated_nums[idx]
    
    return nums

def main() -> int:
    """
    Main function
    """
    assert rotate([1, 2, 3, 4], 3) == [2, 3, 4, 1]
    assert rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
    assert rotate([1, 2, 3, 4, 5, 6], 2) == [5, 6, 1, 2, 3, 4]
    assert rotate([1, 2, 3, 4, 5, 6], 4) == [3, 4, 5, 6, 1, 2]
    assert rotate([1, 2, 3, 4, 5, 6], 6) == [1, 2, 3, 4, 5, 6]
    assert rotate([1, 2, 3, 4, 5, 6], 7) == [6, 1, 2, 3, 4, 5]
    assert rotate([1, 2, 3, 4, 5, 6], 8) == [5, 6, 1, 2, 3, 4]

    return 0

if __name__ == "__main__":
    exit(main())