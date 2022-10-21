# https://leetcode.com/problems/valid-parentheses/description/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Input: s = "()"
# Output: true

# Input: s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false

from collections import deque

def is_valid(self, s: str) -> bool:
    """
    Returns True if the input string is valid, False otherwise.
    """
    stack = deque()
    brackets_match = {"}" : "{", "]" : "[", ")" : "("}
    for c in s:
        if c in brackets_match:
            if len(stack) == 0 or stack.pop() != brackets_match[c]: return False
            continue

        stack += [c]
    
    return len(stack) == 0

def main() -> int:
    """
    Main function.
    """
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False
    assert is_valid("([)]") == False
    assert is_valid("{[]}") == True

    return 0

if __name__ == "__main__":
    exit(main())