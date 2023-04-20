import csv




import matplotlib.pyplot as plt

from datetime import date

from datetime import datetime

import matplotlib.ticker as ticker

import decimal





class earthquake:

    earthquakes = []
    with open('M:\earthquakeDataset.csv', 'r') as f:

        csv_reader = csv.reader(f)

        header_row = next(csv_reader)

        print(header_row)




# each row is an earthquake

        for row in csv_reader:

            earthquakes.append(row)





    def magAz(earthquakes):

        mag =[]

        az = []


        startDate = input("enter a start date? (D-MMM-YY)")
        startDate = datetime.strptime(startDate, "%d-%b-%y").date()

        endDate = input("enter an end date? (D-MMM-YY)")
        endDate = datetime.strptime(endDate, "%d-%b-%y").date()

        for row in earthquakes:
            row_date = datetime.strptime(row[0], "%d-%b-%y").date()
            if row_date >= startDate and row_date <= endDate:

                if row[6] != "" and row[7] != "":

                    mag.append(row[6])

                    az.append(row[7])



        fig, ax = plt.subplots()


        ax.bar(mag, az)

        plt.show()






    magAz(earthquakes)


