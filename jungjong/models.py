from django.db import models
import  datetime
import os
# Create your models here.

class Product(models.Model):
    pro_1 = models.CharField(max_length=50, default='none', null='none')
    pro_2 = models.CharField(max_length=50, default='none', null='none')
    pro_3 = models.CharField(max_length=50 , default='none',null='none')

    def __str__(self):
        return self.pro_1

class Product_real(models.Model):
    pro_name = models.CharField(max_length=50, default='none', null='none')
    pro_count = models.CharField(max_length=50, default='none', null='none')

    def __str__(self):
        return self.pro_name

