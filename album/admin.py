from django.contrib import admin
from .models import Image, Location, Category
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    list_display=("name","description","location","category")
    list_filter=("location","category")


admin.site.register(Image, AlbumAdmin)
admin.site.register(Location)
admin.site.register(Category)