import math

def mainMenu():
    print("Welcome To Earthquake Program")
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
    print("Earthquake1")

def barMenu():
    print("Earthquake2")

def pieMenu():
    print("Earthquake3")

def mapPlot():
    print("Earthquake4")
 
def top():
    print("Earthquake5")
    


mainMenu()