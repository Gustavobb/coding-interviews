# https://leetcode.com/problems/power-of-two/
# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Input: n = 1
# Output: true
# Explanation: 20 = 1

# Input: n = 16
# Output: true
# Explanation: 24 = 16

def is_power_of_two(self, n: int) -> bool:
    """
    Is power of two
    """
    return n > 0 and n & (n - 1) == 0

def main() -> int:
    """
    Main function
    """
    assert is_power_of_two(1) == True
    assert is_power_of_two(16) == True
    assert is_power_of_two(3) == False
    assert is_power_of_two(4) == True
    assert is_power_of_two(5) == False

    return 0

if __name__ == "__main__":
    exit(main())