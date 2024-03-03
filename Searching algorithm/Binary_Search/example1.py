import sys
sys.path.append('c:\\Users\\babu5\\OneDrive\\Desktop\\DSA\\Searching algorithm\\')

from check_run_time.check_run_time import time_it

def binary_search(list_of_numbers,number_to_find):
    left_index = 0
    right_index = len(list_of_numbers)-1

    while left_index<=right_index:

        mid_val = (left_index+right_index)//2

        if list_of_numbers[mid_val]==number_to_find:
            return mid_val
        if list_of_numbers[mid_val]<number_to_find:
            left_index=mid_val+1
        else:
            right_index=mid_val-1

    return -1

if __name__=='__main__':

    lst = [i for i in range(1,10)]

    n = 100

    print(binary_search(lst,n))
