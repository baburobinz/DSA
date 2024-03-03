class TreeNode:

    def __init__(self,data):

        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_children(self):
        for child in self.children:
            print(child.data)

    def get_level(self):
        parent = self.parent
        level=0
        while parent:
            parent=parent.parent
            level+=1
        return level
    
    def print_tree(self):
        space = ' '*self.get_level()*3
        prefix=space+'|__' if self.parent else ""
        print(prefix,self.data)
        if len(self.children)==0:
            return
        for child in self.children:
            child.print_tree()
       

if __name__=='__main__':

    Electronics = TreeNode('Electronics')

    TV = TreeNode('TV')
    Mobile = TreeNode('Mobile')
    Laptop = TreeNode('Laptop')

    # childs Electronics
    Electronics.add_child(TV)
    Electronics.add_child(Mobile)
    Electronics.add_child(Laptop)

    # Tv childs
    TV.add_child(TreeNode('LG'))
    TV.add_child(TreeNode('Onida'))
    TV.add_child(TreeNode('Amstrad'))

    # Mobile childs
    Mobile.add_child(TreeNode('Samsung'))
    Mobile.add_child(TreeNode('Apple'))
    Mobile.add_child(TreeNode('Xiomi'))

    Electronics.print_tree()