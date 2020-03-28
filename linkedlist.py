'''
Linked List
- Uses: constant time is needed for insert/delete, data grows dynamically, no random access, insert at any position
'''
class LinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = self.Node(data)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode


    def delete(self, key):
        pass

    def print_list(self):
        if self.head.next is None:
            print(self.head.data)
        else:
            curr = self.head
            while curr.next:
                print(curr.data)
                curr = curr.next

'''
Double Linked List
- Uses: Easy deletion, reverse iteration
'''
class DoubleLinkedList:
    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = self.Node(data)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode


    def delete(self, key):
        pass

    def print_list(self):
        if self.head.next is None:
            print(self.head.data)
        else:
            curr = self.head
            while curr.next:
                print(curr.data)
                curr = curr.next

'''
Circular Linked List
- Uses: deck of cards, browser cache, most recently used list, undo functionality
- any node can be starting point
'''
class CircularLinkedList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data

    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = self.Node(data)
        if self.head is None:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode


    def delete(self, key):
        pass

    def print_list(self):
        pass

if __name__ == '__main__':
    data = [1,3,7,4,9]

    print('Single Linked List')
    llist = LinkedList()
    for val in data:
        llist.insert(val)
    llist.print_list()
    

    print('Double Linked List')
    dllist = DoubleLinkedList()
    
    
    print('Circular Linked List')