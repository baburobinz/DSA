import sys

sys.path.append('c:\\Users\\babu5\\OneDrive\\Desktop\\DSA\\Stack')

from stack1 import Stack

def reverese_using_stack(s):

    stack = Stack()

    for ch in s:

        stack.push(ch)


    res = ''

    while stack.size()!=0:
        res+=stack.pop()
    return res





print(reverese_using_stack("We will conquere COVI-19"))
print(reverese_using_stack("I am the king"))

