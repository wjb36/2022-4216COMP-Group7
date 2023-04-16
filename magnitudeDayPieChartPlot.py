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
        plottingData = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        chartLabels = ["5.5", "5.51", "5.52", "5.53", "5.55", "5.58", "5.6", "5.64", "5.66", "5.67", "5.69", "5.7", "5.72", "5.73", "5.75", "5.77", "5.8", "5.82", "5.84", "5.88", "5.89", "5.9", "5.94", "5.97", "6", "6.02", "6.1", "6.12", "6.2", "6.21", "6.29", "6.3", "6.31", "6.34", "6.35", "6.36", "6.4", "6.45", "6.47", "6.48", "6.5", "6.57", "6.6", "6.69", "6.7", "6.72", "6.8", "6.9", "6.93", "7", "7.1", "7.2", "7.3", "7.4", "7.5", "7.6", "7.7", "7.8", "7.9", "8", "8.1", "8.2", "8.3", "8.4", "8.5", "8.6", "8.8", "9", "9.1"]

        for row in earthquakes:
            if row[4] == 5.5:
                plottingData[0] = plottingData[0]+ 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.52:
                plottingData[2] = plottingData[2] + 1
            elif row[4] == 5.53:
                plottingData[3] = plottingData[3] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1
            elif row[4] == 5.51:
                plottingData[1] = plottingData[1] + 1


        plt.pie(plottingData, labels = chartLabels)
        plt.legend()
        plt.show() 