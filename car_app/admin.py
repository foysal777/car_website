from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.CarModel)
admin.site.register(models.BrandModel)
admin.site.register(models.CommentModel)