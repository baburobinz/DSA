import threading
import time


def cal_square(nums):

    print('calculating Squares...')

   
    for n in nums:
        time.sleep(0.2)

        print(f'Square : {n*n}')


def calc_cube(nums):

    print('Calculating Cubes..!')
    

    for n in nums:
        time.sleep(0.2)

        print(f'cube : {n**3}')

nums = [2,4,8,10]
time_before = time.time()

# cal_square(nums)
# calc_cube(nums)
t1 = threading.Thread(target=cal_square,args=(nums,))
t2 = threading.Thread(target=calc_cube,args=(nums,))
t1.start()
t2.start()
t1.join()
t2.join()
print(f'time taken : {time.time()-time_before}')