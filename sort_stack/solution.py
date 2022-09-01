# Write a program to sort a stack such that the smallest items are on the top. The stack supports the following operations: push, pop, peek, and is_empty.
# You may not copy the elements into any other data structure (such as an array);
# You can use an additional temporary stack, but not two.
# One way of sorting an array is to iterate through the array and insert each element into a new array in sorted order. Can you do this with a stack?
# Imagine your secondary stack is sorted. Can you insert elements into it in sorted order? You might need some extra storage. What could you use for extra storage?
# Keep the secondary stack in sorted order, with the biggest elements on the top. Use the primary stack for additional storage.

class Stack:
    """
    Stack class
    """
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)


def sort_stack(stack: Stack) -> None:
    """
    Sort stack
    """
    sorted_stack = Stack()
    while not stack.is_empty():
        tmp = stack.pop()

        while not sorted_stack.is_empty() and sorted_stack.peek() < tmp:
            stack.push(sorted_stack.pop())
        
        sorted_stack.push(tmp)
    
    stack._items = sorted_stack._items

def check(values):
    stack = Stack()
    stack._items = [v for v in values]
    sort_stack(stack)
    assert stack._items == sorted(values, reverse=True)

def main() -> int:
    """
    Main function
    """
    check([])
    check([1])
    check([7, 10, 5, 3, 1, 8, 12])
    check(list(range(10, 0, -1)))
    return 0

if __name__ == "__main__":
    exit(main())