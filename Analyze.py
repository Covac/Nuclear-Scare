import os
import json
from datetime import date
from statistics import stdev

import matplotlib.pyplot as plt
import matplotlib.dates as mdates


METADATA = None
MATCHES = None
with open('Metadata.json', encoding='utf-8') as meta:
    METADATA = json.load(meta)
    meta.close()

with open('Matches.json', encoding='utf-8') as match:
    MATCHES = json.load(match)
    match.close()

total_articles = MATCHES["total_articles"]
matched_articles = MATCHES["number_matched"]


for MATCH in MATCHES["matches"]:
    MATCH["date"] = date.fromisoformat(MATCH["date"].split("T")[0])

for META in METADATA["metadata_by_month"]:
    META["date"] = date.fromisoformat(META["date"])
    META["matches"] = []
    for MATCH in MATCHES["matches"]:
        if MATCH["date"].year == META["date"].year and MATCH["date"].month == META["date"].month:
            for keyword in MATCH["keywords"]:
                if keyword == "Nuclear Energy":
                    META["matches"].append(MATCH)
                    break

Xdates = []
Yper = []
for META in METADATA["metadata_by_month"]:
    if len(META["matches"])>0 and META["date"].year >= 2009:
        print(META["date"].isoformat()+' with '+str(len(META["matches"]))+' matches')
        print("Percentage: "+str(round(len(META["matches"])/META["hits"]*100,2))+'%')
        Yper.append(len(META["matches"])/META["hits"]*100)
        Xdates.append(META["date"])

std = stdev(Yper)
print("Average percentage: "+str(std)+"%")

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
plt.plot(Xdates,Yper)
plt.gcf().autofmt_xdate()
plt.axhline(y=std, color="black", linestyle=":")
plt.show()
