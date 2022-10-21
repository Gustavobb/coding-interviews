# https://leetcode.com/problems/all-possible-full-binary-trees/description/

# Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.
# Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.
# A full binary tree is a binary tree where each node has exactly 0 or 2 children.

# Input: n = 7
# Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

# Input: n = 3
# Output: [[0,0,0]]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def all_possible_full_binary_trees(n: int) -> list[TreeNode]:
    """
    Returns a list of all possible full binary trees with n nodes.
    """
    if n % 2 == 0: return []
    if n == 1: return [TreeNode(0)]
    
    ret = []
    for childs in range(1, n, 2):
        for left_child in all_possible_full_binary_trees(childs):
            for right_child in all_possible_full_binary_trees(n - childs - 1):
                ret += [TreeNode(0, left_child, right_child)]
                
    return ret

def main() -> int:
    """
    Main function.
    """

    assert all_possible_full_binary_trees(7) == [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
    assert all_possible_full_binary_trees(3) == [[0,0,0]]

    return 0

if __name__ == "__main__":
    exit(main())