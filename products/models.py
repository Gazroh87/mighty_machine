from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=12)
    brand = models.CharField(max_length=254)
    part_name = models.CharField(max_length=254)
    description = models.TextField()
    has_colours = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    rating = models.DecimalField(
        max_digits=3, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    part_type = models.CharField(max_length=254)

    def __str__(self):
        return self.part_name
