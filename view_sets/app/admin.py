from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(category)
admin.site.register(products)
