import csv

import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime
import matplotlib.ticker as ticker


class earthquake:
    earthquakes = []

    with open('M:\earthquakeDataset.csv', 'r') as f:
        csv_reader = csv.reader(f)
        header_row = next(csv_reader)
        print(header_row)

        for row in csv_reader:
            earthquakes.append(row)

    def plotMagDayPie(earthquakes):
        
        requestedDate = (input("enter a date? (D-MMM-YY) "))
        formatedDateRequest = datetime.strptime(requestedDate, "%d-%b-%y").date()
        
        plottingData = [0]
        chartLabels = [0.0]

        
        

        for i in range(len(chartLabels)):
            for row in earthquakes:
                Currentdate = datetime.strptime((row[0]), "%d-%b-%y").date()
                if Currentdate == formatedDateRequest:
                    if float(row[4]) == i:
                        plottingData[chartLabels.index(i)] = plottingData[chartLabels.index(i)] + 1
                    else:
                        chartLabels.append(row[4])
                        plottingData.append(1)
        print(chartLabels, plottingData)

        plt.pie(plottingData, labels = chartLabels)
        plt.legend()
        plt.show() 

    plotMagDayPie(earthquakes)