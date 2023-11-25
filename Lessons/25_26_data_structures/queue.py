class Queue:
    def __init__(self):
        self.items = []
    
    def __len__(self):
        return self.size()
    
    def __bool__(self):
        return not self.is_empty()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    queue = Queue()

    print("Add elements to the queue:")
    print("Item 1")
    queue.enqueue("Item 1")
    print("Item 2")
    queue.enqueue("Item 2")
    print("Item 3")
    queue.enqueue("Item 3")

    print("Get elements from the queue:")
    while not queue.is_empty():
        print(queue.dequeue())
