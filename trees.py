class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

'''
Binary Tree
- each node has at most 2 children
- uses: find name in phone book, sorted tree traversal, next closest elem, find all elems less or greater than a key

'''
class BinaryTree:
    def __init__(self):
        self.root = None
        self.tree = None
            
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
    
    def build(self, data):
        root = Node(data.pop(0))
        self.root = root
        
        n = len(data)-1
        curr = self.root
        index = 0
        x,y = 0,1
        tree = [curr]
        while index <= n:            
            # left child
            if index + x <= n:
                curr.left = Node(data[index + x])
            else:
                curr.left = None
            # right child
            if index + y <= n:
                curr.right = Node(data[index + y])
            else:
                curr.right = None
                    
            # update curr node
            curr = Node(data[index])
            tree.append(curr)
            
            index += 1
            x += 1
            y += 1
    
        self.tree = tree
        return tree
    
    def search(self, key):
        tree = self.tree
        for node in tree:
            if node.data == key:
                return node
            if node.left:
                if node.left.data == key:
                    return node.left
            if node.right:
                if node.right.data == key:
                    return node.right
        return None
            
        
    
    def insert(self, data):
        newNode = Node(data)
        tree = self.tree
        
        for node in tree:
            if self.isFull(node):
                continue
            else:
                if not node.left:
                    node.left = newNode
                    break
                if not node.right:
                    node.right = newNode
                    break
        tree.append(newNode)
        self.tree = tree
                

    def delete(self, key):
        tree = self.tree
        target = self.search(key)
        deepest = tree.pop()
        if target:
            for node in tree:
                if node == target:
                    node.data = deepest.data
                    break
            self.tree = tree
        else:
            print('node not found')
        
        
    def print_tree(self):
        tree = self.tree
        
        for node in tree:
            left = node.left
            right = node.right
            
            if left:
                left = left.data
            else:
                left = None
            if right:
                right = right.data
            else:
                right = None
            
            print(node.data, [left,right])
        
        

'''
Binary Search Tree
- left child of each node is <= to that nodes value
- right child of each node is >= to that nodes value
- uses: data needs to be sorted, search for a range of values
'''
class BST:
    def __init__(self):
        self.root = None  
    
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
    
    def build(self, data):
        pass
    
    def insert(self, data):
        pass
                
    def delete(self, node):
        pass

    def search(self, node):
        pass
    
    def print_tree(self, node=None):
        pass

if __name__ == '__main__':
    print('Binary Tree')
    data = [5, 6, 3, 2, 4, 8, 7]
    bt = BinaryTree()
    bt.build(data)
    bt.print_tree()
    bt.insert(12)
    print()
    bt.print_tree()
    
    print()
    bt.delete(6)
    bt.print_tree()
    
    print('Binary Search Tree')
    

