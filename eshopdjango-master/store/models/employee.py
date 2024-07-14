from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/',default=None)


class MyModel(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/',default=None)
