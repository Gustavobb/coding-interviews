# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
# Given a string array words, return the maximum value of length(word[i]) * length(word[j])
#  where the two words do not share common letters. If no such two words exist, return 0.

# Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16
# Explanation: The two words can be "abcw", "xtfn".

# Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4
# Explanation: The two words can be "ab", "cd".

# Input: words = ["a","aa","aaa","aaaa"]
# Output: 0
# Explanation: No such pair of words.

def max_product(words: list[str]) -> int:
    """
    Return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters.
    """
    words_size = len(words)
    masks = [0 for _ in range(words_size)]
    
    for idx in range(words_size):             
        for char in words[idx]: masks[idx] |= 1 << (ord(char) - ord('a'))
    
    max_p = 0
    for i in range(words_size):
        for j in range(i + 1, words_size):
            if not (masks[i] & masks[j]):
                max_p = max(max_p, len(words[i]) * len(words[j]))
    
    return max_p

def main() -> int:
    """
    Main function
    """
    assert max_product(["abcw","baz","foo","bar","xtfn","abcdef"]) == 16
    assert max_product(["a","ab","abc","d","cd","bcd","abcd"]) == 4
    assert max_product(["a","aa","aaa","aaaa"]) == 0

    return 0

if __name__ == "__main__":
    exit(main())