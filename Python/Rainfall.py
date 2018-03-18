
rain = input('Enter monthly rainfall for the year, separated by commas: ')
rainfall = rain.split(', ')
print(rainfall)

maxFall = max(rain)

minFall = min(rain)

length = len(rain)
print(length)

length = int(length)
rain = int(rain)

total = sum(rain)

av = total/length

print('The total was,', total, '\n', 'The average was,', av, '\n', 'The max was', maxFall, '\n', 'The minimum was', minFall)
print('The highest rainfall was {0}, the lowest rainfall was {1} the average rainfall was {2}'.format(maxFall,minFall,av))