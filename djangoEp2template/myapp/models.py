from email.policy import default
from pickle import FALSE
from pyexpat import model
from django.db import models
# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
#load image libray PiL to resize uploaded image
from PIL import Image 
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
    
class Employee(models.Model):
    bookname = models.CharField(max_length=50)
    emp_image = models.ImageField(upload_to='upload/')

    
class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    # log_date = models.DateTimeField("date logged")
    log_date = models.CharField(max_length=100,null=FALSE,blank=FALSE)
    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
        
class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    img = models.ImageField(upload_to = "images/")
 
    def __str__(self):
        return self.title    

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