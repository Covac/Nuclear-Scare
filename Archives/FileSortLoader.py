import os
import json

def Standardize():
    files = os.listdir(os.getcwd())
    for file in files:
        extractname = file.rstrip('.json')
        DATE = extractname.split('-')
        #print(DATE)
        if len(DATE[1]) == 1:
            DATE[1]='0'+DATE[1]
            newname = '-'.join(DATE)+'.json'
            print('RENAMED:{} TO {}'.format(file,newname))
            #os.rename(file,newname)

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
            
#CheckAndSort()
interests = ["Atomic","Nuclear"]
MATCHES = []
counter = 0
#fake = ['2022-04.json']
#for JSON in fake:
for JSON in CheckAndSort():
    with open(JSON, encoding='utf-8') as f:
        print("Starting search on {}".format(JSON))
        data = json.load(f)
        if len(data["response"]["docs"]) == 0:
            continue
        for article in data["response"]["docs"]:
            counter+=1
            abstract = article["abstract"]
            headline = article["headline"]["main"]
            keywords = []
            date = article["pub_date"]
            match_flag = False
            for key in article["keywords"]:
                keywords.append(key["value"])
                for interest in interests:
                    if interest in key["value"]:
                        match_flag = True
            if match_flag:
                populate = {"date":date,"headline":headline,"abstract":abstract,"keywords":keywords}
                MATCHES.append(populate)
    
print("Total articles:{}, Matching interesting keywords:{}".format(counter,len(MATCHES)))
SAVEME = {"searched":interests,"total_articles":counter,"number_matched":len(MATCHES),"matches":MATCHES}
with open('Matches.json','w',encoding='utf-8') as s:
    json.dump(SAVEME, s, ensure_ascii=False, indent=4)
    s.close()
