from django.contrib import admin

# Register your models here.
from . models import *

admin.site.register(BrandsModel)
admin.site.register(CategoriesModel)
admin.site.register(ProductsModel)