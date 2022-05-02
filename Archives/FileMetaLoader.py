import os
import json
from datetime import date

def CheckAndSort():
    to_remove = []
    files = os.listdir(os.getcwd())
    for file in files:
        NAME = file.split('.')
        print(NAME)
        if NAME[1] != 'json':
            to_remove.append(file)

    for not_json in to_remove:
        files.remove(not_json)
        print("REMOVED: ", not_json)
        
    return files

STATS = []
TOTAL_HITS = 0
for JSON in CheckAndSort():
    print(JSON)
    filename = JSON.split('.')
    datefromname = filename[0].split('-')
    dobj=date(int(datefromname[0]),int(datefromname[1]),1)#YEAR-MONTH-fakeday
    with open(JSON, encoding='utf-8') as f:
        data = json.load(f)
        if len(data["response"]["docs"]) == 0:
            continue
        TOTAL_HITS += int(data["response"]["meta"]["hits"])
        STATS.append({"date":dobj.isoformat(),"hits":data["response"]["meta"]["hits"]})

SAVEME = {"total_htis":TOTAL_HITS,"metadata_by_month":STATS}
with open('Metadata.json','w',encoding='utf-8') as s:
    json.dump(SAVEME, s, ensure_ascii=False, indent=4)
    s.close()
