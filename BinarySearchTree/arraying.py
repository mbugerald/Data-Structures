from random import randint
import time


class Node(object):

    def __init__(self, value=None):
        self.parent = value
        self.left_child = []
        self.right_child = []

    def print_root_node(self):
        return "Root node", self.parent

    def print_left_children(self):
        # Print out all the elements in the left child
        return "Left Children", self.left_child

    def print_right_children(self):
        # Print out all the elements int he right child
        return "Right children", self.right_child


class BinarySearchTree(Node):

    def __init__(self):
        super().__init__()

    def insert(self, value):
        # Adding values to the given nodes
        if self.parent is None:
            self.parent = value
        else:
            self._insert(value, self.parent)

    def _insert(self, value, cur_node):
        if value < cur_node:
            # Insert in the left child.
            self.left_child.append(value)
        elif value > cur_node:
            # Insert in the right child.
            self.right_child.append(value)
        else:
            print("Value already exist!")


start_time = time.time()
tree = BinarySearchTree()
tree.insert(randint(1, 10))
for value in range(1, 10):
    tree.insert(value)

print(tree.print_root_node())
print(tree.print_left_children())
print(tree.print_right_children())
print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
tree = BinarySearchTree()
tree.insert(randint(1, 10))
i = 1
while i <= 10:
    tree.insert(i)
    i += 1

print(tree.print_root_node())
print(tree.print_left_children())
print(tree.print_right_children())
print("--- %s seconds ---" % (time.time() - start_time))
