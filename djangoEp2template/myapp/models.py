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
        return self.name
    
class Allproduct(models.Model):
    name=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    description = models.CharField(max_length=500,null=True,blank = True)
    imageurl = models.CharField(max_length=500,null=True,blank=True)
    instock = models.BooleanField(default=True)
    unit = models.CharField(max_length=200,default='-')
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to="products",null=True,blank=True)
    
    def __self__(self):
        return self.name
    
    
class BookProduct(models.Model):
    name=models.CharField(max_length=100)
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
        return self.name
    
class Employee(models.Model):
    name = models.CharField(max_length=50)
    emp_image = models.ImageField(upload_to='upload/')
    
class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    img = models.ImageField(upload_to = "images/")
 
    def __str__(self):
        return self.title    