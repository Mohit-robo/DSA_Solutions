
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.head = None
    
    def Addcircluar(self,data):
        
        ptr1 = Node(data)
        temp = self.head

        ptr1.next = self.head

        # If linked list is not None then set the next of
        # last node
        
        if self.head is not None:
            while (temp.next != self.head):
                temp = temp.next
            temp.next = ptr1

        else:
            ptr1.next = ptr1

        self.head = ptr1

    def printCircular(self):
        
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data,end= ' ')
                temp = temp.next
                if (temp == self.head):
                    break

if __name__ == '__main__':

    cllist = CircularLinkedList()
    cllist.Addcircluar(12)
    cllist.Addcircluar(25)
    cllist.Addcircluar(23)
    cllist.Addcircluar(52)

    print("Contents of circular list:")
    cllist.printCircular()