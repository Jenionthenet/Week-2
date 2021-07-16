#stacks = []




class Stack:
    def __init__(self):
        self.items = []

   
    def push(self, item):
        if item is not None:
            self.items.append(item)
    

    def pop(self):
        if len(self.items) > 0:
            item = self.items[ -1]
            del self.items [-1]
            return item
        else:
            return None # custom error can be thrown
        
        

stack = Stack()
stack.push(13)
stack.push(None)
stack.push(33)
stack.push(50)

print(stack.items)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())   

