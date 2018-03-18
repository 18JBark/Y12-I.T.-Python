print('Hello, this is Ramu' + "'" + 's Vintage Calculator')

#Opens files for the code
f = open('weekly-harvest.txt', 'r')
g = open('outp-weekly-harvest.txt', 'w')

#Finds the profit made from the grapes
def getProfit(cP, sP, sA):
    g.write('\n' "Profit made from grapes" '\n')
    p = (sA*(sP-cP))
    g.write(str(p))
    return p

#Uses (slt) to determine whether or not Ramu's wine will be good or not
def getVintage(slt):
    if slt >= 100:
        print('Vintage is excellent')
    if slt < 100 >= 40:
        print('Vintage is good')
    if slt < 40:
        print('Vintage is poor')


cP = float(input('Cost of producing grapes: $ '))
sP = float(input('Selling price of grapes (Tonnes): '))

vlist = []
listtotal = []


for line in f:
    line=line.strip('\n')
    line=line.split(' ')

#removes the first thing in the list
    vname = line.pop(0)
    vlist.append(vname)

    total = 0
    for i in line:
        total += float(i)

    listtotal.append(total)


#Working out the combined number of everything in the list
slt = (sum(listtotal))

#Writing the sum(listtotal) to the output file
g.write("Total grapes" '\n')
g.write(str(slt))

#Finding and writing the average of the grapes collected to output file
g.write('\n' "Average grapes" '\n')
a = (slt/7)
g.write(str(a))

#Finding and writing the min number of grapes to output file
g.write('\n' "The min grapes collected" '\n')
b = min(listtotal)
g.write (str(b))

#Finding and writing the max number of grapes to the output file
g.write('\n' "The max grapes collected" '\n')
g.write(str(max(listtotal)))
g.write('\n')

#Calculates the amount of grapes sold
g.write("The amount of grapes sold" '\n')
sA = slt*.45
g.write(str(sA))

#print min and max for the user
print('\n' 'Your max is:')
print(max(listtotal), '\n')
print('Your min is:')
print(min(listtotal), '\n')

#Running both functions
getProfit(cP, sP, slt)
getVintage(slt)