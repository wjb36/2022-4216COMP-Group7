import visualisation

def mainMenu():
    menuEnd = False
    while menuEnd == False:
        menuInput = input("Please Select An Option:\n1. Create Line Chart\n2. Create Bar Chart\n3. Create Pie Chart\n4. Plot Earthquake Map Drawing\n5. Show Top 10\n6. Exit\n")
        menuInput = str(menuInput)
 
        if menuInput == "1":
            print("You Have Selected To Display Line Charts For Your Data Query")
            lineMenu()
        elif menuInput == "2":
            print("You Have Selected To Display Bar Charts For Your Data Query")
            barMenu()
        elif menuInput == "3":
            print("You Have Selected To Display Pie Charts For Your Data Query")
            pieMenu()
        elif menuInput == "4":
            print("You Have Selected To Display A Map Plot For Your Data Query")
            mapMenu()
        elif menuInput == "5":
            print("You Have Selected To Display A Ranking For Your Data Query")
            rankingsMenu()
        elif menuInput == "6":
            print("Goodbye")
            menuEnd = True
        else:
            print("Invalid")
    
    
def lineMenu():
    #Waiting For Elliot's Code File
    menuEnd = False
    while menuEnd == False:
        menuInput = input("Please Select An Option:\n1. Create Line Graph for Number of Earthquakes between two Specified Day\n2. \n3. \n4. \n5. \n6. Return\n")
        menuInput = str(menuInput)
 
        if menuInput == "1":
            print("Create Line Graph for Number of Earthquakes between two Specified Day")
        elif menuInput == "2":
            print("Option 2")
        elif menuInput == "3":
            print("Option 3")
        elif menuInput == "4":
            print("Option 4")
        elif menuInput == "5":
            print("Option 5")
        elif menuInput == "6":
            menuEnd = True
            mainMenu()
        else:
            print("Invalid")

def barMenu():
    #Waiting For Elliot's Code File
    menuEnd = False
    while menuEnd == False:
        menuInput = input("Please Select An Option:\n1. \n2. \n3. \n4. Return\n")
        menuInput = str(menuInput)
 
        if menuInput == "1":
            print("Option 1")
        elif menuInput == "2":
            print("Option 2")
        elif menuInput == "3":
            print("Option 3")
        elif menuInput == "4":
            menuEnd = True
            mainMenu()
        else:
            print("Invalid")

def pieMenu():
    #Waiting For Elliot's Code File
    menuEnd = False
    while menuEnd == False:
        menuInput = input("Please Select An Option:\n1. Create Pie Chart to Show Percentage of True vs False for All Records\n2. Create Pie Chart to Show Percentage of Earthquakes with an Azimuthal Gap Below 180°\n3. Create Pie Chart to Show Percentage of Earthquakes based on Location\n4. Return\n")
        menuInput = str(menuInput)
 
        if menuInput == "1":
            print("Create Pie Chart to Show Percentage of True vs False for All Records")
        elif menuInput == "2":
            print("Create Pie Chart to Show Percentage of Earthquakes with an Azimuthal Gap Below 180°")
        elif menuInput == "3":
            print("Create Pie Chart to Show Percentage of Earthquakes based on Location")
        elif menuInput == "4":
            menuEnd = True
            mainMenu()
        else:
            print("Invalid")

def mapMenu():
    print("Map Plot")
    mainMenu()
 
def rankingsMenu():
    #Waiting For Maaria's Code File
    menuEnd = False
    while menuEnd == False:
        x = input("Please Select An Option:\n1. \n2. \n3. \n4. \n5. \n6. Return\n")
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