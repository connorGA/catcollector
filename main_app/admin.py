from django.contrib import admin

from .models import Cat, Dog

# Register your models here.
admin.site.register(Cat)
admin.site.register(Dog)