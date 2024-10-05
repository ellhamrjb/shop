from django.contrib import admin
from .models import Category,Product



class ProductAdmin(admin.ModelAdmin):
    list_display=['name','category','price','stock']
    list_filter=['category']
    

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)

