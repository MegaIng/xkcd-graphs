import matplotlib.pyplot as plt
import matplotlib.dates as dates

from csv import reader
from datetime import datetime

with open("xkcd_upload_times.csv") as rf:
    data_x = []
    data_y = []
    for row in reader(rf):
        data_x.append(int(row[0]))
        data_y.append(dates.date2num(datetime.fromisoformat(row[1]))%1)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot_date(data_x, data_y, 'ro', xdate=False, ydate=True)
ax.yaxis_date()
fig.autofmt_xdate()

plt.show()
datetime.fromisoformat(row[1])
