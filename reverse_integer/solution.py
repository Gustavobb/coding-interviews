# https://leetcode.com/problems/reverse-integer/submissions/
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the 
# signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Input: x = 123
# Output: 321

# Input: x = -123
# Output: -321

# Input: x = 120
# Output: 21

def reverse(x: int) -> int:
    """
    Reverse integer
    """
    str_x = str(abs(x))
    reversed_x = ""
    if x < 0: reversed_x = "-"

    reversed_x = int(reversed_x + str_x[::-1])
    if reversed_x < -2**31 or reversed_x > 2**31 - 1: return 0
    return reversed_x

def main() -> int:
    """
    Main function
    """
    assert reverse(-123) == -321
    assert reverse(123) == 321
    assert reverse(120) == 21
    assert reverse(0) == 0
    assert reverse(1534236469) == 0

if __name__ == "__main__":
    exit(main());