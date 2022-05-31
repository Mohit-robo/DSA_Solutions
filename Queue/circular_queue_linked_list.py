class Node:
    def __init__(self):
        self.data = None
        self.link = None
  
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Function to create Circular queue 
    def enQueue(self, value):
        temp = Node() 
        temp.data = value 
        if (self.front == None): 
            self.front = temp 
        else:
            self.rear.link = temp 
    
        self.rear = temp 
        self.rear.link = self.front
    
    # Function to delete element from Circular Queue 
    def deQueue(self):
        if (self.front == None):
            print("Queue is empty") 
            return -999999999999
    
        # If this is the last node to be deleted 
        value = None # Value to be dequeued 
        if (self.front == self.rear):
            value = self.front.data
            self.front = None
            self.rear = None
        else: # There are more than one nodes 
            temp = self.front 
            value = temp.data 
            self.front = self.front.link 
            self.rear.link = self.front
    
        return value 
    
    # Function displaying the elements 
    # of Circular Queue 
    def displayQueue(self):
        temp = self.front 
        print("Elements in Circular Queue are: ", 
                                    end = " ") 
        while (temp.link != self.front):
            print(temp.data, end = " ") 
            temp = temp.link
        print(temp.data)

if __name__ == '__main__':
  
    # Create a queue and initialize
    # front and rear 
    q = Queue() 
  
    # Inserting elements in Circular Queue 
    q.enQueue(14) 
    q.enQueue(22) 
    q.enQueue(6) 
  
    # Display elements present in 
    # Circular Queue 
    q.displayQueue() 
  
    # Deleting elements from Circular Queue 
    print("Deleted value = ", q.deQueue()) 
    print("Deleted value = ", q.deQueue()) 
  
    # Remaining elements in Circular Queue 
    q.displayQueue() 
  
    q.enQueue(9) 
    q.enQueue(20) 
    q.displayQueue()