from django.db import models

# Create your models here.


class Location(models.Model):
    "Model stores location information in db"
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Model stores category types in db
    """
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    

class Image(models.Model):

    """
    Model that stores images in a database
    """
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='album/', default='static/landing.png')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo: {self.name} : description: {self.description} : location: {self.location.name} : category: {self.category.name}"

    def delete_photo(self):
        self.delete()

    def save_photo(self):
        self.save()
