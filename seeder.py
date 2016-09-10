from bs4 import BeautifulSoup
import requests
import collections
import csv
from mobile_codes import operators, mcc_mnc
from models import Job
import datetime

Network = collections.namedtuple('Network', ['isp', 'org', 'state'], verbose=False)

def seed_mcc_codes():
    for code in ('404', '405'):
        l = operators(code)
        print(l)
    pass

def get_ip_addresses():
    BASE_URL = 'http://tools.tracemyip.org/search--country/india:-v-:&gNr=50&gTr='

    result = []

    for i in range(0,50):
        start = (i*50)+1
        url = BASE_URL + str(start)
        print(url)
        res = requests.get(url)
        content = res.text
        result = result + parse_ip_page(content)

    uniq = set(result)
    with open('isp-db.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerow(['isp', 'org', 'state'])
        spamwriter.writerows(map(lambda x: list(x), uniq))

def parse_ip_page(content):
    result = []
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='tbsClass1')
    for row in table.find_all('tr'):
        data = row.find_all('td')
        if (len(data) !=10):
            continue
        result.append(Network(
            isp=data[2].get_text(),
            org=data[3].get_text(),
            state=data[4].get_text()
        ))

    return result

def seed_ip_addresses():
    get_ip_addresses()

def seed():
    seed_mcc_codes()
    # seed_ip_addresses()

def seed_jobs():
    d = datetime.datetime.now()
    job = Job(scheduled_on=d, site='https://thepiratebay.org', network=None, status='PENDING')
    job.save()
