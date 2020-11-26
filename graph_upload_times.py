import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib as mpl

from csv import reader
import datetime as dt
import dateutil.parser as dtp
from dateutil import tz

plt.ion()
plt.clf()
plt.show()

with open("xkcd_upload_times.csv") as rf:
    data_x = []
    data_y = []
    for row in reader(rf):
        data_x.append(int(row[0]))
        data_y.append(
        	dt.datetime.combine(
        		dt.datetime.utcfromtimestamp(0),
        		dtp.isoparse(row[1]).astimezone(tz=tz.gettz('America/New York')).time()
        	)
      	)

plt.scatter(data_x, dates.date2num(data_y), marker='o', c='r')
plt.xlabel('Comic number')
plt.ylabel('Time of day (EST + DST)')
plt.title('XKCD upload time of day vs. comic number')
plt.gca().yaxis.set_major_formatter(mpl.dates.DateFormatter('%H:%M'))

input()