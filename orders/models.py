from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from product.models import Product
from django.contrib.auth.models import User
from utils.generate_code import generate_code

ORDER_STATUS = (
    ("Recieved", "Recieved"),
    ("Processed", "Processed"),
    ("Shipped", "Shipped"),
    ("Delivered", "Delivered"),
)


class Order(models.Model):
    order_code = models.CharField(_("order_code"), max_length=10, default=generate_code)
    user = models.ForeignKey(
        User,
        verbose_name=(_("user")),
        related_name="user_order",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    order_status = models.CharField(
        _("order_status"), max_length=12, choices=ORDER_STATUS, default="Recieved"
    )
    delivery_date = models.DateTimeField(_("delivery_date"), null=True, blank=True)
    order_date = models.DateTimeField(_("order_date"), default=timezone.now)

    def __str__(self) -> str:
        return self.order_code


class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name=_("order"),
        related_name="order_detail",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        verbose_name=_("product"),
        related_name="order_product",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    price = models.FloatField(_("price"))
    quantity = models.IntegerField(_("quantity"), default=1)
    total = models.FloatField(_("total"), null=True, blank=True)

    def __str__(self) -> str:
        return str(self.order)

    def save(self, *args, **kwargs):
        self.total = self.price * self.quantity
        super(OrderDetail, self).save(*args, **kwargs)


CART_STATUS = (
    ("Inprogress", "Inprogress"),
    ("Completed", "Completed"),
)


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=(_("user")),
        related_name="user_cart",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    cart_status = models.CharField(
        _("cart_status"), max_length=12, choices=CART_STATUS, default="Inprogress"
    )

    def __str__(self) -> str:
        return str(self.user)

    def cart_total(self):
        total = 0
        for product in self.cart_detail.all():
            total += product.total
        return round(total, 2)


class CartDetail(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name=_("cart_detail"),
        related_name="cart_detail",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        verbose_name=_("cart_product"),
        related_name="cart_product",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    price = models.FloatField(_("price"), null=True, blank=True)
    quantity = models.IntegerField(_("quantity"), default=1)
    total = models.FloatField(_("total"), null=True, blank=True)

    def __str__(self) -> str:
        return str(self.cart)

    # def save(self, *args, **kwargs):
    #     self.total = round(self.price * self.quantity, 2)
    #     super(CartDetail, self).save(*args, **kwargs)
