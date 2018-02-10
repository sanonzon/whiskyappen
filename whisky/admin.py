from django.contrib import admin
from .models import Whisky, Rating

# Register your models here.
class whiskyAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'

admin.site.register(Whisky)
admin.site.register(Rating)