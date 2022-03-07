from email.policy import default
from pickle import FALSE
from django.db import models
# Create your models here.
from django.utils import timezone

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    # log_date = models.DateTimeField("date logged")
    log_date = models.CharField(max_length=100,null=FALSE,blank=FALSE)
    # name=models.CharField(max_length=100)
    # price=models.CharField(max_length=100)
    # description = models.CharField(max_length=500,null=True,blank = True)
    # imageurl = models.CharField(max_length=500,null=True,blank=True)
    # instock = models.BooleanField(default=True)
    # unit = models.CharField(max_length=200,default='-')
    # quantity = models.IntegerField(default=1)
    # image = models.ImageField(upload_to="products",null=True,blank=True)

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


class Alluser(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email = models.CharField(max_length=500,null=True,blank = True)
    password = models.CharField(max_length=500,null=True,blank=True)

    def __self__(self):
        return self.firstname

    
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
    image = models.ImageField(upload_to="products",null=True,blank=True)
    
    def __self__(self):
        return self.bookname
    
class Employee(models.Model):
    bookname = models.CharField(max_length=50)
    emp_image = models.ImageField(upload_to='upload/')

class Userregister(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
        
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