def merge_sort(elements):

    if len(elements)==1:
        return elements
    
    mid = len(elements)//2

    left = elements[:mid]
    right = elements[mid:]

    merge_sort(left)
    merge_sort(right)

    sort_item(left,right,elements)

def sort_item(left,right,elements):
    
    i=j=k=0

    while i<len(left) and j<len(right):

        if left[i]<=right[j]:
            elements[k]=left[i]
            i+=1
        else:
            elements[k]=right[j]
            j+=1

        k+=1

    while i<len(left):
        elements[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        elements[k]=right[j]
        j+=1
        k+=1
        

# l = [10,8,3,9,4,7,6,2,3,1]

l=[3,1,4,2]

merge_sort(l)

print(l)
