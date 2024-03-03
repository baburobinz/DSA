def partition(elements,start,end):

    pivot = elements[end]
    i=start-1

    for j in range(start,end):

        if elements[j]<=pivot:
            i+=1
            elements[i],elements[j]=elements[j],elements[i]
    elements[i+1],elements[end]=elements[end],elements[i+1]

    return i+1



def quick_sort(elements,start,end):
    if start<end:
        pi = partition(elements,start,end)
        quick_sort(elements,start,pi-1)
        quick_sort(elements,pi+1,end)


l = [10,5,7,2,9,3,1,6,4,8]

start = 0

end = len(l)-1



quick_sort(l,0,len(l)-1)

print(l)