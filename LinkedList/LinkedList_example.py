class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class LinkedList:

    def __init__(self):
        self.head=None

    def insert_at_beginning(self,val):
        node = Node(val,self.head)
        self.head=node

    def insert_at_end(self,val):
        if self.head is None:
            self.head = Node(val)
        itr = self.head
        while itr.next:
            itr=itr.next
        itr.next = Node(val)

    def show(self):
        if self.head is None:
            print('List is Empty')
            return
        itr = self.head
        list_str = ''
        while itr:
            list_str+=str(itr.val)
            list_str+='-->' if itr.next else ''    
            itr = itr.next

        print(list_str)
        return
    
    def get_length(self):
        length = 0
        itr = self.head
        while itr:
            length+=1
            itr=itr.next
        return length
    
    def insert_at(self,index : int,val : any)->None:
        if index<0 or index>=self.get_length():
            raise Exception('Invalid index value')
        elif index==0:
            self.insert_at_beginning(val)
        count = 0
        itr=self.head
        while itr:
            if count == index-1:
                itr.next = Node(val,itr.next)
                break
            itr=itr.next
            count+=1

    def insert_values(self,*values):
        for val in values:
            self.insert_at_end(val)

    
    def remove_at(self,index):

        if index<0 or index>=self.get_length():
            raise Exception('Invalid index value')    
        elif index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break        
            itr=itr.next
            count+=1

    def remove_value(self,val):
        itr=self.head
        while itr.next:
            if val == itr.next.val:
                itr.next=itr.next.next
                return
            itr=itr.next
        raise Exception('Value error')
    

if __name__=='__main__':
    
    list1 = LinkedList()
    list1.insert_at_beginning(1)
    list1.insert_at_beginning(2)
    list1.insert_at_end(20)
    list1.insert_at_beginning(500)
    list1.insert_at_end(1000)
    list1.insert_at_end(200)
    list1.insert_at(0,30)
    list1.show()
    list1.remove_value(200)
    list1.show()


