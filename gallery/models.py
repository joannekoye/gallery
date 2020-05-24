from django.db import models

class Location(models.Model):
    location = models.CharField(max_length=30)

class Category(models.Model):
    category = models.CharField(max_length=30)

class Image(models.Model):
    img_path = models.ImageField(upload_to= 'images/')
    img_name = models.CharField(max_length=30)
    img_desc = models.TextField(blank=True)
    img_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    img_category = models.ForeignKey(Category, on_delete=models.CASCADE)
