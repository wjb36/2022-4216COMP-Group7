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
            if row[4] == "5.5":
                plottingData[0] = plottingData[0]+ 1
            elif row[4] == "5.51":
                plottingData[1] = plottingData[1] + 1
            elif row[4] == "5.52":
                plottingData[2] = plottingData[2] + 1
            elif row[4] == "5.53":
                plottingData[3] = plottingData[3] + 1
            elif row[4] == "5.55":
                plottingData[4] = plottingData[4] + 1
            elif row[4] == "5.58":
                plottingData[5] = plottingData[5] + 1
            elif row[4] == "5.6":
                plottingData[6] = plottingData[6] + 1
            elif row[4] == "5.64":
                plottingData[7] = plottingData[7] + 1
            elif row[4] == "5.66":
                plottingData[8] = plottingData[8] + 1
            elif row[4] == "5.67":
                plottingData[9] = plottingData[9] + 1
            elif row[4] == "5.69":
                plottingData[10] = plottingData[10] + 1
            elif row[4] == "5.7":
                plottingData[11] = plottingData[11] + 1
            elif row[4] == "5.72":
                plottingData[12] = plottingData[12] + 1
            elif row[4] == "5.73":
                plottingData[13] = plottingData[13] + 1
            elif row[4] == "5.75":
                plottingData[14] = plottingData[14] + 1
            elif row[4] == "5.77":
                plottingData[15] = plottingData[15] + 1
            elif row[4] == "5.8":
                plottingData[16] = plottingData[16] + 1
            elif row[4] == "5.82":
                plottingData[17] = plottingData[17] + 1
            elif row[4] == "5.84":
                plottingData[18] = plottingData[18] + 1
            elif row[4] == "5.88":
                plottingData[19] = plottingData[19] + 1
            elif row[4] == "5.89":
                plottingData[20] = plottingData[20] + 1
            elif row[4] == "5.9":
                plottingData[21] = plottingData[21] + 1
            elif row[4] == "5.94":
                plottingData[22] = plottingData[22] + 1
            elif row[4] == "5.97":
                plottingData[23] = plottingData[23] + 1
            elif row[4] == "6":
                plottingData[24] = plottingData[24] + 1
            elif row[4] == "6.02":
                plottingData[25] = plottingData[25] + 1
            elif row[4] == "6.1":
                plottingData[26] = plottingData[26] + 1
            elif row[4] == "6.12":
                plottingData[27] = plottingData[27] + 1
            elif row[4] == "6.2":
                plottingData[28] = plottingData[28] + 1
            elif row[4] == "6.21":
                plottingData[29] = plottingData[29] + 1
            elif row[4] == "6.29":
                plottingData[30] = plottingData[30] + 1
            elif row[4] == "6.3":
                plottingData[31] = plottingData[31] + 1
            elif row[4] == "6.31":
                plottingData[32] = plottingData[32] + 1
            elif row[4] == "6.34":
                plottingData[33] = plottingData[33] + 1
            elif row[4] == "6.35":
                plottingData[34] = plottingData[34] + 1
            elif row[4] == "6.36":
                plottingData[35] = plottingData[35] + 1
            elif row[4] == "6.4":
                plottingData[36] = plottingData[36] + 1
            elif row[4] == "6.45":
                plottingData[37] = plottingData[37] + 1
            elif row[4] == "6.47":
                plottingData[38] = plottingData[38] + 1
            elif row[4] == "6.48":
                plottingData[39] = plottingData[39] + 1
            elif row[4] == "6.5":
                plottingData[40] = plottingData[40] + 1
            elif row[4] == "6.57":
                plottingData[41] = plottingData[41] + 1
            elif row[4] == "6.6":
                plottingData[42] = plottingData[42] + 1
            elif row[4] == "6.69":
                plottingData[43] = plottingData[43] + 1
            elif row[4] == "6.7":
                plottingData[44] = plottingData[44] + 1
            elif row[4] == "6.72":
                plottingData[45] = plottingData[45] + 1
            elif row[4] == "6.8":
                plottingData[46] = plottingData[46] + 1
            elif row[4] == "6.9":
                plottingData[47] = plottingData[47] + 1
            elif row[4] == "6.93":
                plottingData[48] = plottingData[48] + 1
            elif row[4] == "7":
                plottingData[49] = plottingData[49] + 1
            elif row[4] == "7.1":
                plottingData[50] = plottingData[50] + 1
            elif row[4] == "7.2":
                plottingData[51] = plottingData[51] + 1
            elif row[4] == "7.3":
                plottingData[52] = plottingData[52] + 1
            elif row[4] == "7.4":
                plottingData[53] = plottingData[53] + 1
            elif row[4] == "7.5":
                plottingData[54] = plottingData[54] + 1
            elif row[4] == "7.6":
                plottingData[55] = plottingData[55] + 1
            elif row[4] == "7.7":
                plottingData[56] = plottingData[56] + 1
            elif row[4] == "7.8":
                plottingData[57] = plottingData[57] + 1
            elif row[4] == "7.9":
                plottingData[58] = plottingData[58] + 1
            elif row[4] == "8":
                plottingData[59] = plottingData[59] + 1
            elif row[4] == "8.1":
                plottingData[60] = plottingData[60] + 1
            elif row[4] == "8.2":
                plottingData[61] = plottingData[61] + 1
            elif row[4] == "8.3":
                plottingData[62] = plottingData[62] + 1
            elif row[4] == "8.4":
                plottingData[63] = plottingData[63] + 1
            elif row[4] == "8.5":
                plottingData[64] = plottingData[64] + 1
            elif row[4] == "8.6":
                plottingData[65] = plottingData[65] + 1
            elif row[4] == "8.8":
                plottingData[66] = plottingData[66] + 1
            elif row[4] == "9":
                plottingData[67] = plottingData[67] + 1
            elif row[4] == "9.1":
                plottingData[68] = plottingData[68] + 1



        plt.pie(plottingData, labels = chartLabels)
        plt.legend()
        plt.show() 