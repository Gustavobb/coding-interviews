# You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to find the length of the longest sequence of 1s you could create.
# Input: 1775 (or: 11011101111); Output: 8

# Start with a brute force solution. Can you try all possibilities?
# Flipping a 0 to a 1 can merge two sequences of 1s - but only if the two sequences are separated by only one O.
# Each sequence can be lengthened by merging it with an adjacent sequence (if any) or just flipping the immediate neighboring zero. You just need to find the best choice.
# Try to do it in linear time, a single pass, and 0 (1) space.
BITS = 32

def longest_sequence(n: int) -> int:
    """
    Have an integer and you can flip exactly one bit from a 0 to a 1. 
    Find the length of the longest sequence of 1s you could create.
    """
    if ~n == 0:
        return BITS

    for i in range(BITS):
        print(n & 1, n)
        n >>= 1

def main() -> int:
    """
    Main function
    """
    assert longest_sequence(1775) == 8

    return 0

if __name__ == "__main__":
    exit(main())