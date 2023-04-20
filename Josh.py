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



    def magAz(earthquakes):
        mag =[]
        az = []

        allRecords = str(input("Would you like to use all records? [Y/N]: "))

        startDate = input("Enter a start date? (D-MMM-YY): ")
        startDate = datetime.strptime(startDate, "%d-%b-%y").date()

        endDate = input("Enter an end date? (D-MMM-YY): ")
        endDate = datetime.strptime(endDate, "%d-%b-%y").date()

        for row in earthquakes:
            row_date = datetime.strptime(row[0], "%d-%b-%y").date()
            if row_date >= startDate and row_date <= endDate:
                if allRecords == "Y":  
                    if row[6] != "" and row[7] != "":
                        mag.append(decimal.Decimal(row[6]))
                        az.append(decimal.Decimal(row[7]))
                elif allRecords == "N":
                    if row[6] != "" and row[7] != "" and row[11] == "TRUE":
                        mag.append(decimal.Decimal(row[6]))
                        az.append(decimal.Decimal(row[7]))
                    


        fig, ax = plt.subplots()
        ax.bar(mag, az)
        ax.grid(True)
        ax.set_title("The Number of Magnitude Stations in Relation to Azimuthal Gap")
        ax.set_xlabel("Number of Magnitude Seismic Stations")
        ax.set_ylabel("Azimuthal Gap (°)")
        plt.show()


    magAz(earthquakes)


