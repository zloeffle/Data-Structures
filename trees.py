class Node:
    def __init__(self, data, children):
        self.data = data
        self.children = children

'''
Binary Tree
- each node has at most 2 children
'''
class BinaryTree:
    def __init__(self, root):
        self.root = root

    def print_tree(self):
        pass

    def insert(self, node):
        pass    

    def delete(self, node):
        pass

    def search(self, node):
        pass

'''
Binary Search Tree
- left child of each node is <= to that nodes value
- right child of each node is >= to that nodes value
'''
class BST:
    def __init__(self, root):
        self.root = root

    def build(self, data):
        pass

    def print_tree(self, nodes):
        pass   
 
    def insert(self, node):
        pass

    def delete(self, node):
        pass

    def search(self, node):
        pass

if __name__ == '__main__':
    print('main')
    test = [5, 6, 3, 2, 4, 8, 7]
    bt = BinaryTree(Node(12))
    

