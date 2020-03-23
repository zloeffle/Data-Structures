
'''
Stack LIFO
- Uses: rexpression eval, correct path in maze
'''
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, val):
        self.items.append(val)

    def pop(self):
        n = len(self.items)
        return self.items.pop(n-1)

    def size(self):
        return len(self.items)