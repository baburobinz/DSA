def shell_sort(arr):
    n = len(arr)
   
    gap = n//2
    while gap > 0:
        index_to_delete = []
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >= temp:
                if arr[j-gap] == temp:
                    index_to_delete.append(j)
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp

        if index_to_delete:
            for i in index_to_delete[::-1]:

                del arr[i]
    
      
        gap = gap//2

   
elements = [8,9,10,8]


shell_sort(elements)

print(elements)