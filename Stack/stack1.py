from collections import deque


class Stack:

    def __init__(self):

        self.container = deque()

    def push(self,val):

        return self.container.append(val)

    def peek(self):

        return self.container[-1]
    
    def pop(self):

        return self.container.pop()
    
    def is_empty(self):

        return len(self.container)==0
    
    def size(self):

        return len(self.container)
    
    def __repr__(self):
        return f'{self.container}'
    

if __name__ == '__main__':

    obj = Stack()

    obj.push(10)
    obj.push(20)
    res=obj.size()

    print(res)

    print(obj)