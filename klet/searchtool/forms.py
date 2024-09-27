from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'

class NewRecordForm(forms.ModelForm):

	GENRE = [ ('Fiction','Fiction'),
			('Poetry','Poetry'),
			('Essay','Essay'),
			('Play','Play'),
			('Graphic Novel', 'Graphic Novel'),
			("Children’s Literature","Children’s Literature"),
			('Classic_General','Classic_General'),
			('Classic_Poetry','Classic_Poetry'),
			('Classic_History','Classic_History'),
			('Classic_Folk Tale','Classic_Folk Tale'),
			('Classic_Fiction','Classic_Fiction'),
			('Misc','Misc')]
	authorKorean = forms.CharField(max_length=100, label="Name of author in Korean", widget=forms.TextInput(attrs={'class': 'form-control'}))
	authorEnglish = forms.CharField(max_length=100, label="Name of author in English", widget=forms.TextInput(attrs={'class': 'form-control'}) )
	workTitle = forms.CharField(max_length=100, label="Work title in genglish",  widget=forms.TextInput(attrs={'class': 'form-control'}))
	genre= forms.ChoiceField(choices=GENRE, required=True,  widget=forms.Select(attrs={'class': 'form-control'}))
	translator = forms.CharField(max_length=100, label="Name of Translator in English",  widget=forms.TextInput(attrs={'class': 'form-control'}))
	sourceTitle = forms.CharField(max_length=100, label="Name of Shource Title in English", required=True,  widget=forms.TextInput(attrs={'class': 'form-control'}))
	publisher = forms.CharField(max_length=100, label="Name of Publisher in English",  widget=forms.TextInput(attrs={'class': 'form-control'}))
	year = forms.CharField(max_length=100, label="Year",  widget=forms.TextInput(attrs={'class': 'form-control'}))
	other = forms.CharField(max_length=300, label="Any other additional information the approver should know",  widget=forms.Textarea(attrs={'class': 'form-control'}))
	class Meta:
		model = Record
		fields = ['authorKorean', 'authorEnglish', 'workTitle', 'genre', 'translator', 'sourceTitle', 'publisher', 'year', 'other']

