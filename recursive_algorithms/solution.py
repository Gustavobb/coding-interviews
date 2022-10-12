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
            self.root = None
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


class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self, values):
        self.root = None
        if not values:
            return
        prev = None
        for value in values:
            node = LinkedListNode(value)
            if prev:
                prev.next = node
            if self.root is None:
                self.root = node
            prev = node

def list_sum(l: list[int]) -> int:
    return l.pop() + list_sum(l) if len(l) != 0 else 0

def digit_sum(n: int) -> int:
    return int(n % 10) + digit_sum(int(n / 10)) if n != 0 else 0

def tree_sum(root: TreeNode) -> int:
    return root.value + tree_sum(root.left) + tree_sum(root.right) if root is not None else 0

def tree_max(root: TreeNode) -> int:
    return max(root.value, tree_max(root.left), tree_max(root.right)) if root is not None else -float('inf') 

def k_combinations(l: list[int], k: int) -> list[list[int]]:
    if k == 0: return [[]]
    if len(l) == 0: return []
    return k_combinations(l[1:], k) + [[l[0]] + i for i in k_combinations(l[1:], k - 1)]

def all_strictly_increasing_sequences(k: int, n: int, **kwargs) -> list[list[int]]:
    return []

def create_pattern(n: int) -> list[int]:
    return [n] + create_pattern(n - 5) + [n] if n > 0 else [n]

def find_middle(head: LinkedListNode) -> LinkedListNode:
    # Don't change this function
    return find_middle_rec(head)[1]

def find_middle_rec(head: LinkedListNode, n: int=0) -> tuple[int, LinkedListNode]:
    # return the node in the middle of the linked list. Examples:
    # The list 1->2->3->4->5 should return 3;
    # The list 1->2->3->4->5->6 should return 4.
    # Hint: n will be used to count nodes from left to right and
    # the number returned by the function will be used to count the nodes from right to left

    if head is None: return (n, None)
    n, node = find_middle_rec(head.next, n + 1)
    n /= 2
    # TODO: implement this function