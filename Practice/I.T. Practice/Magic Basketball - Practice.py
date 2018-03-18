"""Author: Jack Bark
   Version: 1.00
   This code makes and calls upon files of basketballers and gives information about them"""

#Enters data into the file
#
file = ()
def EnterNewData(file, list1):
    name = input('Enter player name: ')
    score = input('Enter points scored per game (seperate with spaces): ')
    entries = input('Enter how many data entries were made: ')
    list1.append(entries)
    list1.append(', ')
    list1.append(name)
    list1.append(', ')
    list1.append(score)
    file.write(list)
    return

#Loads a specified file based on the name entered
#It does this by asking for a name and then calling on it
def LoadPrevious():
    fileName = input('enter file name: ')
    file = open(fileName, 'r+')
    return(file)

#Searches for the specified name and returns player name, games played, points per game and total points
def SearchAndDisplay(file):
    print('Search function')
    if file == ():
        print('Must enter a file first!')
        LoadPrevious()
    name = input('Enter name: ')
    with open(file, 'r') as f:
        for list in f:
            if name in list:
                entries = [0]
                name = [1]
                score = [2]
                total = sum(score)
                print('Name:', name)
                print('# of games played:', entries)
                print('Points per game:', score)
                print('Total score:', total)
    return

#Exits program
def Exit():
    exit(1)

#Main menu
#This asks the user for a choice and then calls upon the function based upon their choice
def MenuOption():
    while True:
        print('Enter a number')
        print('     1. Enter new data')
        print('     2. Load previous data')
        print('     3. Search and display')
        print('     4. Exit')
        menuOption = input('Selection: ')

        if menuOption == '1':
            if file == ():
                print('Must enter a file first!')
                LoadPrevious()
            list1 = []
            EnterNewData(file, list1)

        elif menuOption == '2':
            LoadPrevious()

        elif menuOption == '3':
            if file == ():
                print('Must enter a file first!')
                LoadPrevious()
            SearchAndDisplay(file)

        elif menuOption == '4':
            Exit()

        else:
            print('Menu option doesnt exist')


MenuOption()
