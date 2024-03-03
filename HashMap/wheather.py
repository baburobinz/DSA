file = open('nw_weather.csv','r')
temp_dict = {}
arr =[]

for line in file:

    token = line.split(',')

    try:

        temperature = int(token[1])
        month = token[0]

        temp_dict[month]=temperature
        arr.append(temperature)

    except:

        continue


print(arr)

# avg temp in a week
avg_temperature_of_week = sum(arr[0:7])/7

print(avg_temperature_of_week)

# max temp in a first 10 days


max_temp = max(arr[0:10])

print(max_temp)



# lets stores this in dict

print(temp_dict)


# temp on jan9?

jan9 = temp_dict['Jan 9']
jan4 = temp_dict['Jan 4']

print(f'tem on jan 9 : {jan9} ')
print(f'tem on jan 4 : {jan4} ')







  



