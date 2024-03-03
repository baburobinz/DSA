class BinaryTree:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,val):

        if val==self.data:
            return
        if val<self.data:
            if self.left:
                self.left.add_child(val)
            else:
                self.left=BinaryTree(val)

        if val>self.data:
            if self.right:
                self.right.add_child(val)
            else:
                self.right=BinaryTree(val)


    def inorder_traversal(self):

        elements=[]
        if self.left:
            elements+=self.left.inorder_traversal()

        elements.append(self.data)
        
        if self.right:
            elements+=self.right.inorder_traversal()
        return elements
    

    def preorder_traversal(self):

        elements=[]

        elements.append(self.data)

        if self.left:
            elements+=self.left.preorder_traversal()

        if self.right:
            elements+=self.right.preorder_traversal()

        return elements
    
    def postorder_traversal(self):

        elements=[]

        if self.left:
            elements+=self.left.postorder_traversal()

        if self.right:
            elements+=self.right.postorder_traversal()

        elements.append(self.data)

        return elements
    

    def find_min(self):

        if self.left is None:

            return self.data
        
        return self.left.find_min()
    
    def find_max(self):

        if self.right is None:
            return self.data
        return self.right.find_max()
    

    def calculate_sum(self):

        left_sum = self.left.calculate_sum()if self.left else 0
        right_sum = self.right.calculate_sum()if self.right else 0
        return self.data+left_sum+right_sum

    def is_exist(self,val):

        if val == self.data:
            return True
        
        if val<self.data:
            if self.left:
                return self.left.is_exist(val)
            else:
                return False
        
        if val>self.data:
            if self.right:
                return self.right.is_exist(val)
            else:
                return False
            
    
    def delete_item(self,val): 
       
        if val<self.data:
            if self.left:
                self.left = self.left.delete_item(val)

        elif val>self.data:
            if self.right:
                self.right = self.right.delete_item(val)

        else:

            if self.left is None and self.right is None:
                return None
            
            if self.right is None:
                return self.left
            
            if self.left is None:
                return self.right
            


            # if the node has two children method-1
            # min_val = self.right.find_min()

            # self.data = min_val

            # self.right=self.right.delete_item(min_val)


            # method-2 find max of left sub tree

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete_item(max_val)

        return self
            

def build_tree(elements):

    root = BinaryTree(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root






elements = [50,30,20,40,80,90,15,35]

tree = build_tree(elements)
# print(tree.inorder_traversal())

tree.delete_item(30)
print('second : ',tree.inorder_traversal())



res = ['babu']+['vinu']

print(res)
