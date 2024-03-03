def insertion_sort(elements):
    for i in range(1,len(elements)):
        anchor = elements[i]
        j=i-1

        while anchor<elements[j] and j>=0:
            elements[j+1]=elements[j]

            j-=1

        elements[j+1]=anchor


        


l = [2,7,1]

insertion_sort(l)

print(l)