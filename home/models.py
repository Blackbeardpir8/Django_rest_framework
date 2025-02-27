from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    
class Book(models.Model):
    book_title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.FloatField( )

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()