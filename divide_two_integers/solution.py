# https://leetcode.com/problems/divide-two-integers/
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
# Return the quotient after dividing dividend by divisor.
# Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.

# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.

def divide(dividend: int, divisor: int) -> int:
    """
    Divide two integers without using multiplication, division, and mod operator. 
    """
    quotient = 0
    MAX_Q = 2**31 - 1
    MIN_Q = -2**31

    operator_divisor = -1 if divisor < 0 else 1
    operator_dividend = -1 if dividend < 0 else 1
    dividend *= operator_dividend
    divisor *= operator_divisor
    neg = operator_divisor * operator_dividend

    if dividend == -MIN_Q and divisor == 1:
        if neg == -1: return MIN_Q
        return MAX_Q
    
    if divisor > dividend: return 0
    if divisor == 1: return neg * dividend

    while (dividend - divisor * quotient) >= divisor:
        quotient += 1

    return quotient * neg

def main() -> int:
    """
    Main function
    """
    assert divide(10, 3) == 3
    assert divide(7, -3) == -2
    assert divide(0, 1) == 0
    assert divide(1, 1) == 1
    assert divide(-1, 1) == -1
    assert divide(1, -1) == -1
    assert divide(-1, -1) == 1
    assert divide(2**31 - 1, 1) == 2**31 - 1

    return 0

if __name__ == "__main__":
    exit(main())