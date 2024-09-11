from django.core.management.base import BaseCommand
from searchtool.models import AuthorEnglish, Record

class Command(BaseCommand):
    help = 'Import AuthorEnglish data'

    def handle(self, *args, **options):
        records = Record.objects.all()

        for record in records:
            # Strip the authorEnglish name and find or create an AuthorEnglish instance
            if record.authorEnglish and record.authorEnglish.strip():
              author_name = record.authorEnglish.strip()
              author, created = AuthorEnglish.objects.get_or_create(name=author_name)

              if created:
                  
                  # Assign first and last names
                  author.first_name = record.first_name_author_english(author.name)
                  author.last_name = record.last_name_author_english(author.name)
                  
                  # Save the author instance
                  author.save()

              # Update the record with the author's id
              record.author_id = author.id
              record.save()

              print(f">>>>>> Update Record {record.id}")