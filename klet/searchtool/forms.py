from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Record, AddRequest

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'

class NewRecordForm(forms.ModelForm):

	GENRE = [ ('Fiction','Fiction'),
			('Poetry','Poetry'),
			('Essay','Essay'),
			('Play','Play'),
			("Children’s Literature","Children’s Literature"),
			('Classic_General','Classic_General'),
			('Classic_Poetry','Classic_Poetry'),
			('Classic_History','Classic_History'),
			('Classic_Folk Tale','Classic_Folk Tale'),
			('Classic_Fiction','Classic_Fiction'),
			('Misc','Misc')]
	workTitle = forms.CharField(max_length=100, label="Translation Title in English", required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))
	workTitleKorean = forms.CharField(max_length=100, label="Title in Korean", required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))      
	authorKorean = forms.CharField(max_length=100, label="Author Name(s) in Korean", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
	authorEnglish = forms.CharField(max_length=100, label="Author Name(s) in English", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}) )
	translator = forms.CharField(max_length=100, label="Translator Name(s)", required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))

	genre= forms.ChoiceField(choices=GENRE, required=True,  widget=forms.Select(attrs={'class': 'form-control'}))
	sourceTitle = forms.CharField(max_length=100, label="Source Title in English", required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))
	publisher = forms.CharField(max_length=100, label="Publisher", required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))
	year = forms.CharField(max_length=100, label="Publication Year", required=False,  widget=forms.TextInput(attrs={'class': 'form-control'}))
	other = forms.CharField(max_length=300, label="Additional Information", required=False,  widget=forms.Textarea(attrs={'class': 'form-control'}))
	class Meta:
		model = AddRequest
		fields = ['authorKorean', 'authorEnglish', 'workTitle', 'workTitleKorean', 'genre', 'translator', 'sourceTitle', 'publisher', 'year', 'other']

