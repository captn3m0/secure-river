import csv
import os

data = dict()

file = os.path.dirname(os.path.abspath(__file__)) + '/mcc.csv'

with open(file) as csvfile:
  reader = csv.DictReader(csvfile, restkey='data')
  for row in reader:
      data[(int(row['mcc']), int(row['mnc']))] = row

class MCC(object):
  @staticmethod
  def get_mcc_details(mcc,mnc):
    return data[(mcc, mnc)]
