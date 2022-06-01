from unicodedata import category
from django.test import TestCase
from .models import Location, Category, Image

class LocationTestClass(TestCase):
    # set up method

    def setUp(self):
        self.london = Location(
            name='London')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.london, Location))

    def test_save_method(self):
        self.london.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    def test_delete_location(self):
        self.london.save_location()
        location = Location(name = "Kisumu")
        location.save_location()
        self.london.delete_location()
        loct = Location.objects.all()

        self.assertTrue(len(loct),1)



    def test_save_method(self):
        self.london.save_editor()
        loct = Location.objects.all()
        self.assertTrue(len(loct) > 0)
    

class CategoryTestClass(TestCase):
    # set up method

    def setUp(self):
        self.food = Category(
            name='Burger')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food, Category))

    def test_save_method(self):
        self.food.save_editor()
        cat = Category.objects.all()
        self.assertTrue(len(cat) > 0)
    
    def test_delete_category(self):
        self.food.save_category()
        category = Category(name = "art")
        category.save_location()
        self.food.delete_category()
        cat = Category.objects.all()

        self.assertTrue(len(cat),1)


    

class ArticleTestClass(TestCase):
    def setUp(self):
        self.loct = Location(name="Nairobi")
        self.loct.save_editor()

        self.new_category=Category(name="Food")
        self.new_category.save_editor()

        self.new_image=Image(name='Burger',description='It is delicious'
        ,photo='media/album/water.png',
        location=self.loct,category=self.new_category)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save(self):
        self.new_image.save_photo()
        images =  Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.new_image.delete_photo()
        images =  Image.objects.all()

        self.assertTrue(len(images),1)

    def test_search_image(self):
        self.new_image.search_images("Food")
        images =  Image.objects.all()

        self.assertEquals(len(images),1)

    def test_search_image(self):
        self.new_image.filter_by_location("Nairobi")
        images =  Image.objects.all()

        self.assertEquals(len(images),1)

    def test_get_image_by_id(self):
        self.new_image.save_image()
        image = Image.get_image_id(self.new_image.id)

        self.assertTrue(image)