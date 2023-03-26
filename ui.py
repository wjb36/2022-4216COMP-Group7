def mainMenu():
    menuEnd = False
    while menuEnd == False:
        menuInput = input("Please Select An Option:\n1. Create Line Chart\n2. Create Bar Chart\n3. Create Pie Chart\n4. Plot Earthquake Map Drawing\n5. Show Top 10\n6. Exit\n")
        menuInput = str(menuInput)
 
        if menuInput == "1":
            lineMenu()
        elif menuInput == "2":
            barMenu()
        elif menuInput == "3":
            pieMenu()
        elif menuInput == "4":
            mapPlot()
        elif menuInput == "5":
            top()
        elif menuInput == "6":
            menuEnd = True
        else:
            print("Invalid")
    
    
def lineMenu():
    menuEnd = False
    while menuEnd == False:
        menuInput = input("Please Select An Option:\n1. Create Line Graph for Number of Earthquakes between two Specified Day\n2. Create Bar Chart\n3. Create Pie Chart\n4. Plot Earthquake Map Drawing\n5. Show Top 10\n6. Exit\n")
        menuInput = str(menuInput)
 
        if menuInput == "1":
            print("Create Line Graph for Number of Earthquakes between two Specified Day")
        elif menuInput == "2":
            print("Earthquake2")
        elif menuInput == "3":
            print("Earthquake2")
        elif menuInput == "4":
            print("Earthquake2")
        elif menuInput == "5":
            print("Earthquake2")
        elif menuInput == "6":
            menuEnd = True
            mainMenu()
        else:
            print("Invalid")

def barMenu():
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

def pieMenu():
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

def mapPlot():
    menuEnd = False
    while menuEnd == False:
        menuInput = input("Please Select An Option:\n1. Create Line Chart\n2. Create Bar Chart\n3. Create Pie Chart\n4. Plot Earthquake Map Drawing\n5. Show Top 10\n6. Exit\n")
        menuInput = str(menuInput)
 
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