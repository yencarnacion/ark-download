#!/usr/bin/env python3

import urllib.request
from datetime import datetime, timedelta

download_dir="./data"

# https://ark-funds.com/investor-resources
arkk = { 'url': 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv', 'name': 'arkk'}
arkq = { 'url': 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_AUTONOMOUS_TECHNOLOGY_&_ROBOTICS_ETF_ARKQ_HOLDINGS.csv', 'name': 'arkq'}
arkw = { 'url': 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_NEXT_GENERATION_INTERNET_ETF_ARKW_HOLDINGS.csv', 'name': 'arkw'}
arkg = { 'url': 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_GENOMIC_REVOLUTION_MULTISECTOR_ETF_ARKG_HOLDINGS.csv', 'name': 'arkg'}
arkf = { 'url': 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_FINTECH_INNOVATION_ETF_ARKF_HOLDINGS.csv', 'name': 'arkf'}
prnt = { 'url': 'https://ark-funds.com/wp-content/fundsiteliterature/csv/THE_3D_PRINTING_ETF_PRNT_HOLDINGS.csv', 'name': 'prnt'}
izrl = { 'url': 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_ISRAEL_INNOVATIVE_TECHNOLOGY_ETF_IZRL_HOLDINGS.csv', 'name': 'izrl'}

etfs = [arkk, arkq, arkw, arkg, arkf, prnt, izrl]


###
now = datetime.now()
start_date = None
end_date = None

d = now

mm = str(d.month).zfill(2)

dd = str(d.day).zfill(2)

yyyy = str(d.year)

hour = str(d.hour).zfill(2)

mi = str(d.minute).zfill(2)

ss = str(d.second).zfill(2)

#print( mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)

yesterday_s = None
yesterday_1_s = None

if int(hour) >= 19:
    yesterday_s = yyyy+mm+dd

    yesterday_1 = d - timedelta(1)
    mm = str(yesterday_1.month).zfill(2)
    dd = str(yesterday_1.day).zfill(2)
    yyyy = str(yesterday_1.year)
    yesterday_1_s = yyyy+mm+dd

else:
    yesterday = d - timedelta(1)
    mm = str(yesterday.month).zfill(2)
    dd = str(yesterday.day).zfill(2)
    yyyy = str(yesterday.year)
    yesterday_s = yyyy+mm+dd
    
    yesterday_1 = d - timedelta(2)
    mm = str(yesterday_1.month).zfill(2)
    dd = str(yesterday_1.day).zfill(2)
    yyyy = str(yesterday_1.year)
    yesterday_1_s = yyyy+mm+dd
    
    #print("from " + yesterday_s + " to " + yesterday_1_s)
    start_date = yesterday_1_s
    end_date = yesterday_s
    

operating_date = yesterday_s

# Download the file from `url` and save it locally under `file_name`:
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

for e in etfs:
    file_name = f"{operating_date}-{e['name']}.csv"
    urllib.request.urlretrieve(e['url'], download_dir+"/"+file_name)
