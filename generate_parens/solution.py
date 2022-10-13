# Implement an algorithm to print all valid (e.g., properly opened and closed) combinations of n pairs of parentheses.
# Input: 3
# Output: ((())), (()()), (())(), ()(()), ()()()

def generate_parens(n: int) -> list[str]:
    """
    Generate all valid combinations of n pairs of parentheses
    """
    answer = []

    def add_parens(left: int, right: int, string: str) -> None:
        """
        Add parentheses to string
        """
        nonlocal answer
        if left == 0 and right == 0: return answer.append(string)
        if left > 0: add_parens(left - 1, right, string + "(")
        if right > left: add_parens(left, right - 1, string + ")")

    add_parens(n, n, "")
    return answer
    
def main() -> int:
    """
    Main function
    """
    assert generate_parens(0) == [""]
    assert generate_parens(1) == ["()"]
    assert generate_parens(2) == ["(())", "()()"]
    assert generate_parens(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert generate_parens(4) == ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]
    return 0

if __name__ == "__main__":
    exit(main())