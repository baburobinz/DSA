from binary_tree import BinarySearchTreeNode

class BinarySearchTreeNodeExtended(BinarySearchTreeNode):

    def add_child(self,val):

        if val==self.data:
            return 
        elif val<self.data:
            if self.left:
                self.left.add_child(val)
            else:
                self.left=BinarySearchTreeNodeExtended(val)
        elif val>self.data:
            if self.right:
                self.right.add_child(val)
            else:
                self.right=BinarySearchTreeNodeExtended(val)

    def find_min(self):

        if self.left is None:
            return self.data
        
        return self.left.find_min()
    
    def find_max(self):

        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0

        return self.data+left_sum+right_sum


def create_binary_tree(elements):

    root = BinarySearchTreeNodeExtended(elements[0])

    for i in range(1,len(elements)):

        root.add_child(elements[i])

    return root






if __name__=='__main__':

    elements = [90,36,17,3,50,26,94]

    tree = create_binary_tree(elements)

    print(tree.find_min())
    print(tree.find_max())
 
    print(tree.calculate_sum())
