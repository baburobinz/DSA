class BinarySearchTreeNode:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,val):

        if val==self.data:
            return 
        elif val<self.data:
            if self.left:
                self.left.add_child(val)
            else:
                self.left=BinarySearchTreeNode(val)
        elif val>self.data:
            if self.right:
                self.right.add_child(val)
            else:
                self.right=BinarySearchTreeNode(val)

    def inorder_traversal(self):

        elements = []
        if self.left:
            elements+=self.left.inorder_traversal()
        elements.append(self.data)
        if self.right:
            elements+=self.right.inorder_traversal()
        return elements
    
    def pre_order_traversal(self):

        elements = []

        elements.append(self.data)

        if self.left:

            elements+=self.left.pre_order_traversal()

        if self.right:
            elements+=self.right.pre_order_traversal()

        return elements
    

    def post_order_traversal(self):

        elements = []
        if self.left:
            elements+=self.left.post_order_traversal()
        if self.right:
            elements+=self.right.post_order_traversal()
        elements.append(self.data)
        return elements
    

    def search(self,val):

        if val==self.data:
            return True
        
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False


def create_binary_tree(val_list):
    root = BinarySearchTreeNode(val_list[0])

    for i in range(1,len(val_list)):

        root.add_child(val_list[i])

    return root


if __name__=='__main__':

    tree = create_binary_tree([50,25,30,42,10,25])

    print(tree.inorder_traversal())

    print(tree.search(12))
   