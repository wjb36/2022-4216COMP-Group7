
import csv

import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime
import matplotlib.ticker as ticker


class earthquake:
    earthquakes = []


        

    with open('E:\earthquakeDatasetElliot.csv', 'r') as f:
        csv_reader = csv.reader(f)
        header_row = next(csv_reader)
        print(header_row)

        # each row is an earthquake
        for row in csv_reader:
            
            earthquakes.append(row)
    
       


    def averageMonthPie(earthquakes):
        pieData = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        pieLabels = ["January", "Febuary", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"]

        for row in earthquakes:
            Currentdate = datetime.strptime((row[0]), "%d-%b-%y").date()
            month = Currentdate.month
            IndexOfData = month - 1
            pieData[month -1] = pieData[month -1] + 1

        plt.pie(pieData, labels = pieLabels)
        plt.legend()
        plt.show()

    def averageMonthBar(earthquakes):
        numOfEarthquakes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        months = ["January", "Febuary", "March", "April", "May","June", "July", "August", "September", "October", "November", "December"]

        for row in earthquakes:
            Currentdate = datetime.strptime((row[0]), "%d-%b-%y").date()
            month = Currentdate.month
            IndexOfData = month - 1
            numOfEarthquakes[month -1] = numOfEarthquakes[month -1] + 1

        fig, ax = plt.subplots()
        ax.bar(months, numOfEarthquakes)
        plt.show()


        
            


        

    #averageMonthPie(earthquakes)
    #averageMonthBar(earthquakes)