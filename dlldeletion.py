class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
      
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def display(self):
       
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" <-> ".join(elements) if elements else "List is empty")

    def delete_node(self, target_node):
        
        if not self.head or not target_node:
            return

        # Case 1: Deleting the head node
        if self.head == target_node:
            self.head = target_node.next

        # Case 2: Node is NOT the last node (update next node's prev pointer)
        if target_node.next is not None:
            target_node.next.prev = target_node.prev

        # Case 3: Node is NOT the first node (update previous node's next pointer)
        if target_node.prev is not None:
            target_node.prev.next = target_node.next

        # Free the memory (Optional in Python, but good practice)
        target_node.next = None
        target_node.prev = None

        # Create list: 10 <-> 20 <-> 30
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
print("Original list:")
dll.display() 

# Delete the middle node (20)
node_to_delete = dll.head.next
dll.delete_node(node_to_delete)

print("After deleting 20:")
dll.display() 

