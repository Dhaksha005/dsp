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

    def delete_at_beginning(self):
       
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

      
        print(f"Deleted from beginning: {self.head.data}")
        self.head = self.head.next

    def delete_at_end(self):
       
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

       
        if self.head.next is None:
            print(f"Deleted from end: {self.head.data}")
            self.head = None
            return

       
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next

        print(f"Deleted from end: {curr.next.data}")
        curr.next = None  
    def display(self):
       
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elements) if elements else "Empty List")



if __name__ == "__main__":
    llist = SinglyLinkedList()
    llist.append(10)
    llist.append(20)
    llist.append(30)
    llist.append(40)
    
    print("Original List:")
    llist.display()  
    llist.delete_at_beginning()
    llist.display()  

    llist.delete_at_end()
    llist.display()  
