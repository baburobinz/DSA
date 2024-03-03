import sys
sys.path.append('C:\\Users\\babu5\\OneDrive\\Desktop\\DSA\\Searching algorithm')
from check_run_time.check_run_time import time_it


def binary_search_recursion(list_of_nums,num,start_index,end_index):

    if end_index<start_index:
        return -1
    if start_index>len(list_of_nums)-1 or end_index<0:
        return -1
    mid_index = (start_index+end_index)//2
    mid_val = list_of_nums[mid_index]

    if mid_val==num:
        return mid_index
    if mid_val<num:

        start_index=mid_index+1
    
    else:
        end_index=mid_index-1

    return binary_search_recursion(list_of_nums,num,start_index,end_index)

lst = [i for i in range(100)]

num = 99

res = binary_search_recursion(lst,num,0,len(lst))

print(res)

