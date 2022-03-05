import os
from os import listdir
from os.path import isfile, join
# from django.conf import settings
import json
import random
import string

# -------------------------------------------------------
# work with only file name use this one
# mypath ='../static/myapp/images/book/icon/'
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# for row in onlyfiles:
#     print(row)

# ------------------------------------------------------- 
#gen random characters for Book's Author and random number for price
# def random_author_price():
#     list1 = [6,7,8,9,10,11]
#     length = random.choice(list1)
#     price = random.randint(1000,3000)
    
#     letters = string.ascii_lowercase
#     author = string.capwords(''.join(random.choice(letters) for i in range(length)))
#     return (author,price)

# -------------------------------------------------------
#generate json file according with number of picture
# with open('../static/myapp/data/books.json', "w", encoding="utf-8") as file:
#     file.write('[ \n')
#     i=1
#     for row in onlyfiles:
#         (author,price) = random_author_price()
#         textline = '{"id":"'+str(i)+'","filename":"'+row+'","filepath":"myapp/images/book/icon/'+row+'","author":"' \
#             +author+'","price":"'+str(price)+'"},\n'
#         file.write(textline)
#         i+=1
#         # print(textline) # it print all records in the database
#     file.write(']')
                
# with open('../static/myapp/data/books.json') as f:
#     data = json.load(f)

# -------------------------------------------------------

#test json filtering, fetch record 10 per page
#dict
# dm = data[:10]
# # dm = data[10:20]
# for dx in dm: 
#     print(dx)
#     print(type(dx))

# -------------------------------------------------------
#test range to generate how many page(s), to display 10 record per page        
# x = range(1,10)
# for n in x:
#   print(n)
# print(type(data))

# -------------------------------------------------------
#this retrieve folder show fulpath, didn't good for my task
# print(myapp.static_folder)
# work with full path
# import glob
# print(glob.glob("../static/myapp/images/book/icon/*.jpg")) 
# settings.configure() 

# -------------------------------------------------------
#this another write file technique, by use dump instead write row by row as above
#but at concat text make computer hang so ignore this technique
# for write
# data = {"key": "value"}
# with open('../static/myapp/data/books.json', 'w') as jsonfile:
#     json.dump(data, jsonfile)

# for read
# with open('../static/myapp/data/books.json') as file:
#     file = json.load(file)
# print(file)    

# -------------------------------------------------------
# json member for template
# {{book.id}},{{book.price}},{{book.author}},{{book.filename}},{{book.filepath}}