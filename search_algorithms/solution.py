from collections import deque

class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, representation: str):
        '''
        representation: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        if not representation:
            return
        nodes = []
        for i, value in enumerate(representation):
            node = None
            if value is not None:
                node = TreeNode(value)
                if i > 0:
                    if i % 2 == 1:
                        parent = nodes[(i - 1) // 2]
                        parent.left = node
                    else:
                        parent = nodes[(i - 2) // 2]
                        parent.right = node
            nodes.append(node)
        self.root = nodes[0]

class GraphNode:
    def __init__(self, value=None):
        self.value = value
        self.adjacent = []

class Graph:
    def __init__(self, adjacency: list[list[bool]]):
        '''
        adjacency: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        self.nodes = [GraphNode(i) for i in range(1, len(adjacency) + 1)]
        for node1, row in zip(self.nodes, adjacency):
            for node2, adjacent in zip(self.nodes, row):
                if adjacent and node1 is not node2:
                    node1.adjacent.append(node2)

def pre_order_recursive(root: TreeNode) -> None:
    '''
    Pre-order traversal of a binary tree.
    '''
    print(root.value)
    if root.left: pre_order_recursive(root.left)
    if root.right: pre_order_recursive(root.right)

def pre_order_iterative(root: TreeNode) -> None:
    '''
    Pre-order traversal of a binary tree.
    '''
    stack = deque()
    stack.append(root)

    while len(stack) != 0:
        node = stack.pop()
        print(node.value)
        if node.left: stack.append(node.right)
        if node.left: stack.append(node.left)

def in_order_recursive(root: TreeNode) -> None:
    '''
    In-order traversal of a binary tree.
    '''
    if root.left: in_order_recursive(root.left)
    print(root.value)
    if root.right: in_order_recursive(root.right)

def post_order_recursive(root: TreeNode) -> None:
    '''
    Post-order traversal of a binary tree.
    '''
    if root.left: post_order_recursive(root.left)
    if root.right: post_order_recursive(root.right)
    print(root.value)

def breadth_first(root: TreeNode) -> None:
    stack = deque()
    stack.append(root)

    while len(stack) != 0:
        node = stack.peek()
        if node.left: stack.append(node.right)
        if node.left: stack.append(node.left)
    
    print(stack)

def graph_depth_first_recursive(node: GraphNode, visited=None) -> None:
    if visited is None:
        visited = set()

def graph_depth_first_iterative(node: GraphNode) -> None:
    pass

def graph_breadth_first(node: GraphNode) -> None:
    pass