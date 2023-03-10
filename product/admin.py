from django.contrib import admin
from .models import *

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    list_display= ['id','name','brand','price']
    list_filter = ['brand','price']
    inlines = [ProductImagesAdmin]
    search_fields = ['name','subtitle','description']
    list_editable = ['name','brand','price']



class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user','product','rate','comment','created_at']
    list_filter = ['rate','created_at']
    search_fields = ['user','product','comment']


admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Reviews,ReviewAdmin)