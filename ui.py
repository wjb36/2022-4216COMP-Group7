import math

def mainMenu():
    menuEnd = False
    while menuEnd == False:
        x = input("Please Select An Option:\n1. Create Line Chart\n2. Create Bar Chart\n3. Create Pie Chart\n4. Plot Earthquake Map Drawing\n5. Show Top 10\n6. Exit\n")
        x = str(x)
 
        if x == "1":
            lineMenu()
        elif x == "2":
            barMenu()
        elif x == "3":
            pieMenu()
        elif x == "4":
            mapPlot()
        elif x == "5":
            top()
        elif x == "6":
            menuEnd = True
        else:
            print("Invalid")
    
    
def lineMenu():
    menuEnd = False
    while menuEnd == False:
        x = input("Please Select An Option:\n1. Create Line Chart\n2. Create Bar Chart\n3. Create Pie Chart\n4. Plot Earthquake Map Drawing\n5. Show Top 10\n6. Exit\n")
        x = str(x)
 
        if x == "1":
            print("Earthquake2")
        elif x == "2":
            print("Earthquake2")
        elif x == "3":
            print("Earthquake2")
        elif x == "4":
            print("Earthquake2")
        elif x == "5":
            print("Earthquake2")
        elif x == "6":
            menuEnd = True
            mainMenu()
        else:
            print("Invalid")

def barMenu():
    menuEnd = False
    while menuEnd == False:
        x = input("Please Select An Option:\n1. Create Line Chart\n2. Create Bar Chart\n3. Create Pie Chart\n4. Plot Earthquake Map Drawing\n5. Show Top 10\n6. Exit\n")
        x = str(x)
 
        if x == "1":
            print("Earthquake2")
        elif x == "2":
            print("Earthquake2")
        elif x == "3":
            print("Earthquake2")
        elif x == "4":
            print("Earthquake2")
        elif x == "5":
            print("Earthquake2")
        elif x == "6":
            menuEnd = True
            mainMenu()
        else:
            print("Invalid")

def pieMenu():
    menuEnd = False
    while menuEnd == False:
        x = input("Please Select An Option:\n1. Create Line Chart\n2. Create Bar Chart\n3. Create Pie Chart\n4. Plot Earthquake Map Drawing\n5. Show Top 10\n6. Exit\n")
        x = str(x)
 
        if x == "1":
            print("Earthquake2")
        elif x == "2":
            print("Earthquake2")
        elif x == "3":
            print("Earthquake2")
        elif x == "4":
            print("Earthquake2")
        elif x == "5":
            print("Earthquake2")
        elif x == "6":
            menuEnd = True
            mainMenu()
        else:
            print("Invalid")

def mapPlot():
    menuEnd = False
    while menuEnd == False:
        x = input("Please Select An Option:\n1. Create Line Chart\n2. Create Bar Chart\n3. Create Pie Chart\n4. Plot Earthquake Map Drawing\n5. Show Top 10\n6. Exit\n")
        x = str(x)
 
        if x == "1":
            print("Earthquake2")
        elif x == "2":
            print("Earthquake2")
        elif x == "3":
            print("Earthquake2")
        elif x == "4":
            print("Earthquake2")
        elif x == "5":
            print("Earthquake2")
        elif x == "6":
            menuEnd = True
            mainMenu()
        else:
            print("Invalid")
 
def top():
    menuEnd = False
    while menuEnd == False:
        x = input("Please Select An Option:\n1. Create Line Chart\n2. Create Bar Chart\n3. Create Pie Chart\n4. Plot Earthquake Map Drawing\n5. Show Top 10\n6. Exit\n")
        x = str(x)
 
        if x == "1":
            print("Earthquake2")
        elif x == "2":
            print("Earthquake2")
        elif x == "3":
            print("Earthquake2")
        elif x == "4":
            print("Earthquake2")
        elif x == "5":
            print("Earthquake2")
        elif x == "6":
            menuEnd = True
            mainMenu()
        else:
            print("Invalid")
    

print("Welcome To Earthquake Program")
mainMenu()