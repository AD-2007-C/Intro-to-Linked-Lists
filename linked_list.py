class List_Node:
    def __init__ (self,val=0,next=None):
        self.val=val
        self.next=next

def print_list(head):
    current=head
    while current:
        print(current.val, end=" => " if current.next else "\n")
        current=current.next

node1=List_Node(1)
node2=List_Node(2)
node3=List_Node(3)

node1.next=node2
node2.next=node3

def insert_at_beginning(head,val):
    new_node=List_Node(val)
    new_node.next=head
    return new_node
head=insert_at_beginning(node1,0)
#print_list(head)

def insert_at_end(head, val):
    new_node = List_Node(val)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head
head=insert_at_end(head,4)
#print_list(head)

def delete_node(head,val):
    if head is None:
        return None
    if head.val==val:
        return head.next
    current=head
    while current.next and current.next.val!=val:
        current = current.next
    if current.next:
        current.next=current.next.next
    return head

head=delete_node(head,4)
#print_list(head)



    