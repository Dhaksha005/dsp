class Node:
   
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
  
    def __init__(self):
        self.head = None

    def insert_at_position(self, data, position):
       
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

       
        current = self.head
        count = 0

        
        while current is not None and count < position - 1:
            current = current.next
            count += 1

       
        if current is None:
            print(f"Position {position} is out of bounds.")
            return

        
        new_node.next = current.next
        current.next = new_node

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty List")



if __name__ == "__main__":
    llist = SinglyLinkedList()
    
  
    llist.insert_at_position(10, 0)
    llist.insert_at_position(20, 1)
    llist.insert_at_position(30, 2)
    print("Initial List:")
    llist.display() 

   
    llist.insert_at_position(15, 1)
    print("\nAfter inserting 15 at position 1:")
    llist.display()  
    llist.insert_at_position(5, 0)
    print("\nAfter inserting 5 at position 0:")
    llist.display() 