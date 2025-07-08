class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.head = None



    def insert_at_beginning(self,val):
        new_node= Node(val)
        new_node.next=self.head
        if self.head:
           self.head.prev= new_node
        self.head= new_node

    def print_list(self):
       temp = self.head
       while temp:
          print(temp.data, end=" <-> " if temp.next else "\n")
          temp = temp.next
    print("None")

    def insert_at_end(self,val):
        new_node= Node(val)
        if not self.head:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp

    def delete_at_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head=None
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.prev.next=None


dll = DoublyLinkedList()      # Create a new empty DLL
dll.insert_at_beginning(10)  # Insert 10
dll.insert_at_beginning(20)  # Insert 20 (before 10)
dll.insert_at_beginning(30)
dll.insert_at_end(45)
dll.delete_at_end()

dll.print_list()


