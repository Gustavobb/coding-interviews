# Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree. You may assume that each node has a link to its parent.
# Binary Search Tree: a binary tree for which the following is valid for all nodes: the value in the node is greater than all values on the left sub-tree and less than or equal to all values in the right sub-tree.
# Think about how an in-order traversal works and try to "reverse engineer" it;
# Here's one step of the logic: The successor of a specific node is the leftmost node of the right subtree. What if there is no right subtree, though?

class TreeNode:
    """
    Tree node
    """
    def __init__(self, value=None, left=None, right=None, parent=None):
        """
        Constructor
        """
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def in_order_succ(node: TreeNode) -> TreeNode:
    """
    Find the in-order successor of a given node in a binary search tree
    """
    if node is None:
        return None
        
    if node.right:
        node = node.right
        while node.left: node = node.left
        return node

    p = node.parent
    while p and p.left != node:
        node = p
        p = p.parent
    return p

def main() -> int:
    """
    Main function
    """
    return 0

if __name__ == "__main__":
    exit(main())