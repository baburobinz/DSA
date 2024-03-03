import time

def time_it(func):

    def wrapper(*args,**kwargs):
        
        time_before = time.time()

        res = func(*args,**kwargs)

        time_taken = "%.3f"%(time.time()-time_before)

        print(f'time taken by {func.__name__} is {time_taken}s')
        return res
        
    return wrapper


