class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        newnode = Node(data)

        if self.head is None:
            self.head = newnode
            newnode.next = self.head
        else:
            current = self.head

            while current.next != self.head:
                current = current.next

            newnode.next = self.head
            current.next = newnode
            self.head = newnode

    def display(self):
        if self.head is None:
            return

        current = self.head

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(back to head)")



list = CircularLinkedList()

list.insert_beginning(30)
list.insert_beginning(20)
list.insert_beginning(10)

list.display()