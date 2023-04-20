import csv

import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime
import matplotlib.ticker as ticker
import decimal


class earthquake:
    earthquakes = []


        

    with open('C:\earthquakeDataset.csv', 'r') as f:
        csv_reader = csv.reader(f)
        header_row = next(csv_reader)
        print(header_row)

        # each row is an earthquake
        for row in csv_reader:
            earthquakes.append(row)
    


    def magniStatAzimuth(earthquakes):
        magniStat = [0]
        azimuth = [0]

        for row in earthquakes:
            if row[6] != "":
                magniStat.append(decimal.Decimal(row[6]))
            if row[7] != "":
                azimuth.append(decimal.Decimal(row[7]))
        
        fig, ax = plt.subplots()
        ax.bar(magniStat, azimuth)

        plt.show()
        
    magniStatAzimuth(earthquakes)