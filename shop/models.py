import email
from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', null=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.product_name


    @classmethod
    def search_by_product(cls, search_term):
        product = cls.objects.filter(product_name__icontains=search_term)
        return product

class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    email = models.EmailField
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    contact = models.IntegerField

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return self.customer_name

class Category(models.Model):
    name = models.CharField(max_length=255)

    