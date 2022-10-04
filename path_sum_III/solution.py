# https://leetcode.com/problems/path-sum-iii/

# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        '''
        TreeNode class
        '''
        self.val = val
        self.left = left
        self.right = right

def path_sum(root: TreeNode, target_sum: int) -> int:
    """
    Path sum
    """
    sums = {0: 1}

    def calculate(node: TreeNode, current_sum: int, result: int) -> int:
        if not node: return result

        current_sum += node.val
        result += sums.get(current_sum - target_sum, 0)
        sums[current_sum] = sums.get(current_sum, 0) + 1
        result = calculate(node.left, current_sum, result)
        result = calculate(node.right, current_sum, result)
        sums[current_sum] -= 1
        return result
    
    return calculate(root, 0, 0)

def main() -> int:
    """
    Main function
    """
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(11)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)
    assert path_sum(root, 8) == 3

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    assert path_sum(root, 22) == 3

    return 0

if __name__ == "__main__":
    exit(main())