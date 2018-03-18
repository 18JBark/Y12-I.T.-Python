import math


a = int(input('First side? '))

a = a^2


b = int(input('Second side? '))
b = b^2

c = a + b

print('C^2 = ',c)

angle = math.atan(a/b)
angle = str(round(angle, 2))

print('the angle in degrees is',angle)