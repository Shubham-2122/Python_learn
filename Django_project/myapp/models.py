from django.db import models

# Create your models here.

# class banse 

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField() #email valid
    mobile = models.PositiveIntegerField() # interer value
    remarks = models.TextField() # multip line

    def __str__(self):
        return self.name

class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.PositiveIntegerField()
    address = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.fname + " " + self.lname
