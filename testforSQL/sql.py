import sqlite3
db = sqlite3.connect('example.db')
c=db.cursor()
#c.execute('create table stocks(date text,trans integer,symbol real,qty real,price real)')
#c.execute("INSERT INTO stocks VALUES ('2017-05-13','BUY','rhat',100,35.14)")
#db.commit()
#db.close()
#never do this
symbol='rhat'
print c.execute('SELECT * FROM stocks WHERE symbol="%s"' %symbol)

t=('rhat',)
c.execute("SELECT *FROM stocks WHERE symbol=?",t)
print c.fetchone()
purchases=[('2006-03-28','BUY','IBM',1000,45.00),('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)',purchases)
for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print row
c.executescript("""
    create table huamabn(firstname,lastname,age);
    create table book1(title,author,published);
    insert into book(title,author,published)
    VALUES ('dliuxiongcheng book','asg',1987);
""")