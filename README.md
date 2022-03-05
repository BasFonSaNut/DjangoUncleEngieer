# DjangoUncleEngineer

- Teamleader this project : SA
- Project : ร้านพี่ต้น
- Software Design : frontend ว่าด้วยเรื่อง data ให้ใช้ json ทั้งหมด การเข้าถึง database MYSQL ใช้สำหรบ create,update,delete เท่านั้น
- 
- Editor Vscode , database SQLITE3,MYSQL, ภาษา Python Django
- Project url output : ajaxjson.pythonanywhere.com
- learning url
- YOUTUBE:

PHASE 1 : 05-MARCH-2022

- เสร็จในส่วนของ query from json object เพื่อใช้แสดงผลในส่วนของหน้า front end 
- เขียน code จำลองว่า เมื่อวันที่ส่วน backend หาส่วนของ database เสร็จแล้ว จะสร้าง  books.json ไฟล์ => ไปวางไว้ใน folder /static ได้อย่างไร =>เมื่อสร้างได้แล้ว โยนไปวางใน folder static ได้แล้ว 
=> จะเรียกใช้งาน จาก /static/books.json ได้อย่าง 
=> จะ filtering จาก json object (dict) ได้อย่างไร
- ณ วันนี้ในวันที่ส่วน backend ยังไมไ่ด้เกิด จึงลงมติว่า การ gen json file ดังกล่าว ให้ gen จากจำนวนรูปทั้งหมด ในระบบ ไปก่อน โดย :=> เข้าไปวิ่งไล่ดู รูปภาพทั้งหมด ใน folder /static/myapp/images/book/icon => generate json object element(ฟิล์ด) เท่าที่จำเป็นใช้งานได้ ในหน้า frontend ไปก่อน ประกอบด้วย : id,author(ผู้เขียน,random),price(ราคาหนังสือ,random),filename,filelocation => เมื่อวันใดที่ส่วน database พร้อม => source ที่นำมา gen จะใช้จาก Mysql แทน
generate code :

- เพื่อ 2 เป้าหมาย : 
- 1. host free ไม่ได้ให้ความเร็วไว้สูงมากพอเทียบเท่าระดับจ่ายตังก์
- 2. ลดการเข้าถึง database โดยไม่จำเป็น
- กระบวนการคือ เมื่อ แอดมิน ทำการเพิ่มลบอัปเดต สินค้าใดๆ => เข้าไป query รายการสินค้า จาก Mysql => 
สร้าง books.json จากจำนวนเรคคอร์ดทั้งหมด ที่มีในระบบ => โยน books.json ไปไว้ที่ /static folder =>
เมื่อผู้ใช้งาน ดูสินค้า ให้เรียกใช้จาก books.json เท่านั้นไม่จำเป็นต้องวิ่งมาฝั่ง server

PHASE 1 : SOLUTION
from os import listdir
from os.path import isfile, join
import json
import random
import string

# STEP 1-------------------------------------------------------
# จับไฟล์ทั้งหมด มายัดใส่ อะเรย์รายชื่อไฟล์
mypath ='../static/myapp/images/book/icon/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# for row in onlyfiles:
#     print(row)

# STEP 2------------------------------------------------------- 
# เตรียมฟังก์ชั่นไว้ random ชื่อผู้เขียน และราคา 
def random_author_price():
    list1 = [6,7,8,9,10,11]
    length = random.choice(list1)
    price = random.randint(1000,3000)
    
    letters = string.ascii_lowercase
    author = string.capwords(''.join(random.choice(letters) for i in range(length)))
    return (author,price)

# STEP 3-------------------------------------------------------
#สร้างไฟล์ ิ books.json จำนวน row เท่าจำนวน array ของภาพ จ่าก step แรก
with open('../static/myapp/data/books.json', "w", encoding="utf-8") as file:
    file.write('[ \n')
    i=1
    for row in onlyfiles:
        (author,price) = random_author_price()
        textline = '{"id":"'+str(i)+'","filename":"'+row+'","filepath":"myapp/images/book/icon/'+row+'","author":"' \
            +author+'","price":"'+str(price)+'"},\n'
        file.write(textline)
        i+=1
    file.write(']')

# STEP 4-------------------------------------------------------
# เช็คดูว่า ไฟล์ ไปวางใน folder ที่ต้องการหรือยัง
with open('../static/myapp/data/books.json') as f:
    data = json.load(f)
    # เช็คดูว่า object เป็น dict สมตั้งใจหรือไม่
    print(type(data)) 

# STEP 5-------------------------------------------------------
# ทดสอบการ เรียกใช้งาน  json object filtering, fetch record 10 per page
dm = data[:10]
dm = data[10:20]
for dx in dm: 
    print(dx)
    print(type(dx))
-----------------------------------------------------------------------------------
- 👋 สวัสดีครับ, นี่คือ github ในนามกลุ่มของ นักเรียน ป.5 4 คน น้องบาส น้องฝน น้องสา น้องนัท
- 👀 github ตัวนี้เป้าเหมายเพื่อใช้ในการส่ง การบ้าน และ เวิร์คชอบ จากการเข้า คลาส Python bootcamp 2022 
- 🌱 ของคุณลุงวิศวะสอนคำนวน (UncleEngineering)
- 💞️ ถ้าพี่ๆ เข้ามาเพื่อหวังจะเห็น code เทพๆ บอกไว้ก่อนเลยว่า "อย่าหวัง" ครับ 
- 📫 ถ้ามีอะไรแนะนำพวกเรา comment ไว้เลยครับ เพราะกว่าพวกผมจะ ขึ้น ม.1 มีเวลาอีกเยอะ
- ✨ ต้องรีบเก็บเกี่ยวประสบการณ์ครับ เพราะเห็นแนวข้อสอบย้อนหลังเข้า ม.1 แล้วหืดจับเลย จะเป็นลม

<!---
BasFonSaNut/BasFonSaNut is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
