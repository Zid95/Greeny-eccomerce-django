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
    name = models.CharField(_('name'),max_length=150)
    image = models.ImageField(_('image'),upload_to='products/',default='default.png')
    flag = models.CharField(_('flag'),max_length=10,choices=PRODUCT_FLAG)
    price = models.FloatField(_('price'))
    sku = models.IntegerField(_('sku'))
    brand = models.ForeignKey('Brand',verbose_name=_('brand'),related_name='product_brand',on_delete=models.CASCADE)
    tags =  TaggableManager()
    subtitle = models.TextField(_('subtitle'),max_length=500)
    description = models.TextField(_('description'),max_length=20000)
    slug = models.SlugField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name




class ProductImages(models.Model):
    pass

class Brand(models.Model):
    pass


class Reviews(models.Model):
    pass


