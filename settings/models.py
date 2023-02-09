from django.db import models



class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company')
    call_us = models.CharField(max_length=25)
    email_us = models.EmailField()
    about = models.TextField(max_length=1000)
    fb_link = models.URLField(null=True,blank=True)
    tw_link = models.URLField(null=True,blank=True)
    inst_link = models.URLField(null=True,blank=True)
    
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
