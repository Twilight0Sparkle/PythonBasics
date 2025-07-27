class Node:
    # Node init
    def __init__(self, data):
        self.data = data
        self.next = None

    # Method to get data of the node
    def get_data(self):
        return self.data

    # Method to set data of the node
    def set_data(self, data):
        self.data = data
        return self.data

    # Method to set next node' value
    def set_next(self, next):
        self.next = next

    # Method to receive next node
    def get_next(self):
        return self.next

    # Method to check whether there is next node or not
    def has_next(self):
        return self.next is not None


class LinkedList:
    # Linked list init
    def __init__(self):
        self.head = None

    # Method to check whether current list is empty or not
    def is_empty(self):
        return self.head is None

    # Method which adds object at the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Method which adds object at the beginning of the list
    def insert(self, data):
        new_node = Node(data)
        new_node.set_data(data)
        if self.size() == 0:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    # Method to search certain object in the list
    def search(self, data=None):
        index = 0
        current = self.head
        while current is not None:
            if Node.get_data(current) == data:
                print(f"Found {data} at position {index}")
                return True
            index += 1 # Increment the position
            current = Node.get_next(current) # Assign the next node to the current node
        else:
            print(f"Cannot find {data} at any position")
            return False

    # Method to remove first object in the list
    def remove_first(self):
        if self.head is None:
            return
        self.head = self.head.next

    # Method to remove last object in the list
    def remove_last(self):
        if self.head is None:
            return
        current = self.head
        while current.next is not None and current.next.next is not None:
            current = current.next
        current.next = None

    # Method to delete certain object in the list
    def delete(self, data):
        current = self.head

        # Check if the head node contains the specified data
        if current.data == data:
            self.remove_first()
            return

        while current is not None and current.next.data != data:
            current = current.next
        if current is None:
            return
        else:
            current.next = current.next.next

    # Method to clear whole list (re-init itself)
    def clear(self):
        self.__init__()

    # Method to check actual size of current list
    def size(self):
        size = 0
        if self.head:
            current = self.head
            while current:
                size = size + 1
                current = current.next
            return size
        else:
            return 0

    # Method to output whole list
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

# # # # # # # # # # # # #

my_list = LinkedList() # List init
my_list.append(30) # Add new object at the end of the list
my_list.append(40) # ^^^
my_list.append(50) # ^^^
my_list.insert(10) # Add new object at the beginning of the list
my_list.insert(20) # ^^^
my_list.display() # Output: 20 -> 10 -> 30 -> 40 -> 50
print("Size:", my_list.size()) # Prints size of this list
my_list.search(5) # Search results
my_list.search(10) # Search results
my_list.display() # Output: 20 -> 10 -> 30 -> 40 -> 50
my_list.delete(10) # Deletes element '10'
my_list.display() # Output: 20 -> 30 -> 40 -> 50
my_list.search(10) # Search results
my_list.display() # Output: 20 -> 30 -> 40 -> 50
print("Size:", my_list.size()) # Prints size of this list