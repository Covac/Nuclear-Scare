import json
import requests
from time import sleep
import datetime

def twodigit(month):
    if month < 10:
        return '0'+str(month)
    return month

last_request_timestamp = datetime.datetime.now()
API_KEY = ""
START =(1851,1)#1851
END = (2022,4)
LIMIT = 7 # 10 requests per minute MAX

print("Waiting 6 seconds before starting...")
sleep(6)

for YEAR in range(START[0],END[0]+1):
    for MONTH in range(1,12+1):
        
        if YEAR == END[0] and MONTH > END[1]:
            break
        
        samir_you_are_breaking_the_car = datetime.datetime.now()-last_request_timestamp
        if samir_you_are_breaking_the_car.seconds <= 7:
            sleep(7-samir_you_are_breaking_the_car.seconds)
            
        r = requests.get('https://api.nytimes.com/svc/archive/v1/{Y}/{M}.json?api-key={KEY}'.format(Y = YEAR, M = MONTH, KEY = API_KEY))
        last_request_timestamp = datetime.datetime.now()
        TO_DUMP = r.json()
        print(YEAR,MONTH)
        with open('{}-{}.json'.format(YEAR,twodigit(MONTH)), 'w', encoding='utf-8') as f:
            json.dump(TO_DUMP, f, ensure_ascii=False, indent=4)
            f.close()
            
