import csv, sqlite3
#import sqlite record from localhost to real server
  # #################image old image upload at addproduct route ##########################
        # file_image = request.FILES['imageupload']
        # file_image_name = request.FILES['imageupload'].name.replace(' ','')
        # new.imagefilename = file_image_name
        # new.imageurl = 'books/'+file_image_name
        #  ขึ้น server ../static/myapp/images/book/icon/
        # print('file_image :',file_image)
        # print('filename :',file_image_name)
        # fs = FileSystemStorage()
        # filename = fs.save(file_image_name,file_image)
        # upload_file_url = fs.url(filename)
        # # print('upload_file_url :',upload_file_url)
        # new.image = upload_file_url[6:]
        # #################end image management ##########################
# con = sqlite3.connect("../db.sqlite3") # change to 'sqlite:///your_filename.db'
# #realserver /home/ajaxjson/djangoEp2template/db.sqlite3
# cur = con.cursor()
# with open('myapp_bookproduct.csv','r',encoding="utf-8") as fin: # `with` statement available in 2.5+
#     # csv.DictReader uses first line in file for column headings by default
#     dr = csv.DictReader(fin) # comma is default delimiter
#     to_db = [(i['id'], i['bookname'],i['price'],i['author'],i['description'],i['imageurl'],i['imagefilename'],i['instock'],i['unit'],i['quantity'],i['image']) for i in dr]
# cur.executemany("INSERT INTO myapp_bookproduct (id,bookname,price,author,description,imageurl,imagefilename,instock,unit,quantity,image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
# con.commit()
# con.close()

#================update image file in database after uploate file upload location ===========
# con = sqlite3.connect("../db.sqlite3") # change to 'sqlite:///your_filename.db'
# with open('myapp_bookproduct.csv','r',encoding="utf-8", newline='\n') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     for row in spamreader:
#         print(row[10])


conn = sqlite3.connect("../db.sqlite3") # change to 'sqlite:///your_filename.db'
# #realserver /home/ajaxjson/djangoEp2template/db.sqlite3
cur = conn.cursor()
with conn:    
    cur = conn.cursor()    
    cur.execute("UPDATE myapp_bookproduct SET image = 'book/'||imagefilename")        
    
conn.close() 