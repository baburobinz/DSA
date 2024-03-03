from collections import deque


class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
    def __repr__(self) -> str:
        return f'{self.buffer}'
    

if __name__=='__main__':

    myObj = Queue()

    myObj.enqueue(10)
    myObj.enqueue(20)
    myObj.enqueue(70)
    myObj.enqueue(80)


    print(myObj.is_empty())
    print(myObj.size())
    print(myObj)