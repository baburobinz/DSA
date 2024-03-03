def find_min(arr):

    min = arr[0]

    for i in range(1,len(arr)):
        if arr[i]<min:
            min=arr[i]

    return min


arr = [10,3,2,100,6,8]

print(find_min(arr))