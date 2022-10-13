from django.contrib import admin

from .models import Blog, Tag, Trader

# Register your models here.
admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Trader)