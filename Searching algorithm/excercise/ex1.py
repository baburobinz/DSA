import sys
sys.path.append('c:\\Users\\babu5\\OneDrive\\Desktop\\DSA\\Searching algorithm')
from Binary_Search.example1 import binary_search

def number_of_occurence(lst,num):
    index = binary_search(lst,num)

    occurence = [index]

    # checking on left side

    i = index-1

    while i>=0:
        if lst[i]==num:
            occurence.append(i)
            i-=1
        else:
            break

    # checking on right side
        
    i = index+1

    while i<len(lst):
        if lst[i]==num:
            occurence.append(i)
            i+=1
        else:
            break
    
    return occurence
    


 

numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
number_to_find = 15  


res = number_of_occurence(numbers,number_to_find)

print(res)