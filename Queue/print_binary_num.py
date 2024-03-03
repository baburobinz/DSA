from eg1 import Queue

class QueueModified(Queue):
    def front(self):
        return self.buffer[-1]

def gen_binary_numbers(n):
    queue = QueueModified()

    queue.enqueue('1')
    for i in range(n):
        front = queue.front()
        print(front)
        queue.enqueue(front+'0')
        queue.enqueue(front+'1')
        queue.dequeue()


# gen_binary_numbers(10)
        


# def binary_gen(n):

#     l=['1']


#     for i in range(n//2):

#         l.append(l[i]+'0')
#         l.append(l[i]+'1')


#     return l[:n]



    


# print(binary_gen(32))
# print(len(binary_gen(32)))
        






