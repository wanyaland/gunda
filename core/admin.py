from django.contrib import admin
from core.models import Album,Profile,Genre,Track

# Register your models here.

admin.site.register(Album)
admin.site.register(Genre)
admin.site.register(Track)