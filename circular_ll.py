class Node:
    def __init__ (self,data):
        self.data=data
        self.next= None
class CircularLinkedList:
    def __init__ (self):
        self.head=None

    def print_list(self):
        temp=self.head
        while True:
            print(temp.data, end=" => " if temp.next else "\n")
            temp=temp.next
            if temp==self.head:
               break
    def insert_at_beginning(self,data):
        new_node= Node(data)
        if self.head is None:
            new_node.next=new_node
            self.head=new_node
       
        current= self.head
        while current.next!=self.head:
             current=current.next
             
        current.next=new_node
        new_node.next=self.head
        self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.next=new_node
            new_node=self.head

        else:
            current=self.head
            while current.next!=self.head:
                current=current.next

            new_node.next=self.head
            current.next=new_node
    def delete_node(self):
        if self.head is None:
            return
        if self.head.next is self.head:
            self.head=None
            return
        current=self.head
        while current.next.next!=self.head:
            current=current.next
        current.next=self.head
        
        

cll= CircularLinkedList()
cll.insert_at_beginning(50)
cll.insert_at_beginning(30)
cll.insert_at_beginning(10)
cll.insert_at_end(75)
cll.delete_node()
cll.print_list()


        
