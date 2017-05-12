#encoding:utf-8
import csv
with open('stock.csv') as f:
    f_csv=csv.reader(f)
    #headers=next(f_csv)取走第一行column headers
    headers=next(f_csv)
    print headers
    for row in f_csv:
       print row[0]
from collections import namedtuple
with open('stock.csv') as f:
     f_csv=csv.reader(f)
     headings=next(f_csv)

     Row=namedtuple('Row',headings)
     for r in f_csv:
         row=Row(*r)
         print row.Symbol
stockset=['time','value','future']
stock=namedtuple('stock',stockset)
dataset=['2017.2.3','999yuan','yes']
row=stock(*dataset)
print row.time