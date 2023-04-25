import csv

import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime
import matplotlib.ticker as ticker

from geopy.geocoders import Nominatim

class earthquake:

    
    
    earthquakes = []
    with open('C:/Users/harri/Desktop/earthquakeDatasetElliot.csv') as f:
        csv_reader = csv.reader(f)
        header_row = next(csv_reader)
        print(header_row)



# each row is an earthquake
        for row in csv_reader:
            earthquakes.append(row)



    def location(earthquakes):
        
        geolocator = Nominatim(user_agent="geoapiExercises")
        
        lats = []
        longs = []

        allRecords = str(input("Would you like to use all records? [Y/N]: ")).upper()
        isRange = str(input("Would you like to use a range of dates? [Y/N]: ")).upper()
        if isRange == "Y":
            startDate = input("Enter a start date (D-MMM-YY) : ")
            startDate = datetime.strptime(startDate, "%d-%b-%y").date()
            endDate = input("Enter an end date (D-MMM-YY) : ")
            endDate = datetime.strptime(endDate, "%d-%b-%y").date()
        else:
            date = input("Enter a date (D-MMM-YY) : ")
            date = datetime.strptime(date, "%d-%b-%y").date()

        for row in earthquakes:
            row_date = datetime.strptime(row[0], "%d-%b-%y").date()
            if isRange == "Y":
                if row_date >= startDate and row_date <= endDate:
                    if allRecords == "Y":
                        if row[1] != "" and row[2] != "":
                            lats.append(row[1])
                            longs.append(row[2])
                    else:
                        if row[1] != "" and row[2] != "" and row[11] == "TRUE":
                            lats.append(row[1])
                            longs.append(row[2])
            else:
                if row_date == date:
                    if allRecords == "Y":
                        if row[1] != "" and row[2] != "":
                            lats.append(row[1])
                            longs.append(row[2])
                    else:
                        if row[1] != "" and row[2] != "" and row[11] == "TRUE":
                            lats.append(row[1])
                            longs.append(row[2])

        for i in range(len(lats)):
            Latitude = lats[i]
            Longitude = longs[i]
            location = geolocator.geocode(Latitude+","+Longitude)
            print(location)
                    

    location(earthquakes)
