from g_tree1 import TreeNode

class TreeNode(TreeNode):

    def print_tree(self,level):

        get_level = self.get_level()
        prefix = ' '*get_level*3+'|___' if self.parent else ""

        if get_level>level:     
            return
    
        print(prefix,self.data)
        for child in self.children:   
            child.print_tree(level)





            
       


        


if __name__=='__main__':

    root = TreeNode('Global')
    # india
    india = TreeNode('India')
    guj = TreeNode('Gujarat')
    guj.add_child(TreeNode('Ahmedabad'))
    guj.add_child(TreeNode('Baroda'))
    ka = TreeNode('Karnataka')
    ka.add_child(TreeNode('bangaluru'))
    ka.add_child(TreeNode('Mysore'))
    india.add_child(guj)
    india.add_child(ka)
    # us
    us = TreeNode('USA')
    new = TreeNode('New Jersey')
    new.add_child(TreeNode('Princeton'))
    new.add_child(TreeNode('Trenton'))
    cali = TreeNode('California')
    cali.add_child(TreeNode('San Francisco'))
    cali.add_child(TreeNode('Mountain View'))
    cali.add_child(TreeNode('Palo Alto'))
    us.add_child(new)
    us.add_child(cali)

    root.add_child(india)
    root.add_child(us)

    



root.print_tree(0)



name = ['babu','kambly','babu','vishnu','kambly']


print(set(['babu','kambly','babu','vishnu','kambly']))