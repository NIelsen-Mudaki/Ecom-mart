import datetime
import email
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1, null=True )

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.product_name

    @classmethod
    def search_by_product(cls, search_term):
        product = cls.objects.filter(product_name__icontains=search_term)
        return product
    @classmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @classmethod
    def get_all_products():
        return Product.objects.all()

    @classmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

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

    def register(self):
        self.save()

    @classmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False

class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField
    address = models.CharField(max_length=255)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'orders'

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Orders.objects.filter(customer=customer_id).order_by('-date')