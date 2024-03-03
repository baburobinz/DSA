from g_tree1 import TreeNode

class TreeNodeModified(TreeNode):

    def __init__(self,name,designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def print_tree(self,basis):

        if basis == 'name':
           value = self.name
        elif basis=='designation':
           value = self.designation
        elif basis=='both':
            value = f'{self.name} ({self.designation})'
        else:
            print('Invalid Input')

        
        space = ' '*self.get_level()*2
        prefix = space+'|__' if self.parent else ""

        print(prefix,value)
        

        for child in self.children:

            child.print_tree(basis)

def build_management_tree():
    
    root = TreeNodeModified('Nilupul','CEO')

    cto = TreeNodeModified('Chinmay','CTO')

    cloud_mgr = TreeNodeModified('Dhaval','Cloud Manager')
    app_mgr = TreeNodeModified('Abhijith','App Manager')

    infra_head = TreeNodeModified('Vishwa','Infrastructure Head')
    appli_head = TreeNodeModified('Aamir','Application Head')

    infra_head.add_child(cloud_mgr)
    infra_head.add_child(app_mgr)

    cto.add_child(infra_head)
    cto.add_child(appli_head)

    hr_head = TreeNodeModified('Gels','HR Head')
    hr_head.add_child(TreeNodeModified('Peter','Recruitment Manager'))
    hr_head.add_child(TreeNodeModified('Waqas','Policy Manager'))

    root.add_child(cto)
    root.add_child(hr_head)
    return root



if __name__=='__main__':
    root = build_management_tree()
    # root.print_tree('name')
    # root.print_tree('designation')
    root.print_tree('both')


