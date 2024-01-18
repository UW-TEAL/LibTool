from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import *


class ModelAdmin(ImportExportModelAdmin):
    list_display = ['authorKorean', 'authorEnglish', 'workTitle', 'genre', 'translator', 'sourceTitle', 'publisher', 'year']
    search_fields = ['authorKorean', 'authorEnglish', 'workTitle', 'genre', 'translator', 'sourceTitle', 'publisher', 'year', 'yearCreated', 'authorEnglish2', 'uid2']
    list_per_page = 20

admin.site.register(Record, ModelAdmin)