# Generated by Django 4.1.5 on 2023-03-11 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_cart_cart_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartdetail',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='price'),
        ),
    ]