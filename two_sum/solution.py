# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Input: nums = [3,3], target = 6
# Output: [0,1]

def two_sum(nums: list[int], target: int) -> list[int]:
    '''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
    '''
    seen = {}
    for i, v in enumerate(nums):
        remaining = target - nums[i]
        if remaining in seen:
            return [i, seen[remaining]]

        seen[v] = i

def main() -> int:
    """
    Main function
    """
    assert two_sum([2,7,11,15], 9) == [0,1] or two_sum([2,7,11,15], 9) == [1,0]
    assert two_sum([3,2,4], 6) == [1,2] or two_sum([3,2,4], 6) == [2,1]
    assert two_sum([3,3], 6) == [0,1] or two_sum([3,3], 6) == [1,0]

    return 0

if __name__ == "__main__":
    exit(main())