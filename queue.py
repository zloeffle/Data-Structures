
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
    
    def print_queue(self):
        for item in queue.items:
            print(item)

if __name__ == '__main__':
    print('Queue')
    queue = Queue()
    queue.push(3)
    queue.push(4)
    queue.push(5)
    queue.push(6)
    queue.pop()
    queue.pop()
    queue.print_queue()
