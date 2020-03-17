# Stack is first in last out.
# A queue is the reverse of a stack.


class Stacks(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        # Push the element at the last index.
        self.items.append(item)

    def pop(self):
        # Remove the last element
        self.items.pop()

    def peek(self):
        # Produce the length of the items
        if self.items:
            return len(self.items)
        else:
            return None

    def is_empty(self):
        # Return last element in the stack
        if not self.items:
            return True
        else:
            return False


if __name__ == "__main__":
    stack = Stacks()
    stack.push(1)
    stack.push(2)
    print(stack.is_empty())
    print(stack.peek())
    stack.pop()
    print(stack.is_empty())


