from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from product.models import Product
from django.contrib.auth.models import User

ORDER_STATUS = (
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)

class Order(models.Model):
    order_code = models.CharField(_('order_code'),max_length=10)
    user = models.ForeignKey(User,verbose_name=(_('user')),related_name='user_order',on_delete=models.SET_NULL,null=True,blank=True)
    order_status = models.CharField(_('order_status'),max_length=12,choices=ORDER_STATUS,default='Recieved')
    delivery_date = models.DateTimeField(_('delivery_date'),null=True,blank=True)
    order_date = models.DateTimeField(_('order_date'),default=timezone.now)

    def __str__(self) -> str:
        return self.order_code


class OrderDetail(models.Model):
    order = models.ForeignKey(Order,verbose_name=_('order'),related_name='order_detail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,verbose_name=_('product'),related_name='order_product',on_delete=models.SET_NULL,null=True,blank=True)
    price = models.FloatField(_('price'))
    quantity = models.IntegerField(_('quantity'),default=1)
    total = models.FloatField(_('total'),null=True,blank=True)

    def __str__(self) -> str:
        return str(self.order)

    def save(self,*args, **kwargs):
        self.total = self.price * self.quantity
        super(OrderDetail,self).save(*args, **kwargs)