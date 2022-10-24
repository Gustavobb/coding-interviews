# https://leetcode.com/problems/first-missing-positive/description/

# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.

def first_missing_positive(nums: list[int]) -> int:
    """
    Returns the smallest missing positive integer in the list.
    """
    nums.sort() # O(nlogn)
    answer = 1

    for num in nums: # O(n)
        if num == answer:
            answer += 1

    return answer

def main() -> int:
    """
    Main function.
    """
    assert first_missing_positive([1,2,0]) == 3
    assert first_missing_positive([3,4,-1,1]) == 2
    assert first_missing_positive([7,8,9,11,12]) == 1

    return 0

if __name__ == "__main__":
    exit(main())
