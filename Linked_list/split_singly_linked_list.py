
class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:

    def __init__(self) -> None:
        self.head = None

    def prepend(self,data):
        
        # 1. Setup a new node
        # 2. set up a current node pointer
        # 3. As we are prepending the nodes our new node's/
        #    next would be initial head node
            
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        # if there are no elements in the List 
        if not self.head:
            new_node.next = new_node
        
        # Traverse through the List untill the last nodes next is /
        # equal to head node

        else:
            while cur.next != self.head:
                cur = cur.next
            
            # Prepending a new node
            cur.next = new_node

        # The Make the new node as head
        self.head = new_node

    def append(self,data):
        
        ## If the list is empty create a node:
        # 1. Assign it a head 
        # 2. make the Head nodes next as head /
        #    this means that we have linked back the next to the head

        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            # 1. create a new node
            # 2. assign a head node 
            new_node = Node(data)
            cur  = self.head
            # 3. Keep on traversing through the list untill /
            # next is equal to head 
            while (cur.next != self.head):
                cur = cur.next
            # 4. if there is another node addes then the last node /
            # rather than pointing to the head back points to the next node

            cur.next = new_node
            new_node.next = self.head

    def print_list(self):
        
        cur = self.head
        while cur:
            # iterate the loop untill the current node is /
            # head node 

            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break
    
    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def split_list(self):
        
        size = len(self)

        # If no element in the list
        if size == 0:
            return None
        
        # If 1 element in the list
        if size == 1:
            return self.head
        
        # If normal list
        mid = size // 2
        count = 0

        prev = None
        cur = self.head

        while cur and count < mid:
            
            # 1. Increment the count
            # 2. Make current node as previous
            # 3. Move to next 
            count += 1  
            prev = cur      
            cur = cur.next 
        
        # print(prev.data)
        # print(cur.data)

        # Preparing the first list by making next of the left
        # of the mid as head 
        prev.next = self.head
        
        # Preparing the second list
        # 1. create an instance of the Object
        # 2. Traverse utill last node's next is not equal to head
        # 3, Append data to new list and move fowrwar in the list

        split_llist = CircularLinkedList()

        while cur.next != self.head:
            split_llist.append(cur.data)
            cur = cur.next
        split_llist.append(cur.data)

        self.print_list()
        print('\n')
        split_llist.print_list()

if __name__ == '__main__':
    
    cllist = CircularLinkedList()
    cllist.append('A')
    cllist.append('B')
    cllist.append('C')
    cllist.append('D')
    cllist.append('E')

    cllist.split_list()

    