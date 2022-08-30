# https://leetcode.com/problems/palindrome-number/
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

def is_palindrome(x: int) -> bool:
    s_int = str(x)
    len_s_int = len(s_int)
    for i in range(int(len_s_int / 2)):
        if s_int[i] != s_int[len_s_int - 1 - i]: return False
    
    return True

def main() -> int:
    """
    Main function
    """
    assert is_palindrome(-121) == False
    assert is_palindrome(121) == True

if __name__ == "__main__":
    main();
    exit(0);