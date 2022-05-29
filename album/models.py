from django.db import models

# Create your models here.

class Image(models.Model):

    """
    Model that stores images in a database
    """
    name=models.CharField(max_length=60)
    description=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='album/',default='static/landing.png')

