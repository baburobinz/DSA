def sum_of_recursion_list(lst):

    total = 0

    for i in lst:
        if type(i)==list:
            total+=sum_of_recursion_list(i)
        else:
            total+=i

    return total

print(sum_of_recursion_list([[3,4], [5,6]]))