def bubble_sort(lst):

    size = len(lst)

    for i in range(size-1):

        swaped = False

        for j in range(size-1-i):

            if lst[j]>lst[j+1]:
                temp = lst[j]

                lst[j]=lst[j+1]
                lst[j+1]=temp

                swaped=True

        if not swaped:

            break

            


    return lst




l = [2,8,3,7,19,6,30,10,4,16,50,35,58,47,17,28]

res = bubble_sort(l)

print(res)
