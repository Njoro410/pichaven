from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.


class ImageTestClass(TestCase):

    # set up method
    def setUp(self):
        self.picha = Image(name='cool pic', description='a very nice pic')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.picha, Image))

    # Testing Save Method
    def test_save_method(self):
        self.picha.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)

    def test_delete_method(self):
        self.picha.delete_image(1)
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)

    def test_update_method(self, name):
        self.picha.update_image(1, name=name)
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)


class LocationTestClass(TestCase):

    def setUp(self):
        self.location = Location(name='kimbo')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))
