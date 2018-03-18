a = input('enter name: ')


def hi():
    print('hello', a)
    print('hi', a)


def values():
    list = []
    UI = "\n"
    while (UI != ""):
        UI = input("Enter a value for the list: ")
    if (UI != ""):
        list.append(UI)
    print("The current values are: ")
    print(list)


def largeel():
    list = [1, 2, 3]
    print (max(list))
    return list


def revselist():
    list = [1, 2, 3]
    list = list[::-1]
    print (list)
    return list


def findel():
    list = [1, 2, 3]
    a = input('Enter a number: ')
    if 'a' in list:
        print(a, 'is in list')
    else:
        print('That is not in the list')
    return list


def oddnum(numbers, odds):
    list = [1, 2, 3]
    if list[0] % 2 == 1:
        odds.append(list[0])
    print(list)
    return list


def listsize():
    list = [1, 2, 3]
    print (len(list))
    return list


def palin():
    list = [1, 2, 3]
    return list == list[::-1]


def sumfor():
    list = 0
    for x in [1,2,3,4,5]:
        list = list + x
    print(sum(list))


def sumwhile():
    list = 0
    while list == 0:
        for x in [1,2,3,4,5]:
            list = list + x
    print(sum(list))

hi()
largeel()
values()
revselist()
findel()
listsize()




def sumrec():
    list = [1, 2, 3]
