from django.shortcuts import render
import pandas as pd
import re
from .models import *
from .filters import *
import uuid
import numpy
from .forms import *
from django.http import HttpResponse
import openpyxl
from django.db.models import Q
from itertools import groupby
from operator import attrgetter
from django.http import JsonResponse
from .datatable import SearchToolDataTable
from .forms import *
# Create your views here.

def home(request):
    return render(request,'home.html')

def search(request):

    records = Record.objects.all().order_by('authorEnglish')
    namesKr = []
    for i in records:
        if i.authorKorean  and i.authorKorean!= "nan":
            namesKr.append(i.authorKorean)
    newNamesKr = [*set(namesKr)]
    newNamesKr.sort()
    newNamesKr = [i for a,i in enumerate(newNamesKr) if i!=' ']

    author_englishs = (
        AuthorEnglish.objects
        .order_by('last_name', 'first_name')            # Order by 'last_name'
        .distinct()                       # Remove duplicates
        .filter(name__isnull=False)       # Filter out empty names
        .filter(name__gt='')              # Filter out empty strings
    )

    grouped = {k: list(v) for k, v in groupby(author_englishs, key=attrgetter('last_name'))}

    newNamesEng = []
    for last_name, group in grouped.items():
        seen_names = set()

        for person in group:
            normalized = normalize_name(person.first_name)
            if (normalized not in seen_names):
                seen_names.add(normalized)
                newNamesEng.append(person.name)


    myFilter = RecordFilter(request.GET, queryset = records)
    filters = {}
    filter_criteria = request.GET
    for i in filter_criteria:
        filters[i] = filter_criteria[i]
    filters = {k: v for k, v in filters.items() if v}
    print(filters)

    requestForm = NewRecordForm()
    
    context = {'myFilter':myFilter, 'NamesEng':newNamesEng,'NamesKr':newNamesKr, 'Filters':filters, 'is_request_params_empty': not bool(request.GET), 'requestForm': requestForm}
    return render(request,'search.html',context)


def datatable_records(request):
    total_records, data = SearchToolDataTable(request.GET).reponse_data()
    return JsonResponse({
        'draw': int(request.GET.get('draw', 0)),
        'recordsTotal': total_records,
        'recordsFiltered': total_records,
        'data': data
    })


def generateAuthorLinks(names):
    for i in names:
        print(i)
    return 0

def normalize_name(name):
    return re.sub(r'[\s-]', '', name)

def populateDatabase(request):
    df1 = pd.read_csv('/Users/hrithik/Desktop/PC/UofW/work/new/LibTool/klet/searchtool/data/Updates1_WithAlterNames.csv')
    GENRE = (('Fiction'),
			('Poetry'),
			('Essay'),
			('Play'),
			("Children’s Literature"),
			('Classic_General'),
			('Classic_Poetry'),
			('Classic_History'),
			('Classic_Folk Tale'),
			('Classic_Fiction'),
			('Misc'),
            ('Graphic Novel'))
    GenreDict = {'Fiction':0,
			'Poem': 1,
            'Poetry': 1,
			'Essay': 2,
			'Play':3,
			'Children':4,
			'Classic/General':5,
			'Classic/Poem': 6,
			'Classic/History':7,
			'Classic/Folk Tale':8,
			'Classic/Fiction':9,
            'Misc.':10,
            'Misc':10,
            'Graphic Novel':11,
            'Classic Fiction':9,
            'Children’s Literature':4,
            'Classic_Fiction':9}
    for dbframe in df1.itertuples():
        obj = Record.objects.create(genre= GENRE[GenreDict[dbframe.GENRE]],authorEnglish = dbframe.authorEnglish, authorKorean = dbframe.authorKorean, 
        workTitle = dbframe.workTitle, translator = dbframe.translator, sourceTitle = dbframe.sourceTitle, workTitleKorean = dbframe.workTitleKorean,
        publisher = dbframe.publisher, yearCreated = dbframe.yearCreated, authorEnglish2 = dbframe.authorEnglish2, year= populateYear(str(dbframe.yearCreated)), uid2 = str(uuid.uuid4()))
        obj.save()
    context = {'message':"Populating database completed"}
    return render(request, 'message.html', context)

def deleteDatabase(request):
    records = Record.objects.all()
    records.delete()
    context = {'message':"deleting the whole database completed"}
    return render(request, 'message.html', context)

def populateYear(yearint):
    year = str(yearint).replace(".0","")
    return year

def updateYear(request):
    records = Record.objects.all()
    context = {'message':"Changes years greater than 4 digits and adds ."}
    for i in records:
        year = i.year
        if len(year) > 4 and year.find('.') == -1:
            i.year = i.year[:len(i.year)-1]+'.'+i.year[len(i.year)-1:]
            i.save()
    return render(request, 'message.html', context)

def populateAlternateNames(request):
    records = Record.objects.all()
    context = {'message':"Populating alternate names in eglish2 for all the records"}
    authors = {}
    for i in records:
        if i.authorKorean != "" or i.authorKorean != "nan" or not i.authorKorean:
            authors[i.authorKorean] = [i.authorEnglish2]
            for j in records:
                if j.authorKorean != "" or j.authorKorean != "nan" or not j.authorKorean:
                    if i.authorKorean == j.authorKorean and i.authorEnglish != j.authorEnglish:
                        authors[i.authorKorean].append(j.authorEnglish2)
                        authors[i.authorKorean] = list(set(authors[i.authorKorean]))
    for i in records:
        if (i.authorKorean != "nan" and i.authorKorean != "" and i.authorKorean != " "):
            i.authorEnglish2 = i.authorEnglish2 + ",".join(authors[i.authorKorean])
            print(i.authorKorean+" : "+i.authorEnglish2)
            i.save()
    return render(request, 'message.html', context)

def changeAnything(request):
    records = Record.objects.all()
    context = {'message': 'Changing u˘ with ŭ and o˘ with ŏ'}
    for i in records:
        i.authorEnglish = i.authorEnglish.replace("u˘","ŭ")
        i.authorEnglish2 = i.authorEnglish2.replace("u˘","ŭ")
        i.authorEnglish = i.authorEnglish.replace("o˘","ŏ")
        i.authorEnglish2 = i.authorEnglish2.replace("o˘","ŏ")
        i.save()
    return render(request, 'message.html', context)

def adminLogin(request):
    context = {'message': 'Admin Portal in making'}
    return render(request, 'admin.html', context)

def export_selected_to_excel(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids')
        records = Record.objects.filter(id__in=selected_ids)
        
        # Create an Excel workbook and sheet
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = 'Selected Records'

        # Add headers to the Excel sheet
        headers = ['Translation Title', 'Korean Title', 'Author (Kor)', 'Author (Eng)', 'Translator', 'Source', 'Publisher', 'Year', 'Genre']
        sheet.append(headers)

        # Add data rows to the Excel sheet
        for record in records:
            row = [record.workTitle, record.workTitleKorean, record.authorKorean, record.authorEnglish, record.translator, record.sourceTitle, record.publisher, record.year, record.genre]
            sheet.append(row)

        # Set HTTP response with Excel file
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="selected_records.xlsx"'
        workbook.save(response)

        return response