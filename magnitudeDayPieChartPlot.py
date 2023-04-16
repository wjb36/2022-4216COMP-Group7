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

        # each row is an earthquake
        for row in csv_reader:
            earthquakes.append(row)

    def plotMagDayPie(earthquakes):
        
        