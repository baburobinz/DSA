def selection_sort(arr):

    size = len(arr)

    for i in range(size-1):

        min_index = i

        for j in range(min_index+1,size):

            if arr[min_index]>arr[j]:
                min_index=j

        arr[min_index],arr[i]=arr[i],arr[min_index]


l = [9,2,10,3,8,28]


selection_sort(l)

print(l)