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
    pass

def main() -> int:
    """
    Main function
    """
    return 0

if __name__ == "__main__":
    exit(main())