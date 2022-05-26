class StackNode:

    # Constructor to initialize the node

    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:

    # Constructor to initialize the root
    def __init__(self):
        self.root = None
    
    def push(self,item):

        new_node = StackNode(item)
        new_node.next = self.root
        self.root = new_node
        print("%d pushed to stack" % (item))

    def pop(self):
        
        if self.is_empty():
            return float("inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped
    
    def is_empty(self):
        return True if self.root is None else False

    def peek(self):
        if not self.is_empty():
            return self.root.data
        else:
            return float("inf")


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
 
print ("%d popped from stack" % (stack.pop()))
print ("Top element is % d " % (stack.peek()))