class Node:
    # Node init
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

    # Method to check whether there is next node or not
    def has_next(self):
        return self.next is not None

    # Method to check whether there is prev node or not
    def has_prev(self):
        return self.prev is not None

class DoubleLinkedList:
    # Double-Linked list init
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # Method to check whether current list is empty or not
    def is_empty(self):
        return self._size == 0

    # Method which adds object at the beginning of the list
    def insert(self, data):
        new_node = Node(data)

        self._size += 1

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Method which adds object at the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    # Method to delete certain object in the list
    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self._size -= 1
                return True  # Deleted successfully
            current = current.next
        return False  # Not found lol

    # Method to search certain object in the list
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next  # Assign the next node to the current node
        else:
            return False

    # Method to clear whole list (re-init itself)
    def clear(self):
        self.__init__()

    # Method to check actual size of current list
    def __len__(self):
        return self._size

    # Method to display all the elements from beginning to end
    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Method to display all the elements from end to beginning
    def traverse_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")

# # # # # # # # # # # # #

if __name__ == "__main__":
    my_list = DoubleLinkedList()

    my_list.insert(20)
    my_list.insert(30)
    my_list.append(10)
    my_list.append(40)

    print("Traverse forward")
    my_list.traverse_forward()  # 5 -> 10 -> 20 -> 30 -> None

    print("Traverse backwards")
    my_list.traverse_backward()  # 30 -> 20 -> 10 -> 5 -> None

    print("Search elem. 20:", my_list.search(20))  # True
    print("Search elem. 22:", my_list.search(22))  # False

    my_list.delete(10)
    print("10 got deleted!")
    my_list.traverse_forward()  # 5 -> 20 -> 30 -> None

    my_list.delete(13)
    print("tried to delete 13!")
    my_list.traverse_forward()  # 20 -> 30 -> None

    my_list.delete(30)
    print("30 got deleted!")
    my_list.traverse_forward()  # 20 -> None