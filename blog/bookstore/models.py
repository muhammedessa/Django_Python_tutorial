from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=190, null=True)
    email = models.CharField(max_length=190, null=True)
    phone = models.CharField(max_length=190, null=True)
    age = models.CharField(max_length=190, null=True)
    avatar = models.ImageField(blank=True, null=True, default="preson.png")
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name



class Tag(models.Model):
    name = models.CharField(max_length=190, null=True)

    def __str__(self):
       return self.name


class Book(models.Model):
    CATEGORY = (
        ('Classics','Classics'),
        ('Comic Book','Comic Book'),
        ('Fantasy','Fantasy'),
        ('Horror','Horror')
    )
    name = models.CharField(max_length=190, null=True)
    author = models.CharField(max_length=190, null=True)
    price = models.FloatField( null=True)
    category = models.CharField(max_length=190, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
         return self.name





class Order(models.Model):
    STATUS= (
        ('Pending','Pending'),
        ('Delivered','Delivered'),
        ('in progress','in progress'),
        ('out of order','out of order')
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status =  models.CharField(max_length=200, null=True,choices=STATUS)