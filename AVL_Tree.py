class AVL(object):
    def __init__(self,RootValue):
        self.RootValue = RootValue
        self.RightChild = None
        self.LeftChild = None
        self.Height = 1
        
    def insert(self, root, NodeValue): 
        if not root: 
            return AVL(NodeValue) 
        elif NodeValue < root.RootValue: 
            root.LeftChild = self.insert(root.LeftChild, NodeValue) 
        else: 
            root.RightChild = self.insert(root.RightChild, NodeValue) 
        
        root.Height = 1 + max(self.getHeight(root.LeftChild), 
                           self.getHeight(root.RightChild)) 
        
        balance = self.getBalance(root) 

        if balance > 1 and NodeValue < root.LeftChild: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and NodeValue > root.RightChild: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and NodeValue > root.LeftChild: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and NodeValue < root.RightChild: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 

    def leftRotate(self,z):

        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def rightRotate(self,z):
  
        y = z.LeftChild
        T3 = y.RightChild
  
        # Perform rotation 
        y.RightChild= z 
        z.LeftChild= T3 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.LeftChild), 
                        self.getHeight(z.RightCild)) 
        y.height = 1 + max(self.getHeight(y.LeftChild), 
                        self.getHeight(y.RightChild)) 
  
        # Return the new root 
        return y 

    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.Height 

    def getBalance(self,root):
        if not root:
            return 0
        
        return self.getHeight(root.LeftChild)-self.getHeight(root.RightChild)
    
    def GetRootValue(self):
        return self.RootValue
    def GetRightChild(self):
        return self.RightChild
    def GetLeftChild(self):
        return self.LeftChild

    def printPreorder(self,root): 
        if root: 
            print(root.GetRootValue(),end=' ')
            self.printPreorder(root.GetLeftChild()) 
            self.printPreorder(root.GetRightChild()) 

    def printPostorder(self,root): 
        if root: 
            self.printPostorder(root.GetLeftChild()) 
            self.printPostorder(root.GetRightChild()) 
            print(root.GetRootValue(),end=' ')
    def printInorder(self,root): 
        if root: 
            self.printInorder(root.GetLeftChild()) 
            print(root.GetRootValue(),end=' ')
            self.printInorder(root.GetRightChild(),) 

tree = AVL(15) 
tree.insert(tree,20)
tree.insert(tree,10)
tree.insert(tree,12)
tree.insert(tree,30)

print("Preorder: ")
tree.printPreorder(tree) 
print()
print("Postoder: ")
tree.printPostorder(tree) 
print()
print("Inorder: ")
tree.printInorder(tree) 




