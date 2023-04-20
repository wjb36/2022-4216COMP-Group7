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




        for row in earthquakes:

            if row[6] != "" and row[7] != "":

                mag.append(row[6])

                az.append(row[7])



        fig, ax = plt.subplots()


        ax.bar(mag, az)

        plt.show()






    magAz(earthquakes)


