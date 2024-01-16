from django.contrib import admin

# Register your models here.
from .models import *

class ModelAdmin(admin.ModelAdmin):
    list_display = ['authorKorean', 'authorEnglish', 'workTitle', 'genre', 'translator', 'sourceTitle', 'publisher', 'year', 'yearCreated', 'authorEnglish2', 'uid2']
    list_filter = ['authorKorean', 'authorEnglish', 'workTitle', 'genre', 'translator', 'sourceTitle', 'publisher', 'year', 'yearCreated', 'authorEnglish2', 'uid2']
    search_fields = ['authorKorean', 'authorEnglish', 'workTitle', 'genre', 'translator', 'sourceTitle', 'publisher', 'year', 'yearCreated', 'authorEnglish2', 'uid2']
    list_per_page = 10

admin.site.register(Record)