
#Searches the file
def SearchFunction(name):
    print('Search function')
    with open("contacts.txt") as f:
        for line in f:
            if name in line:
                print(line)
    return


#Loads file
def LoadContacts():
    print('Load contacts')
    contacts = open('contacts.txt', 'r+')

    return contacts


#Creates contact
def NewContact():
    print('New contact')
    name = input('Enter a name: ')
    birthday = input('Enter birthday (e.g. 18/2): ')
    SaveFile(name, birthday)
    return


#Changes the birthday of a contact
def ChangeBirthday():
    print("Change birthday")
    LoadContacts()
    name = input('Enter a name: ')
    SearchFunction(name)
    birthday = input('Enter birthday (e.g. 18/2): ')
    with open("contacts.txt") as f:
        if name in f:
            for line in f:
                if name in line:
                    line.strip(line)
    SaveFile(name, birthday)
    return


#Deletes contact
def DeleteContact():
    print('Delete contact')
    name = input('Enter a name: ')
    #g = open("contacts-W.txt")
    #f = open("contacts.txt","r+")
    index = SearchFunction(name)
    print("Are you sure you wish to delete this record? (Yes/No) ")
    userResponse = input(": ")
    if userResponse == "Yes":
        with open("contacts.txt") as f:
            if name in f:
                for line in f:
                    if name in line:
                        line.strip(line)
    #with open("contacts.txt") as f:
    #Finds the line that contains the name and deletes it
        #for line in f:
            #if name +',' != line:
               # g.write(f)
    return


#Looks up the birthday and the contact associated with it
def LookupBirthday():
    print('Lookup birthday')
    birthday = input('Enter birthday (e.g. 18/2): ')
    with open("contacts.txt") as f:
        for line in f:
            if birthday in line:
                print(line)
    return


#Saves contacts to file
def SaveFile(name, birthday):
    contacts = open('contacts.txt', 'a')
    print('File saved')
    names = []
    birthdays = []
    names.append(name)
    birthdays.append(birthday)
    contacts.write(names[0])
    contacts.write(', ')
    contacts.write(birthdays[0])
    #contacts.write('/')
    #contacts.write(birthdays[1])
    contacts.write('\n')
    contacts.close()
    return

#The menu
menuOption = 0

LoadContacts()

while True:
    f = open("contacts.txt")
    print('Please enter the number of the option you wish to see:')
    print('     1. Lookup birthday')
    print('     2. Add a new contact with a birthday')
    print('     3. Change birthday')
    print('     4. Delete a contact and a birth date')
    print('     5. Quit the program')
    menuOption = input('Selection: ')
    if menuOption == '1':
        LookupBirthday()

    elif menuOption == '2':
        NewContact()

    elif menuOption == '3':
        ChangeBirthday()

    elif menuOption == '4':
        DeleteContact()

    elif menuOption == '5':
        exit(0)
    else:
        print('Menu option doesnt exist')
        menuOption = 0
