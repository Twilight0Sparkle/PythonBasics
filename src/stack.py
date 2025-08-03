class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self):
    self.head = None
    self._size = 0

  # Method to add item into stack
  def push(self, value):
    new_node = Node(value)
    if self.head:
      new_node.next = self.head
    self.head = new_node
    self._size += 1

  # Method to remove the most recently added item and return its value
  def pop(self):
    if self.is_empty():
      return None
    popped_node = self.head
    self.head = self.head.next
    self._size -= 1
    return popped_node.value

  # Method to get value of top item
  def peek(self):
    if self.is_empty():
      return None
    return self.head.value

  def is_empty(self):
    return self._size == 0

  def clear(self):
    self.__init__()

  def __len__(self):
    return self._size

  # Method to display current stack
  def traverse(self):
    current = self.head
    while current:
      print(current.value, end=" -> ")
      current = current.next
    print("None")

if __name__ == '__main__':

  # Method to check whether brackets balanced or not
  def is_balanced(st):
    stack = Stack() # Creating empty stack for future operations
    brackets = {')': '(', '}': '{', ']': '['} # Creating dict that maps brackets(key:value)
    opening_brackets = {'(', '{', '['}
    for char in st: # Here we iterate through each char in string
      if char in opening_brackets:  # Check in order to determine whether char is opening bracket(is on dict)
        stack.push(char) # So if it's an opening bracket then add to stack it's mapped value(or idk how to tell this different lol)
      elif char in brackets:  # So if it's not opening bracket, then we do check if it's a closing bracket
        if stack.is_empty() or stack.pop() != brackets[char]: # So if our stack is empty OR our popped opening bracket doesnt match closing bracket then return false
          return False
    return stack.is_empty() # This stuff is balanced if stack is empty at the end so

  my_stack = Stack()
  my_stack.push('A') # A -> None
  my_stack.push('B') # B -> A -> None
  my_stack.traverse() # ^^^
  my_stack.push('C') # C -> B -> A -> None
  my_stack.traverse() # ^^^
  print(my_stack.pop()) # C
  my_stack.traverse() # B -> A -> None
  print(is_balanced('([])')) # True
  print(is_balanced("([])()")) # True
  print(is_balanced("([])(")) # False
  print(is_balanced("([{])")) # False
  print(is_balanced("([[])")) # False
  print(is_balanced("([[]])")) # True