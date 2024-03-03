def multi_level_sorting(arr,preference):

    for pref in reversed(preference):



        size = len(arr)

        for i in range(size-1):

            min_index = i

            for j in range(min_index+1,size):

                if arr[min_index][pref]>arr[j][pref]:

                    min_index=j

            if min_index!=i:

                arr[min_index],arr[i]=arr[i],arr[min_index]



   


l = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]


multi_level_sorting(l,['First Name','Last Name'])

print(*l,sep='\n')
