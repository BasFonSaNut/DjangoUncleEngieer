import json
import os
from os import listdir
from os.path import isfile, join
import sqlite3
import random
import string
#run manual via python terminal
#cd E:\PythonUncleWorkshop\Django\DjangoUncleEngieer\djangoEp2template\myapp>
#เปิดไฟล์ json
# with open('../static/myapp/data/books.json') as f:
#      jsondata = json.load(f)
#      # ขึ้นระบบจริงใช้ real path '/home/ajaxjson/djangoEp2template/static/myapp/data/books.json
     
# #เตรียม function เพื่อ random value มายัดใส่ ฟิล์ดที่่ขาดข้อมูล
# def randomfunction():
#     instock = random.getrandbits(1) 
#     quantity = random.randint(3, 10)
#     list1 = [3,4,5,6]    
#     length = random.choice(list1)
#     letters = string.ascii_lowercase
#     author = string.capwords(''.join(random.choice(letters) for i in range(length)))
#     author = author+' '+string.capwords(''.join(random.choice(letters) for i in range(length)))
#     WORDS = ("เล่ม", "ลัง")
#     unit = random.choice(WORDS)
#     return (instock,author,unit,quantity)

# #เริ่มกระบวนการสร้าง เรคคอร์ดลง database ตามจำนวนรูปที่มีในระบบ
# #copy db.sqlite3 จากข้างนอกมาใส่ไว้ใน myapp folder ก่อน กรณีอยากรัน แมนนวล 
# conn = sqlite3.connect('db.sqlite3')
# print("เปิดฐานข้อมูลสำเร็จ")

# for item in jsondata:
#     instock =0 
#     author =''
#     unit=''
#     quantity = 0
#     (instock,author,unit,quantity) = randomfunction()

#     conn.execute("INSERT INTO myapp_bookproduct(id,bookname,author,price,instock,unit,quantity,imageurl,imagefilename) \
#     VALUES (?,?,?,?,?,?,?,?,?)",(item['id'],item['author'],author,item['price'],instock,unit,quantity,item['filepath'],item['filename']))
   
#     conn.commit()
#     print("เพิ่มระเบียงข้อมูลสำเร็จ")
# conn.close() 


#gen json text จาก database
conn = sqlite3.connect('db.sqlite3')
print("เปิดฐานข้อมูลสำเร็จ")
jsontext="[ \n"
with conn:    
    cur = conn.cursor()    
    cur.execute("SELECT id,bookname,author,price,instock,unit,quantity,imageurl,imagefilename FROM myapp_bookproduct order by id")
    rows = cur.fetchall()
    for row in rows:
        data =  {
        "id": row[0], 
        "bookname": row[1], 
        "author": row[2],
        "price": row[3],
        "instock": str(row[4]),
        "unit" : row[5],
        "quantity": str(row[6]),
        "imageurl":row[7],
        "imagefilename":row[8]
        }
        # print(data)
        json_format = json.dumps(data,ensure_ascii=False).encode('utf8')
        jsontext = jsontext + json_format.decode()+',\n'
jsontext=jsontext+']'        
# print(jsontext)    
conn.close() 
#writ json text to file
with open('../static/myapp/data/books.json',"w", encoding="utf-8") as f:
    f.write(jsontext)
f.close()

