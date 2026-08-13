class Node:
   
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    
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

    def delete_at_position(self, position):
        
       
        if self.head is None:
            print("Error: List is empty.")
            return

       
        if position == 0:
            self.head = self.head.next
            return

       
        current = self.head
        prev = None
        current_index = 0

       
        while current is not None and current_index < position:
            prev = current
            current = current.next
            current_index += 1

       
        if current is None:
            print(f"Error: Position {position} is out of bounds.")
            return

        # Unlink the node from the linked list
        prev.next = current.next

    def display(self):
       
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")


llist = SinglyLinkedList()
llist.append(10)
llist.append(20)
llist.append(30)
llist.append(40)

print("Original List:")
llist.display() 

print("\nDeleting node at position 2 (value 30):")
llist.delete_at_position(2)
llist.display()  
print("\nDeleting node at position 0 (head node, value 10):")
llist.delete_at_position(0)
llist.display()  

