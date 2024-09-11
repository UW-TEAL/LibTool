from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import *
from .resources import RecordResource


class ModelAdmin(ImportExportModelAdmin):
    resource_class = RecordResource
    list_display = ['workTitle', "workTitleKorean", 'authorKorean', 'authorEnglish', 'translator', 'sourceTitle', 'publisher', 'year', 'genre', 'subjects', 'summary', 'InfoLink', 'ISBN_10', 'ISBN_13']
    search_fields = ['authorKorean', 'authorEnglish', 'workTitle', 'genre', 'translator', 'sourceTitle', 'publisher', 'year', 'yearCreated', 'authorEnglish2', 'uid2','subjects', 'summary','ISBN_10', 'ISBN_13']
    exclude = ('id', 'yearCreated', 'authorEnglish2', 'uid2', 'author')

    list_per_page = 20

    def get_list_display_links(self, request, list_display):
        # This method allows you to specify which fields in the list_display should be clickable.
        # You can return a tuple or list of field names from list_display that you want to be clickable.
        # For example, to make 'authorEnglish' and 'workTitle' clickable:
        return ('authorKorean', 'authorEnglish', 'workTitle', 'genre', 'translator', 'sourceTitle', 'publisher', 'year', 'subjects', 'summary', 'InfoLink', 'ISBN_10', 'ISBN_13')

admin.site.register(Record, ModelAdmin)