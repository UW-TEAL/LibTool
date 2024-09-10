import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter
from django import forms
from .models import *

class RecordFilter(django_filters.FilterSet):
	authorEnglish2 = CharFilter(label='Author Name (Eng)',field_name='authorEnglish2', lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-group'}))
	authorKorean  = CharFilter(label='Author Name (Korean)',field_name='authorKorean', lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-group'}))
	workTitle  = CharFilter(label='Translation Title',field_name='workTitle', lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-group'}))
	workTitleKorean  = CharFilter(label='Korean Title',field_name='workTitleKorean', lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-group'}))
	translator  = CharFilter(label='Translator',field_name='translator', lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-group'}))
	publisher = CharFilter(label='Publisher',field_name='publisher', lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-group'}))
	sourceTitle  = CharFilter(label='Source Title',field_name='sourceTitle', lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-group'}))
	start_date  = NumberFilter(label='From Published Year',field_name='yearCreated', lookup_expr='gte',widget=forms.TextInput(attrs={'class': 'form-group'}))
	end_date  = NumberFilter(label='To Published Year',field_name='yearCreated', lookup_expr='lte',widget=forms.TextInput(attrs={'class': 'form-group'}))
	year  = NumberFilter(label='Published Year =',field_name='yearCreated', lookup_expr='icontains',widget=forms.TextInput(attrs={'class': 'form-group'}))
	# Year  = NumberFilter(field_name='yearCreated', lookup_expr='iexact',widget=forms.TextInput(attrs={"max_length":"100","style":"width:450px;margin-left:25px;margin-right:25px;margin-top:10px"}))
	class Meta:
		model = Record
		fields = ['authorEnglish2','authorKorean','workTitle', 'workTitleKorean', 'translator', 'start_date', 'end_date', 'year', 'sourceTitle', 'genre']
