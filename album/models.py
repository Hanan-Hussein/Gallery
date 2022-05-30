from django.db import models

# Create your models here.


class Location(models.Model):
    "Model stores location information in db"
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_location(self):
        """
        saves location
        """
        self.save()

    def delete_location(self):
        """
        deletes location
        """
        self.delete()

    def update_location(self, name):
        """
        updates location
        """
        self.update(name=name)


class Category(models.Model):
    """
    Model stores category types in db
    """
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_category(self):
        """
        saves category
        """
        self.save()

    def delete_category(self):
        """
        deletes category
        """
        self.delete()

    def update_category(self, name):
        """
        updates category
        """
        self.update(name=name)

   

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
        """Deletes a photo"""
        self.delete()

    def save_photo(self):
        """Saves image"""
        self.save()

    def get_image_id(id):
        """
        fetch image by id
        """
        Image.objects.all().filter(id=id).first()

    @classmethod
    def search_image(cls, category):
        """
        search for an image by category
        """
        img = cls.objects.filter(category__name=category)
        return img

    @classmethod
    def filter_by_location(cls, location):
        """
        Filter the images by location
        """
        img = cls.objects.filter(location__name=location)
        return img
