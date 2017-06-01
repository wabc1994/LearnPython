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
#access the elements of each row using the row headers for row['Symbol'],  or row['change']
with open('stock.csv') as f:
    f_csv=csv.DictReader(f)
    for row in f_csv:
        print row['Symbol']
    #show how to write csv data,
headers=[('Symbol','price','Date','Time','Change','Volume')]
rows=[('aa',39.48,'6/11/2007','9:36am',-0.18,181800),('bb',39.48,'6/11/2007','9:36am',-0.18,181800)]
with open('stocks.csv','w') as f:
    f_csv=csv.writer(f)
    f_csv.writerows(headers)
    f_csv.writerows(rows)
#如何向文本中写入字典形式
headers=['Symbol','Price','Date','Time','Change','Volume']
rows=[{'Symbol':'AA','Price':39.48,'Date':'6/11/2007','Time':'9:36am','Change':-0.18,'Volume':1818000},
      {'Symbol':'AA','Price':39.48,'Date':'6/11/2007','Time':'9:36am','Change':-0.18,'Volume':1818000},]
with open('stockdic.cvs','w') as f:
    f_csv=csv.DictWriter(f,headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
