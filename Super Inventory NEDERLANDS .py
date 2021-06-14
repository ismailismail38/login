import os
import fileinput


def menuDisplay():
    print('=============================')
    print('= Inventory Programma =')
    print('=============================')
    print('(1) Nieuwe Item Toevoegen')
    print('(2) Een Item Verwijderen')
    print('(3) Update Inventory Lijst')
    print('(4) Zoek een Item in Inventory')
    print('(5) Print Inventory ')
    print('(99) Quit')
    Keuze = int(input("Enter Je keuze: "))
    menuSelection(Keuze)
    Keuze


def menuSelection(Keuze):
    if Keuze == 1:
        addInventory()
    elif Keuze == 2:
        removeInventory()
    elif Keuze == 3:
        updateInventory()
    elif Keuze == 4:
        searchInventory()
    elif Keuze == 5:
        printInventory()
    elif Keuze == 99:
        exit()


def addInventory():
    InventoryFile = open('Inventory.txt', 'a')
    print("Toevoegen in Inventory")
    print("================")
    item_description = input("Geef de naam van de Item: ")
    item_quantity = input("Enter de hoeveelheid van de Item: ")
    InventoryFile.write(item_description + '\n')
    InventoryFile.write(item_quantity + '\n')
    InventoryFile.close()
    Keuze = int(input('Enter 98 om verder te gaan of 99 om te stoppen: '))
    if Keuze == 98:
        menuDisplay()

    else:
        exit()


def removeInventory():
    print("Verwijder Inventory")
    print("==================")
    item_description = input("Geef de Item naam om van Inventory te verwijderen: ")

    file = fileinput.input('Inventory.txt', inplace=True)

    for line in file:
        if item_description in line:
            for i in range(1):
                next(file, None)
        else:
            print(line.strip('\n'), end='\n')
    item_description
    Keuze = int(input('Enter 98 om verder te gaan of 99 om te stoppen: '))
    if Keuze == 98:
        menuDisplay()
    else:
        exit()


def updateInventory():
    print("Updating Inventory")
    print("==================")
    item_description = input('Enter de Item te updaten: ')
    item_quantity = int(input("Enter de hoeveelheid te updated. Enter - voor minder: "))

    with open('Inventory.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('Inventory.txt', 'r')
    file = f.read().split('\n')
    for i, line in enumerate(file):
        if item_description in line:
            for b in file[i + 1:i + 2]:
                value = int(b)
                change = value + (item_quantity)
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1
    f.close()

    filedata[count] = replace + '\n'

    with open('Inventory.txt', 'w') as f:
        for line in filedata:
            f.write(line)

    Keuze = int(input('Enter 98 om verder te gaan of 99 om te stoppen: '))
    if Keuze == 98:
        menuDisplay()
    else:
        exit()


def searchInventory():
    print('Zoeken in Inventory')
    print('===================')
    item_description = input('Enter de naam van de item: ')

    f = open('Inventory.txt', 'r')
    search = f.readlines()
    f.close
    for i, line in enumerate(search):
        if item_description in line:
            for b in search[i:i + 1]:
                print('Item:     ', b, end='')
            for c in search[i + 1:i + 2]:
                print('Hoeveelheid: ', c, end='')
                print('----------')

    Keuze = int(input('Enter 98 om verder te gaan of 99 om te stoppen: '))
    if Keuze == 98:
        menuDisplay()
    else:
        exit()


def printInventory():
    InventoryFile = open('Inventory.txt', 'r')
    item_description = InventoryFile.readline()
    print('Huidige Inventory')
    print('-----------------')
    while item_description != '':
        item_quantity = InventoryFile.readline()
        item_description = item_description.rstrip('\n')
        item_quantity = item_quantity.rstrip('\n')
        print('Item:     ', item_description)
        print('Hoeveelheid: ', item_quantity)
        print('----------')
        item_description = InventoryFile.readline()
    InventoryFile.close()

    Keuze = int(input('Enter 98 om verder te gaan of 99 om te stoppen: '))
    if Keuze == 98:
        menuDisplay()
    else:
        exit()



menuDisplay()
