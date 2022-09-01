# Given two linked lists, determine if the two lists intersect. Return the intersection node.
# Intersection: the intersection of two linked lists is based on reference, not value. In other words, even if two lists have nodes with the same value, that doesn't mean they intersect.
# The lists are singly linked, i.e. there is no pointer to the previous node.
# Examples are useful. Draw two linked lists with an intersection and two equivalent lists that don't intersect;
# Start by checking if there is an intersection before looking for the exact place it occurs;
# Note that if two lists intersect, they will always share the last node. Once they intersect, all following nodes are shared;
# After you have determined that the two lists intersect, you have to find the intersection node. If the two lists had the exact same length, how would you solve the problem?
# If the two lists had the same length, you could traverse them in parallel until you find a shared node. Now, how can you adapt this idea to lists with different lengths?
# Is the length difference useful for anything?

class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt
    
class LinkedList:
    def __init__(self, head):
        self.head = head
        self.get_tail_and_size()
    
    def get_tail_and_size(self):
        """
        Get tail node and size of linked list
        """
        self.tail = self.head
        self.size = 0

        while self.tail.next != None:
            self.tail = self.tail.next
            self.size += 1

def find_intersection_same_size(l_list_1: LinkedList, l_list_2: LinkedList) -> Node:
    """
    Find the intersection node of two linked lists of same sizes
    """
    node_1 = l_list_1.head
    node_2 = l_list_2.head
    for i in range(l_list_1.size):
        if node_1.next == node_2.next: return node_1.next
        node_1 = node_1.next
        node_2 = node_2.next
    
    return

def find_intersection_diff_size(l_list_1: LinkedList, l_list_2: LinkedList) -> Node:
    """
    Find the intersection node of two linked lists of different sizes
    """
    longest_l_list = l_list_2
    shortest_l_list = l_list_1
    if l_list_1.size > l_list_2.size:
        longest_l_list = l_list_1
        shortest_l_list = l_list_2

    new_head = longest_l_list.head
    size_diff = abs(l_list_1.size - l_list_2.size)
    for i in range(size_diff):
        new_head = new_head.next
    
    longest_l_list.head = new_head
    return find_intersection_same_size(longest_l_list, shortest_l_list)

def find_intersection(head1: Node, head2: Node) -> Node:
    """
    Find the intersection node of two linked lists
    """
    if head1 == None or head2 == None: return
    if head1 == head2: return head1

    l_list_1 = LinkedList(head1)
    l_list_2 = LinkedList(head2)

    if not has_intersection(l_list_1, l_list_2): return

    if l_list_1.size == l_list_2.size: return find_intersection_same_size(l_list_1, l_list_2)
    return find_intersection_diff_size(l_list_1, l_list_2)

def has_intersection(l_list_1: LinkedList, l_list_2: LinkedList) -> bool:
    """
    Determine if two linked lists intersect
    """
    if l_list_1.tail != l_list_2.tail: return False
    return True

def main() -> int:
    """
    Main function
    """
    return 0

if __name__ == "__main__":
    exit(main());