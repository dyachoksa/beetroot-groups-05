class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()
    
    def __bool__(self):
        return not self.is_empty()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return not self.items
        # or
        # return len(self.items) == 0


if __name__ == "__main__":
    stack = Stack()

    print("Push elements to stack:")
    print("'Item 1'...")
    stack.push("Item 1")
    print("'Item 2'...")
    stack.push("Item 2")
    print("'Item 3'...")
    stack.push("Item 3")

    print("\nPop elemets from stack:")
    # one-by-one
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())

    # or with loop
    while not stack.is_empty():
        print(stack.pop())
