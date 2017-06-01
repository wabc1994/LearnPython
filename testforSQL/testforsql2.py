import sqlite3
conn=sqlite3.connect('test.db')
print "open database successfully"
c=conn.cursor()
c.execute("CREATE TABLE COMPANY(ID INT PRIMARY KEY  NOT NULL ,NAME TEXT NOT NULL ,AGE INT NOT NULL, ADDRESS CHAR(50),SALARY REAL)")
print "table created successuulfully"