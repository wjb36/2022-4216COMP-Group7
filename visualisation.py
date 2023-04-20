
import csv

import matplotlib.pyplot as plt
from datetime import date
from datetime import datetime
import matplotlib.ticker as ticker
import decimal


class earthquake:
    earthquakes = []

    with open('E:\earthquakeDatasetElliot.csv', 'r') as f:
        csv_reader = csv.reader(f)
        header_row = next(csv_reader)
        print(header_row)

        # each row is an earthquake
        for row in csv_reader:

            earthquakes.append(row)


    def fiveDateBar(earthquakes):
        usersDates = []
        values = [0, 0, 0, 0, 0]

        # asking user to input dates and formating them into a datetime
        for i in range(5):
            usersDate = (input("enter a date? (D-MMM-YY) "))
            formatedDate = datetime.strptime(usersDate, "%d-%b-%y").date()
            usersDates.append(formatedDate)

        # matching users dates to files dates
        for item in range(len(usersDates)):
            for row in earthquakes:
                Currentdate = datetime.strptime((row[0]), "%d-%b-%y").date()
                if Currentdate == usersDates[item]:
                    values[item] += 1
        print(usersDates)

        # Turns dates into a string
        for h in range(len(usersDates)):
            usersDates[h] = datetime.strftime(usersDates[h], "%y-%m-%d")

        fig, ax = plt.subplots()
        ax.bar(usersDates, values)

        ax.set_xlabel("Date")
        ax.set_ylabel("Number Of Earthquakes")
        ax.set_title("Earthquakes Per Day")

        ax.xaxis.grid()
        ax.yaxis.grid()

        plt.show()

    def magnitudetVsTime(earthquakes):

        mag = []
        time = []

        sortedEarthquakes = sorted(earthquakes, key=lambda x: x[5])

        startDate = input("enter a start date? (D-MMM-YY)")
        startDate = datetime.strptime(startDate, "%d-%b-%y").date()

        endDate = input("enter an end date? (D-MMM-YY)")
        endDate = datetime.strptime(endDate, "%d-%b-%y").date()

        for row in sortedEarthquakes:
            row_date = datetime.strptime(row[0], "%d-%b-%y").date()
            if row_date >= startDate and row_date <= endDate:
                if row[5] != "":
                    mag.append(decimal.Decimal(row[4]))
                    time.append(row[5])

        print(mag)
        print(time)

        

        fig, (left, right) = plt.subplots(1, 2)
        left.bar(time, mag)
        right.scatter(time, mag)

        left.set_xlabel('Time')
        right.set_xlabel('Time')
        left.set_ylabel('Magnitude')
        right.set_ylabel('Magnitude')
        left.set_title("Bar chart")
        right.set_title("Scatter graph")

        plt.xticks(rotation=45)
        plt.show()

    def trueFalsePie(earthquakes):
        pieData = [0, 0]
        pieLabels = ["true", "false"]

        for row in earthquakes:
            if row[11] == "TRUE":
                pieData[0] = pieData[0] + 1
            elif row[11] == "FALSE":
                pieData[1] = pieData[1] + 1

        plt.pie(pieData, labels=pieLabels)
        plt.legend()
        plt.show()

    def dataSourcePie(earthquakes):
        pieData = []
        pieLabels = [""]
        z = 1

        for row in earthquakes:
            print(z)
            if row[10] != "":
                for i in range(len(pieLabels)):
                    if row[10] == i:
                        pieData[pieLabels.index(
                            i)] = pieData[pieLabels.index(i)] + 1
                    else:
                        pieLabels.append(row[10])
                        pieData.append(1)

            z = z+1

        print("hello")
        plt.pie(pieData, labels=pieLabels)
        plt.legend()
        plt.show()

    def azimuthalGapPie(earthquakes):
        pieData = [0,0]
        pieLabels = ["under 180", "Over 180"]
        
        for row in earthquakes:
            if row[7] != "":
                if float(row[7]) >= 180:
                    pieData[1] = pieData[1] + 1
                elif float(row[7]) < 180:
                    pieData[0] = pieData[0] + 1

        plt.pie(pieData, labels=pieLabels)
        plt.legend()
        plt.show()

    # dataSourcePie(earthquakes)
    # trueFalsePie(earthquakes)
    #magnitudetVsTime(earthquakes)
    # fiveDateBar(earthquakes)
    # azimuthalGapPie(earthquakes)
