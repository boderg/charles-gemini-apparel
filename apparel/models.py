from django.db import models


# Colour model
class Colour(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Size model
class Size(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Categories model
class Category(models.Model):
    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# Products model
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    category = models.ManyToManyField(Category, blank=True)
    colours = models.ManyToManyField(Colour, blank=True)
    sizes = models.ManyToManyField(Size, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    # Discounts
    discount = models.BooleanField(default=False)
    discount_price = models.DecimalField(
        default=0, max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
