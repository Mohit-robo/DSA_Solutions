
class Stack():
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


def reverse_string(stack:list,string:str):

    # Loop through the string and push the contents 
    # character by character onto the stack

    for i in string:
        stack.push(i)
    
    rev_str = ''
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str

s = Stack()
input_str = "Mohit"

print(reverse_string(s,input_str))
