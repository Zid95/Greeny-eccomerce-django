from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _

# Create your models here.

PRODUCT_FLAG = (
    ('Sale','Sales'),
    ('Feature','Feature'),
    ('New','New'),
)

class Product(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='products',default='default.png')
    flag = models.CharField(choices=PRODUCT_FLAG,max_length=10)
    price = models.FloatField()
    sku = models.IntegerField()
    brand = models.ForeignKey('Brand',related_name='product_brand',on_delete=models.CASCADE)
    tags = TaggableManager()
    subtitle = models.TextField(max_length=500)
    description = models.TextField(max_length=20000)

    def __str__(self) -> str:
        return self.name




class ProductImages(models.Model):
    pass

class Brand(models.Model):
    pass


class Reviews(models.Model):
    pass


