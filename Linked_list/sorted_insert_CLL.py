class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.head = None


    def push(self,new_data):
        
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printCircular(self):
        
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data,end= ' ')
                temp = temp.next
                if temp == self.head:
                    break
    
    def sortedInsert(self,new_node):
        
        current = self.head

        # Case 1. The given list is empty
        if current is None:
            
            new_node.next =  new_node
            self.head = new_node

        elif (current.data >= new_node.data):
            
            while current.next != self.head:
                current = current.next
            
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

        else:
            while (current.next != self.head and \
                        current.next.data < new_node.data):
                current = current.next
            
            new_node.next = current.next
            current.next = new_node

if __name__ == '__main__':

    arr = [12, 56, 2, 11, 1, 90]
    
    list_size = len(arr)
    
    # start with empty linked list
    start = CircularLinkedList()
    
    # Create linked list from the array arr[]
    # Created linked list will be 1->2->11->12->56->90
    for i in range(list_size):
        temp = Node(arr[i])
        start.sortedInsert(temp)
    
    start.printCircular()



