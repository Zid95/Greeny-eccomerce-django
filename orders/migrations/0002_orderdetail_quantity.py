# Generated by Django 4.1.5 on 2023-02-02 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='quantity'),
        ),
    ]
