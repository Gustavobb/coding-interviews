# https://leetcode.com/problems/bitwise-ors-of-subarrays/

# We have an array arr of non-negative integers.
# For every (contiguous) subarray sub = [arr[i], arr[i + 1], ..., arr[j]] (with i <= j), we take the bitwise OR of all the elements in sub, obtaining a result arr[i] | arr[i + 1] | ... | arr[j].
# Return the number of possible results. Results that occur more than once are only counted once in the final answer

# Input: arr = [0]
# Output: 1
# Explanation: There is only one possible result: 0.

# Input: arr = [1,1,2]
# Output: 3
# Explanation: The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
# These yield the results 1, 1, 2, 1, 3, 3.
# There are 3 unique values, so the answer is 3.

# Input: arr = [1,2,4]
# Output: 6
# Explanation: The possible results are 1, 2, 3, 4, 6, and 7.

def subarray_bitwise_ORs(arr: list[int]) -> int:
    """
    Return the number of possible results
    """
    result, previous = set(), set()
    
    for i in arr:
        curr = {i}
        for j in previous:
            curr.add(i | j)
        result |= curr
        previous = curr

    return len(result)

def main() -> int:
    """
    Main function
    """
    assert subarray_bitwise_ORs([0]) == 1
    assert subarray_bitwise_ORs([1,1,2]) == 3
    assert subarray_bitwise_ORs([1,2,4]) == 6

    return 0

if __name__ == "__main__":
    exit(main())