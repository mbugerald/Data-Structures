# First in first out


class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        # Check if the items list is empty
        return not self.items

    def enqueue(self, item):
        # Insert element into a given index space in list
        try:
            self.items.insert(0, item)
            return self.items
        except Exception as e:
            return str(e)

    def denqueue(self):
        # Remove element into a given index space in list
        try:
            self.items.pop()
            return self.items
        except Exception as e:
            return str(e)


if __name__ == "__main__":
    queue = Queue()
    print(queue.is_empty())
    print(queue.enqueue(1))
    print(queue.enqueue(3))
    print(queue.enqueue(2))
    print(queue.denqueue())
