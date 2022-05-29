from django.db import models

# Create your models here.
class Location(models.Model):
    "Model stores location information in db"
    name=models.CharField(max_length=60)

class Category(models.Model):
    """
    Model stores category types in db
    """
    name=models.CharField(max_length=60)
class Image(models.Model):

    """
    Model that stores images in a database
    """
    name=models.CharField(max_length=60)
    description=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='album/',default='static/landing.png')
    location=models.ForeignKey(Location, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)


