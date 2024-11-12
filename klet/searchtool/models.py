from django.db import models
from django.db.models import Sum, F, FloatField
# Create your models here.
import uuid
from elasticsearch_dsl import analyzer, tokenizer


from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
class AuthorEnglish(models.Model):
	name = models.CharField(max_length=255)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	class Meta:
			verbose_name = "Author English"
			verbose_name_plural = "Author English"
	def __str__(self):
		return self.name

class Record(models.Model):
	GENRE = (('Fiction', 'Fiction'),
			('Poetry', 'Poetry'),
			('Essay', 'Essay'),
			('Play', 'Play'),
			("Children’s Literature", "Children’s Literature"),
			('Classic_General', 'Classic_General'),
			('Classic_Poetry', 'Classic_Poetry'),
			('Classic_History', 'Classic_History'),
			('Classic_Folk Tale', 'Classic_Folk Tale'),
			('Classic_Fiction', 'Classic_Fiction'),
			('Misc','Misc'))
	authorKorean = models.CharField(max_length=100, null=True, blank=True ,default="")
	authorEnglish = models.CharField(max_length=100, null=True, blank=True,default="")
	workTitle = models.CharField(max_length=100, null=True, blank=True,default="") # Translation title
	workTitleKorean = models.CharField(max_length=100, null=True, blank=True,default="")
	genre= models.CharField(max_length=200, null=True, choices=GENRE, blank=True, default=GENRE[1])
	translator = models.CharField(max_length=100, null=True, blank=True,default="")
	sourceTitle = models.CharField(max_length=100, null=True, blank=True,default="")
	publisher = models.CharField(max_length=100, null=True, blank=True,default="")
	year = models.CharField(max_length=100,null=True, blank=True, default=" ")
	yearCreated = models.FloatField(null=True, blank=True, default=00.00)
	authorEnglish2 = models.CharField(max_length=300, null=True, blank=True, default="")
	uid2 = models.CharField(max_length=100, default=uuid.uuid4)
	subjects = models.TextField(blank=True, null=True)
	summary = models.TextField(blank=True, null=True)
	InfoLink = models.CharField(max_length=100, null=True, blank=True, default="")
	ISBN_10 = models.CharField(max_length=100, null=True, blank=True, default="")
	ISBN_13 = models.CharField(max_length=100, null=True, blank=True, default="")
	author = models.ForeignKey(AuthorEnglish, on_delete=models.SET_NULL, related_name='records', null=True)


	def save(self, *args, **kwargs):
		# Custom code to run before saving the instance
		is_changed_author_english = True
		if self.pk:
			previous = Record.objects.get(pk=self.pk)
			if previous and previous.authorEnglish == self.authorEnglish:
				is_changed_author_english = False

		if is_changed_author_english:
			author_english = self.author
			if not author_english:
				author_english = AuthorEnglish.objects.create(name=self.authorEnglish)

			author_english.name = self.authorEnglish
			author_english.first_name = self.first_name_author_english(self.authorEnglish)
			author_english.last_name = self.last_name_author_english(self.authorEnglish)
			author_english.save()
			self.author_id = author_english.id
		# Call the parent class's save method
		super().save(*args, **kwargs)

	def first_name_author_english(self, full_name):
		split_name = full_name.replace('[', '').replace(']', '').split(" ")
		first_name = " ".join(split_name[1:])
		return first_name

	def last_name_author_english(self, full_name):
		split_name = full_name.replace('[', '').replace(']', '').split(" ")
		last_name = split_name[0]
		return last_name

class AddRequest(models.Model):

	GENRE = (('Fiction', 'Fiction'),
			('Poetry', 'Poetry'),
			('Essay', 'Essay'),
			('Play', 'Play'),
			("Children’s Literature", "Children’s Literature"),
			('Classic_General', 'Classic_General'),
			('Classic_Poetry', 'Classic_Poetry'),
			('Classic_History', 'Classic_History'),
			('Classic_Folk Tale', 'Classic_Folk Tale'),
			('Classic_Fiction', 'Classic_Fiction'),
			('Misc','Misc'))
	workTitleKorean = models.CharField(max_length=100, null=True, blank=True,default="")
	workTitle = models.CharField(max_length=100, null=True, blank=True,default="")
	authorKorean = models.CharField(max_length=100, null=True, blank=True ,default="")
	authorEnglish = models.CharField(max_length=100, null=True, blank=True,default="")
	translator = models.CharField(max_length=100, null=True, blank=True,default="")
	genre= models.CharField(max_length=200, null=True, choices=GENRE, blank=True, default=GENRE[1])
	sourceTitle = models.CharField(max_length=100, null=True, blank=True,default="")
	publisher = models.CharField(max_length=100, null=True, blank=True,default="")
	year = models.CharField(max_length=100,null=True, blank=True, default=" ")
	other = models.CharField(max_length=300, null=True, blank=True, default="")
	accepted = models.BooleanField(default=False, null=False)

class Users(models.Model):
	userName = models.CharField(max_length=100, null=False, blank=False )
	userPassword = models.CharField(max_length=100, null=False, blank=False )
	userEmail = models.CharField(max_length=100, null=True, blank=True, default="" )

records_index = Index('records')  # Name your index here

# Optionally configure settings for the index
records_index.settings(
    number_of_shards=1,
    number_of_replicas=1,
)


korean_analyzer =analyzer(
    'korean_analyzer',
    tokenizer="nori_tokenizer",
    type= "custom",
    filter= ["lowercase"]
)


@registry.register_document
class RecordDocument(Document):
    authorKorean = fields.TextField(analyzer=korean_analyzer, fields={
            'keyword': fields.KeywordField()
        })
    authorEnglish = fields.TextField(analyzer=korean_analyzer, fields={
            'keyword': fields.KeywordField()
        })
    workTitle = fields.TextField(analyzer=korean_analyzer, fields={
            'keyword': fields.KeywordField()
        })
    workTitleKorean = fields.TextField(analyzer=korean_analyzer, fields={
            'keyword': fields.KeywordField()
        })
    genre = fields.TextField(analyzer=korean_analyzer, fields={
            'keyword': fields.KeywordField()
        })
    translator = fields.TextField(analyzer=korean_analyzer, fields={
            'keyword': fields.KeywordField()
        })
    sourceTitle = fields.TextField(analyzer=korean_analyzer, fields={
            'keyword': fields.KeywordField()
        })
    publisher = fields.TextField(analyzer=korean_analyzer, fields={
            'keyword': fields.KeywordField()
        })
    year = fields.TextField(analyzer=korean_analyzer, fields={
            'keyword': fields.KeywordField()
        })
    id = fields.TextField(analyzer=korean_analyzer, fields={
            'keyword': fields.KeywordField()
        })  

    class Index:
        # Name of the Elasticsearch index
        name = 'records'
        # Custom settings for the index
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
            'max_ngram_diff': 5,
            'analysis': {
                'analyzer': {
                    "korean_analyzer": {
                      "type": "custom",
                      "tokenizer": "nori_tokenizer",
                      "filter": ["lowercase"]
                    }
                }
            }
        }

    class Django:
        model = Record
