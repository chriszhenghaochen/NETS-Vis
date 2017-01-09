## for plot visit among time

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline

class Line(object):

    def __init__(self):
        print "line set up"

    def plot(self, user):
        start = '2015-12-17 10:00:00'
        duration = 360
        frequency = '1min'

        # stat = [10264, 10159, 10065]
        # stat = [100, 10001, 10006, 10010, 10014, 10022, 10023, 10027,  1003, 10038, 10041]
        # user = [503627775,504859938,512652879,555244338,555271842,555369238,555399799,555423387,573961197,604263429,604860278,613630354,624559610,624583556,634604646,664550682,796135821,796492691]
        # user.append(796140208)
        #stat = pd.read_csv("station.csv").values.ravel()

        plotdict = {}

        ########################file process######################
        file = pd.read_csv('output.csv')


        file = file[['user', 'start', 'end', 'station']]

        file['end'] = pd.to_datetime(file['end'])
        file['start'] = pd.to_datetime(file['start'])


        file = file.sort(['user','end'])


        #####################time processing###############

        val = file.values
        record = []
        target = []
        # dictStart = dict()
        dictEnd = {}
        # dictIP = dict()

        times = pd.date_range(start, periods=duration, freq=frequency)
        times = np.array(times)

        datStart = times[0]
        datEnd = times[len(times) - 1]

        #filter
        for i in range(0,len(val)):
            if (val[i][0] in user) and ((val[i][1] < datEnd and val[i][1] > datStart) or (val[i][2] < datEnd and val[i][2] > datStart)):
                record.append(val[i])

            #record.append(val[i])

        # print(record)


        for r in record:
            if r[0] in dictEnd:
                if r[3] in dictEnd[r[0]]:
                    dictEnd[r[0]][r[3]].append([r[1], r[2]])
                else:
                    dictEnd[r[0]][r[3]] = [[r[1], r[2]]]
            else:
                dictEnd[r[0]] = {}
                dictEnd[r[0]][r[3]] = [[r[1], r[2]]]

        print("OK done!")
        print(dictEnd.keys())

        for i in range(0, len(times)):
            for key, value in dictEnd.items():

                if key not in plotdict:
                    plotdict[key] = []

                count = 0
                for key1, value1 in value.items():
                    for v in value1:
                        # print(times[i])
                        # print(v[0])
                        # print(v[1])
                        if v[0] <= times[i] and v[1] >= times[i]:
                            #print(times[i])
                            count += 1
                            break;
                # print(count)
                plotdict[key].append(count)


        print(plotdict)
        print("raw data done")


        #plot
        label = []
        T = np.asarray(range(len(times)))
        xnew = np.linspace(T.min(), T.max(), 1200)

        for key, value in plotdict.items():
            power_smooth = spline(T, value, xnew)
            plt.plot(xnew, power_smooth)
            # plt.plot(times, value)
            label.append(key)

        # for key, value in plotdict.items():
        #     plt.plot(times, value)


        tick_locs = [xnew[0], xnew[int(len(xnew)/3)], xnew[int(len(xnew)/3*2)], xnew[int(len(xnew) - 1)]]
        tick_lbls = ([times[0], times[int(len(times)/3)], times[int(len(times)/3*2)], times[int(len(times) - 1)]])
        plt.xticks(tick_locs, tick_lbls)

        plt.legend(label, loc='upper left')
        plt.show()