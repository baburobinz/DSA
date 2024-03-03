def insertion_sort(elements):

    for i in range(1,len(elements)):
      
        anchor = elements[i]
        j=i-1
        k = i
        while j>=0 and anchor<elements[j]:

            elements[k],elements[j]=elements[j],elements[k]
            j-=1
            k-=1

       
            
           
       
l = [5,4,3,21,10,25]



insertion_sort(l)

print(l)

