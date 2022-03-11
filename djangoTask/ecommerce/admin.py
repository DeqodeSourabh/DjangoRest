from csv import list_dialects
from django.contrib import admin
from .models import  Song
# Register your models here.
# @admin.register(Singer)
# class SingerAdmin(admin.ModelAdmin):
#     list_display = ['id','name', 'gender']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'cloths']