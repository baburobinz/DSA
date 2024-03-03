import sys
sys.path.append('c:/Users/babu5/OneDrive\Desktop/DSA/Searching algorithm')

from check_run_time.check_run_time import time_it

def linear_search(lst,n):
    
    for idx in range(len(lst)):

        if lst[idx] == n:

            return idx

lst = [i for i in range(1,100000000)]

n = 99999999

res = time_it(linear_search)

print(res(lst,n))



    




