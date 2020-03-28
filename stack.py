
'''
Stack LIFO
- Uses: expression eval, syntax parsing, correct path in maze
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

    def print_stack(self):
        for item in self.items:
            print(item)

if __name__ == '__main__':
    print('Stack')
    stack = Stack()
    stack.push(5)
    stack.push(3)
    stack.push(7)
    stack.push(2)
    stack.pop()
    stack.pop()
    stack.print_stack()    