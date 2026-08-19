def insert_last(self,data):
    new_node  = Node (data)

    if self.head is None:
        self.head = new_node
        return 

    curr = self.head 
    while curr.next is not None:
        curr = curr.next

    curr.next = new_node 