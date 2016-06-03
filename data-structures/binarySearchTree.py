class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.leftChild = None
        self.rightChild = None

class binarySearchTree:
    def __init__(self):
        self.root = None

    #returns true if node with given key is found
    def search(self, key):
        return self.b_search(key, self.root)
    
    def b_search(self, key, root):
        if(root == None):
            return False
        
        if(root.key == key):
            return True
        elif(root.key > key):
            return self.b_search(key, root.leftChild)
        else:
            return self.b_search(key, root.rightChild)
        
    
    def insert(self, key, root=None):
        if(root == None):
            root = self.root        

        #empty tree
        if(self.root == None):
            self.root = Node(key)

        else:
            #go right
            if(root.key < key):
                if(root.rightChild == None):
                    root.rightChild = Node(key)
                else:
                    self.insert(key, root.rightChild)
            #go left
            elif(root.key > key):
                if(root.leftChild == None):
                    root.leftChild = Node(key)
                else:
                    self.insert(key, root.leftChild)

    def delete(self, key):
        self.b_delete(key, self.root)

    def b_delete(self, key, root=None):
        #empty
        if(root == None):
            return root

        #go left or right
        if(root.key > key):
            root.leftChild = self.b_delete(key, root.leftChild)           
        elif(root.key < key):
            root.rightChild = self.b_delete(key, root.rightChild)

        #we found node
        else:

            #node to delete has 0 or 1 children
            if(root.leftChild == None):
                temp = root.rightChild
                root = None
                return temp
            elif(root.rightChild == None):
                temp = root.leftChild
                root = None
                return temp

            #node has 2 children
            #find inorder successor
            temp = self.findMin(root.rightChild)

            root.key = temp.key

            root.rightChild = self.b_delete(temp.key, root.rightChild)
            
            
        return root

    def findMin(self, root):
        cur = root

        while(cur.leftChild != None):
            cur = cur.leftChild

        return cur
    
    #display tree through in-order traversal
    def display(self, root=None):
        if(root == None):
            root = self.root

        #empty tree
        if(self.root == None):
            return
        
        else:
            
            if(root.leftChild != None):
                self.display(root.leftChild)

            print(root.key)
            
            if(root.rightChild != None):
                self.display(root.rightChild)


