class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __len__(self):
        return self.size()
    
    def __bool__(self):
        return not self.is_empty()

    def append(self, value):
        """ Has O(1) complexity """

        node = Node(value)

        node.next = self.head
        self.head = node

    def pop(self):
        """ Has O(1) complexity """

        if self.head is None:
            return None
        
        node = self.head
        self.head = node.next

        return node.value

    def is_empty(self):
        """ Has O(1) complexity """
        return self.head is None

    def size(self):
        """ Has O(n) complexity """

        size = 0

        if self.head is None:
            return size

        current_node = self.head
        while current_node is not None:
            size += 1
            current_node = current_node.next

        return size
    
    def search(self, value):
        """ Has complexity O(1) in best case and O(n) in worse case """

        if self.head is None:
            return False
        
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            
            current = current.next
        
        return False


if __name__ == "__main__":
    a_list = LinkedList()

    a_list.append(100)
    a_list.append(200)

    print("Size:", a_list.size())
    print(a_list.pop())
    print("Size:", a_list.size())
    print(a_list.pop())

    print("Is empty?", a_list.is_empty())
