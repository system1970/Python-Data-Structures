class BinaryTree(object):

    def __init__(self,RootValue):
        self.RootValue = RootValue
        self.RightChild = None
        self.LeftChild = None
    
    def insertRight(self,NodeValue):
        if self.RightChild==None:
            self.RightChild = BinaryTree(NodeValue)

        else:
            temp = BinaryTree(NodeValue)
            temp.RightChild = self.RightChild
            self.RightChild = temp

    def insertLeft(self,NodeValue):
        if self.LeftChild==None:
            self.LeftChild = BinaryTree(NodeValue)

        else:
            temp = BinaryTree(NodeValue)
            temp.LeftChild = self.LeftChild
            self.LeftChild = temp

    # def search(self,root,key): 
    #     if root is None or root.RootValue == key: 
    #         return root 
    #     if root.RootValue < key: 
    #         if self.search(root.RightChild,key) != None:
    #             return self.search(root.RightChild,key)
    #         else:
    #             return "value not available"
    #     if self.search(root.LeftChild,key) != None:
    #         return self.search(root.LeftChild,key) 
    #     else:
    #         return "value not available"

    def search(self,root,key): 
        if root is None or root.RootValue == key: 
            return root 
        if root.RootValue < key: 
            return self.search(root.RightChild,key)
        return self.search(root.LeftChild,key) 

    def insert(self,root,NodeValue): 
        if root is None: 
            root = BinaryTree(NodeValue) 
        else: 
            # print(root.RootValue)
            # print(BinaryTree(NodeValue).RootValue)
            # if root.RootValue < BinaryTree(NodeValue).RootValue:
            #     print("blah blah")
            if root.RootValue < BinaryTree(NodeValue).RootValue: 
                if root.RightChild is None: 
                    root.RightChild = BinaryTree(NodeValue)
                else: 
                    self.insert(root.RightChild, NodeValue) 
            else: 
                if root.LeftChild is None: 
                    root.LeftChild  = node 
                else: 
                    self.insert(root.LeftChild ,NodeValue) 

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
def something():
    print("Cause Why Not?")

tree = BinaryTree(3)
tree.insert(tree,23)
tree.insert(tree,2323)
try:
    print(tree.search(tree,223).RootValue)
except AttributeError:
    print("value not available")

print("Preorder: ")
tree.printPreorder(tree) 
print()
print("Postoder: ")
tree.printPostorder(tree) 
print()
print("Inorder: ")
tree.printInorder(tree) 


