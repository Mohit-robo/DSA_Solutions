class Queue:
    def __init__(self,capacity):
        
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    '''
    Queue would be full when it is equal to the capacity
    '''
    def isFull(self):
        return self.size == self.capacity

    '''
    When size of queue is 0
    '''
    def isEmpty(self):
        return self.size == 0
    
    '''
    Add items to the queue, item gets added at the end.
    '''
    def EnQueue(self,item):
        if self.isFull():
            print("Cannot add item, Queue Full")
            return
        
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1       # Increment the size of queue
        print('{} Enqueued to the queue:'.format(str(item)))

    '''
    Function to remove item from queue, items are removed from front 
    '''
    def DeQueue(self):
        if self.isEmpty():
            print("Cannot remove item, Queue Empty")
        
        print('{} Dequeued from the queue:'.format(str(self.Q[self.front])))
        self.front = (self.front + 1) % (self.capacity)
        self.size = self.size - 1      # Decrease the size of queue

    '''
    Returns first element of the queue
    '''
    def first_element(self):
        if not self.isEmpty():
            print("First element of the Queue: ",self.Q[self.front])
    
    def last_element(self):
        if not self.isEmpty():
            print("Last element of the Queue: ",self.Q[self.rear])

if __name__ == '__main__':
    
    queue = Queue(3)
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.DeQueue()
    queue.first_element()
    queue.last_element()