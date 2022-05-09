
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):

        temp = self.head
        while (temp):
            print (" %d" %(temp.data)),
            temp = temp.next
    
    def atthefront(self,new_data):
        
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self,prev_node,new_data):

        if prev_node is None:
            print("Previous node not present")
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def attheend(self,new_data):

        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node
    
    def delete_node(self,key):
        
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while (temp is not None):
            
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if(temp == None):
            return
 
        # Unlink the node from linked list
        prev.next = temp.next

        temp = None

if __name__ == '__main__':

    llist = LinkedList()
    
    llist.atthefront(7)
    llist.atthefront(1)
    llist.atthefront(3)
    llist.atthefront(2)

    print ("Created Linked List: ")
    llist.printList()
    llist.delete_node(3)
    print ("\nLinked List after Deletion of 1:")
    llist.printList()