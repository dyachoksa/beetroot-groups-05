class Deque:
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()
    
    def __bool__(self):
        return not self.is_empty()

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop()

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    deque = Deque()

    # add items
    deque.add_front(100)
    deque.add_front(200)
    deque.add_rear(300)
    deque.add_front(400)

    # get elements
    print(deque.remove_rear())
    print(deque.remove_rear())
    print(deque.remove_front())
    print(deque.remove_rear())
