#Get the filename from user
print("Enter the name of the file to be read")
fname = input(': ')

#Open the file specified by the user
try:
    f = open(fname, 'r') #'r' means read only, 'w' means write (clears old content if file exists)
    #'a' appends to the end of an existing file.
except FileNotFoundError:
    print("File does not exist")
    exit(0)

#print contents of file
for line in f:
    #Strip nex line character
    line=line.strip('\n')
    #Print line
    print(line)

#close file
f.close()

#Open file for write
f = open(fname, 'a')

#Add a new line to the file
f.write('\n')

#Write to file
f.write(input("Add a new line to the bottom of the file: "))

#Close file
f.close()