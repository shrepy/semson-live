from django.contrib import admin

# Register your models here.
from . import models
# Register your models here.
admin.site.register(models.Logins)
admin.site.register(models.ContactUs)
admin.site.register(models.Registration)
admin.site.register(models.Products)
admin.site.register(models.ProductCategory)