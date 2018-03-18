import math

i = 5

i = i + 3

print(i)

print(i-5)
print(i*5)
print(i/2)

print(i%5) #Mod 5, remainder of division

print(2^2) #Power/ index

i = 12
d = 5

print(int(i/5), 'r', i%5)

r = ((4+5)^3)/(12%5)

print(r)

print(math.sqrt(9)) #Square root

q = int(input('Day of the month? '))

m = int(input('Month of year? '))
if 1 or 2 in m:
    m = m+12

j = int(input('First two digits of the year? '))

k = int(input('Second two digits of the year? '))
k = k-1

h = int(q+((13*(m+1))/5)+k+(k/4)+(j/4)-25)%7

print(h)

if h == 0:
    print('It is Saturday')

if h == 1:
    print('It is Sunday')

if h == 2:
    print('It is Monday')

if h == 3:
    print('It is Tuesday')

if h == 4:
    print('It is Wednesday')

if h == 5:
    print('It is Thursday')

if h == 6:
    print('It is Friday')