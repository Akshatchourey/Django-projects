from django.contrib import admin
from .models import Store

# Register your models here.

# admin.site.register(Store)

class Shope(admin.ModelAdmin):
    data_show =('proid','proname')
admin.site.register(Store, Shope)


"""@admin.register(Store)
class Shope(admin.ModelAdmin):
    data_show =('proid','proname','prodesc','protype')"""
