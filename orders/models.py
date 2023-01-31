from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

ORDER_STATUS = (
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)

class Order(models.Model):
    order_code = models.CharField(_('order_code'),max_length=10)
    user = ""
    order_status = models.CharField(_('order_status'),max_length=12,choices=ORDER_STATUS,default='Recieved')
    delivery_date = models.DateTimeField(_('delivery_date'),null=True,blank=True)
    order_date = models.DateTimeField(_('order_date'),default=timezone.now)

