from django.db import models
from django.contrib.auth.models import User
from PIL import Image 
# import Image
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photoprofile/",null=True,blank=True,default='default.png')
    usertype = models.CharField(max_length=100,default='member')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # saving image first
        img = Image.open(self.photo.path) # Open image using self

        if img.height > 200 or img.width > 200:
            new_img = (200, 200)
            img.thumbnail(new_img)
            # img.resize(self.photo.path, (200, 200))
            img.save(self.photo.path)  # saving image at the same path
            
    def __str__(self):
        return self.user.first_name
 
class BookProduct(models.Model):
    bookname=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=500,null=True,blank = True)
    imageurl = models.CharField(max_length=500,null=True,blank=True)
    imagefilename = models.CharField(max_length=500,null=True,blank=True)
    instock = models.BooleanField(default=True)
    unit = models.CharField(max_length=200,default='-')
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to="books/",null=True,blank=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # saving image first
        img = Image.open(self.image.path) # Open image using self

        if img.height > 260 or img.width > 171:
            new_img = (171, 260)
            img.thumbnail(new_img)
            # img.resize(self.image.path, (171, 260))
            img.save(self.image.path)  # saving image at the same path
            
    def __self__(self):
        return self.bookname

class Cart(models.Model):
    # who order
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bookid = models.CharField(max_length=100)
    bookname = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    stamp = models.DateTimeField(auto_now_add=True)
    
    def __self__(self):
        return self.stamp
    
class Employee(models.Model):
    bookname = models.CharField(max_length=50)
    emp_image = models.ImageField(upload_to='upload/')

        

class Friend(models.Model):
    # NICK NAME should be unique
    nick_name = models.CharField(max_length=100, unique =  True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    likes = models.CharField(max_length = 250)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    lives_in = models.CharField(max_length=150, null = True, blank = True)

    def __str__(self):
        return self.nick_name    