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

def int_2_binary(number):
    
    if number == 0:
        return 0

    s = Stack()

    while number > 0:
        
        remainder_ = number % 2
        s.push(remainder_)
        number = number // 2

    bin_num = ''
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

print(int_2_binary(665))