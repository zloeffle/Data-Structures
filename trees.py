class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

'''
Binary Tree
- each node has at most 2 children
'''
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def build(self, data):
        for val in data:
            self.insert(val)
        
    def print_tree(self, node=None):
        curr = self.root
        if node:
            curr = node
        
        if not self.hasChildren(curr):
            return None
        print(curr.data, [curr.left.data, curr.right.data])
        
        if self.hasChildren(curr.left):
            self.print_tree(curr.left)
        if self.hasChildren(curr.right):
            self.print_tree(curr.right)
            
            
            
    def get_children(self, node):
        children = []
        children.append(node.left)
        children.append(node.right)
        return children
    
    def hasChildren(self, node):
        if node:
            if node.left or node.right:
                return True
        return False
    
    def isFull(self, node):
        if node:
            if node.left and node.right:
                return True
        return False
    
    def insert(self, data):
        newNode = Node(data) # new node
        if self.root is None:
            self.root = newNode
            return self.root
        
        curr = self.root
        while curr.left and curr.right:
            left = curr.left
            right = curr.right
            
            if not self.isFull(left):
                curr = left
            elif not self.isFull(right):
                curr = right
            else:
                curr = left.left
        
        if not curr.left:
            curr.left = newNode
            return curr.left
        if not curr.right:
            curr.right = newNode
            return curr.right

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
    def __init__(self):
        self.root = None
        
    def build(self, data):
        for val in data:
            self.insert(val)

    def print_tree(self, node=None):
        curr = self.root
        if node:
            curr = node
        
        if not self.hasChildren(curr):
            print(curr.data)
            return None
        print(curr.data, [curr.left.data, curr.right.data])
        
        if self.hasChildren(curr.left):
            self.print_tree(curr.left)
        if self.hasChildren(curr.right):
            self.print_tree(curr.right)   
    
    def get_children(self, node):
        children = []
        children.append(node.left)
        children.append(node.right)
        return children
    
    def hasChildren(self, node):
        if node:
            if node.left or node.right:
                return True
        return False
    
    def isFull(self, node):
        if node:
            if node.left and node.right:
                return True
        return False
    
    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            return self.root
        
        curr = self.root
        while 1:
            if newNode.data < curr.data:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = newNode
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = newNode
                    break
                

    def delete(self, node):
        pass

    def search(self, node):
        pass

if __name__ == '__main__':
    print('Binary Tree')
    data = [5, 6, 3, 2, 4, 8, 7]
    bt = BinaryTree()
    bt.print_tree()

    print('Binary Search Tree')
    bst = BST()
    bst.build(data)
    
    

