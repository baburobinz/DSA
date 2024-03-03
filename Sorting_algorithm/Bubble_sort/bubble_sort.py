def bubble_sort(lst):

    for i in range(len(lst)):

       

        for j in range(i+1,len(lst)):

            val1 = lst[i]
            
            val2=lst[j]

            if val1>val2:
                lst[i],lst[j]=lst[j],lst[i]



lst = [100,50,30,10,25,35]

res = bubble_sort(lst)

print(res)