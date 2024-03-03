import sys

sys.path.append('c:\\Users\\babu5\\OneDrive\\Desktop\\DSA\\Stack')

from stack1 import Stack

def is_matching(ch1,ch2):

    map_dict = {
        '}':'{',
        ')':'(',
        ']':'['
    }

    return map_dict[ch1]==ch2


def is_balanced(s):

    stack = Stack()

    for ch in s:

        if ch=='{' or ch=='(' or ch=='[':

            stack.push(ch)

        if ch=='}' or ch==')' or ch==']':

            if stack.size()==0:
                return False
            
            if not is_matching(ch,stack.pop()):
                return False
            

    return stack.size()==0

        




print(is_balanced("(())"))