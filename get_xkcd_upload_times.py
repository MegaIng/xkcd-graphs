from datetime import datetime
from dateutil import tz
import time
import bs4
import requests
from csv import writer

MAX_XKCD = 2399

OUT_FILE = "xkcd_upload_times.csv"

with open(OUT_FILE, "w") as rf:
    with writer(rf) as f:
        for i in range(1, MAX_XKCD + 1):
            try:
                url = f"https://xkcd.com/{i}/"
                req = requests.get(url)
                p = bs4.BeautifulSoup(req.text, "html.parser")
                comic_url = "https:" + p.find("div", id='comic').find('img')['src']
                req_2 = requests.head(comic_url)
                raw_data = req_2.headers.get('Last-Modified', None)
                if raw_data is not None:
                    dt = datetime.strptime(raw_data, "%a, %d %b %Y %H:%M:%S %Z").astimezone(tz.gettz('UTC'))
                    f.writerow((i, datetime.isoformat(dt)))
            except Exception as e:
                print("failed to deal with", i)
                print(type(e), e)
            
            rf.flush()