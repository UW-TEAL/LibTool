from django.db import models
from django.db.models import Sum, F, FloatField
# Create your models here.


class Record(models.Model):
	GENRE = (('Fiction', 'Fiction'),
			('Poetry', 'Poetry'),
			('Essay', 'Essay'),
			('Play', 'Play'),
			('Graphic Novel', 'Graphic Novel'),
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
	uid2 = models.CharField(max_length=100, default="Not Registered yet")
	subjects = models.TextField(blank=True, null=True)
	summary = models.TextField(blank=True, null=True)
	InfoLink = models.CharField(max_length=100, null=True, blank=True, default="")
	ISBN_10 = models.CharField(max_length=100, null=True, blank=True, default="")
	ISBN_13 = models.CharField(max_length=100, null=True, blank=True, default="")



class AddRequest(models.Model):
	requestid = models.CharField(max_length=100, null=True, blank=True ,default="")
	accepted = models.BooleanField(default=False, null=False)

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
	workTitle = models.CharField(max_length=100, null=True, blank=True,default="")
	genre= models.CharField(max_length=200, null=True, choices=GENRE, blank=True, default=GENRE[1])
	translator = models.CharField(max_length=100, null=True, blank=True,default="")
	sourceTitle = models.CharField(max_length=100, null=True, blank=True,default="")
	publisher = models.CharField(max_length=100, null=True, blank=True,default="")
	year = models.CharField(max_length=100,null=True, blank=True, default=" ")
	yearCreated = models.FloatField(null=True, blank=True, default=00.00)
	authorEnglish2 = models.CharField(max_length=300, null=True, blank=True, default="")
	uid2 = models.CharField(max_length=100, default="Not Registered yet")
	other = models.CharField(max_length=300, null=True, blank=True, default="")
	subjects = models.TextField(blank=True, null=True) 
	summary = models.TextField(blank=True, null=True)

class Users(models.Model):
	userName = models.CharField(max_length=100, null=False, blank=False )
	userPassword = models.CharField(max_length=100, null=False, blank=False )
	userEmail = models.CharField(max_length=100, null=True, blank=True, default="" )