from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ManyToManyField(Category, related_name="items")
    name = models.CharField(max_length=20)
    photo = models.ImageField(default='default.jpg', blank=True, upload_to='images')
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    def __str__(self):
        return self.name



