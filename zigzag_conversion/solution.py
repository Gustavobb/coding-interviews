# https://leetcode.com/problems/zigzag-conversion/
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"

# Input: s = "A", numRows = 1
# Output: "A"

def convert(s: str, numRows: int) -> str:
    """
    Convert a string to a zigzag pattern
    """
    if numRows == 1: return s
    return_s = ""
    jump_pace =  numRows * 2 - 2
    len_s = len(s)

    for i in range(numRows):
        j = 0
        while j + i < len_s:
            return_s += s[j + i]
            if i != 0 and i != numRows - 1 and j + jump_pace - i < len_s:
                return_s += s[j + jump_pace - i];

            j += jump_pace
        
    return return_s

def main() -> int:
    """
    Main function
    """
    assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert convert("A", 1) == "A"

    return 0

if __name__ == "__main__":
    exit(main())