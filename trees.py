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
    
    def get_parent(self, key):
        parent = None
        for node in self.tree:
            if node.left:
                if node.left.data == key:
                    parent = node
            if node.right:
                if node.right.data == key:
                    parent = node
        return parent
                
            
    
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
        target = None
        
        # remove deepest node in the tree
        deepest = tree.pop()
        parent = self.get_parent(deepest.data)
        parent = tree[tree.index(parent)]
        if parent.left == deepest:
            parent.left = None
        if parent.right == deepest:
            parent.right = None
        
        # search the tree for the node to be deleted
        for node in tree:
            if node.data == key:
                target = node
                
        if target:
            parent = self.get_parent(target.data) # parent of target node
            parentIndx = tree.index(parent)
            left = target.left # left child of target
            right = target.right # right child of target
            targetIndx = tree.index(target) # index of target node
            
            tree[targetIndx] = deepest # replace target node with deepest node
            target = tree[targetIndx]
            parent = tree[parentIndx]
            
            # update children of parent of deleted node
            if parent.left:
                if parent.left.data == key:
                    parent.left = target
            if parent.right:
                if parent.right.data == key:
                    parent.right = target
            
            # update children of deleted node
            target.left = left
            target.right = right
            
            self.tree = tree
        else:       
            print('Node not found')
        
        
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
        self.tree = []
    
    def get_children(self, node):
        children = []
        children.append(node.left)
        children.append(node.right)
        return children
    
    def get_parent(self, key):
        parent = None
        for node in self.tree:
            if node.left:
                if node.left.data == key:
                    parent = node
            if node.right:
                if node.right.data == key:
                    parent = node
        return parent
                
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
        data.sort()
        n = len(data)
        mid = n // 2
        self.root = Node(data.pop(mid))   
        curr = self.root
        
        left = data[0:mid]
        print(left)
        while len(left) > 1:
            mid = len(left) // 2
            newNode = Node(left.pop(mid))
            if newNode.data < curr.data:    
                
        
        
    def search(self, key):
        pass
    
    def insert(self, data):
        newNode = Node(data)
        tree = self.tree
                
    def delete(self, key):
        pass
        
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

if __name__ == '__main__':
    print('BINARY TREE')
    data = [5, 6, 3, 2, 4, 8, 7]
    print(data)
    bt = BinaryTree()
    
    # build test
    print('\nBuild Test')
    bt.build(data)
    bt.print_tree()
    
    # get_parent test
    print('\nGet Parent Test')
    print(bt.get_parent(6).data)
    
    # search test
    print('\nSearch Test')
    print(bt.search(6))

    # insert test
    print('\nInsert Test')
    bt.insert(12)
    bt.print_tree()

    # delete test
    print('\nDelete Test')
    bt.print_tree()
    bt.delete(6)
    print()
    bt.print_tree()
    
    print('\nBINARY SEARCH TREE')
    data = [5, 6, 3, 2, 4, 8, 7, 9, 10]
    bst = BST()
    data.sort()
    print(data)
    
    # build test
    print('\nBuild Test')
    bst.build(data)
   
    # search test
    print('\nSearch Test')
    

    # insert test
    print('\nInsert Test')
    

    # delete test
    print('\nDelete Test')
    
