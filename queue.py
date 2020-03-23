
'''
Queue FIFO
- Uses: when order is needed, add/removing both ends
'''

class Queue:
    def __init__(self):
        self.items = []
    
    def push(self, val):
        self.items.append(val)

    def pop(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)