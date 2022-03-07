import csv, sqlite3
#import sqlite record from localhost to real server
con = sqlite3.connect("/home/ajaxjson/djangoEp2template/db.sqlite3") # change to 'sqlite:///your_filename.db'
cur = con.cursor()
with open('myapp_bookproduct.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['id'], i['bookname'],i['price'],i['author'],i['description'],i['imageurl'],i['imagefilename'],i['instock'],i['unit'],i['quantity'],i['image']) for i in dr]

cur.executemany("INSERT INTO myapp_bookproduct (id,bookname,price,author,description,imageurl,imagefilename,instock,unit,quantity,image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()