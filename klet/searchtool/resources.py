from import_export import resources
from .models import Record

class RecordResource(resources.ModelResource):
    class Meta:
        model = Record
        # Specify fields to exclude from the import
        exclude = ('id', 'yearCreated', 'authorEnglish2', 'uid2')
