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
