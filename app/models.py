from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Department(models.Model):
    department=models.CharField(max_length=180) 

class Employees(models.Model):
    name=models.CharField(max_length=180)   
    email=models.CharField(max_length=180)
    address=models.CharField(max_length=180)
    age=models.IntegerField(null=True)
    phn=models.IntegerField(null=True)
    password=models.CharField(max_length=180,null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    to_user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
class Customer(models.Model):
    name=models.CharField(max_length=180)
    email=models.CharField(max_length=180)
    address=models.CharField(max_length=180)
    age=models.IntegerField()
    phn=models.IntegerField()
    employe=models.ForeignKey(Employees, on_delete=models.CASCADE)
    password=models.CharField(max_length=180)
    to_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
class Product(models.Model):
    productName=models.CharField(max_length=180)
    stock=models.IntegerField()
    addDate=models.DateField(auto_now_add=True,null=True)
    desc=models.CharField(max_length=880)
    img=models.FileField(null=True)
    price=models.IntegerField()
    employe=models.ForeignKey(Employees, on_delete=models.CASCADE,null=True)
class Purchased(models.Model) :
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    status=models.CharField(max_length=180,null=True,default='ordered')
    date_of_purchase=models.DateField(auto_now_add=True,null=True)
