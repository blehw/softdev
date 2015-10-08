import sqlite3
import csv

conn = sqlite3.connect("demo.db")
c = conn.cursor()

BASE = "INSERT INTO people VALUES%(name)s,%(age)s,%(id)s"
for l in csv.DictReader(open("people.csv"));
    q=BASE%l
    print q
    c.execute(q)

    
