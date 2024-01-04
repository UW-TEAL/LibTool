from django.shortcuts import render
import pandas as pd
from .models import *
from .filters import *
import uuid
import numpy
from .forms import *
from django.db.models import Q

def home(request):
    return render(request,'home.html')

def search(request):
    records = Record.objects.all().order_by('authorEnglish')
    namesEng = []
    namesKr = []
    for i in records:
        if i.authorEnglish and i.authorEnglish!= "nan":            
            namesEng.append(i.authorEnglish)
        if i.authorKorean  and i.authorKorean!= "nan":
            namesKr.append(i.authorKorean)
    newNamesEng = [*set(namesEng)]
    newNamesKr = [*set(namesKr)]
    newNamesEng.sort()
    newNamesKr.sort()
    newNamesEng = [i for a,i in enumerate(newNamesEng) if i!=' ']
    newNamesKr = [i for a,i in enumerate(newNamesKr) if i!=' ']
    myFilter = RecordFilter(request.GET, queryset = records)

    
    filters = {}
    filter_criteria = request.GET
    for i in filter_criteria:
        filters[i] = filter_criteria[i]
    filters = {k: v for k, v in filters.items() if v}
    print(filters)
    records = myFilter.qs
    

    query = request.GET.get('query', '')
    if query:
        # Filter your model results by the query across multiple fields
        records = Record.objects.filter(
            Q(authorEnglish__icontains=query) | 
            Q(authorKorean__icontains=query) |
            Q(workTitle__icontains=query) |
            Q(workTitleKorean__icontains=query) |
            Q(translator__icontains=query) |
            Q(sourceTitle__icontains=query) |
            Q(publisher__icontains=query) |
            Q(year__icontains=query) |
            Q(genre__icontains=query)
            # Add more fields as needed
        )
    # print(type(myFilter.form))
    context = {'records':records,'myFilter':myFilter, 'NamesEng':newNamesEng,'NamesKr':newNamesKr, 'Filters':filters}
    return render(request,'search.html',context)

def generateAuthorLinks(names):
    for i in names:
        print(i)
    return 0

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

def search_view(request):
    query = request.GET.get('query', '')
    print("Query Received:", query)  # Get the query from the URL
    if query:
        # Filter your model results by the query across multiple fields
        results = Record.objects.filter(
            Q(authorEnglish__icontains=query) | 
            Q(authorKorean__icontains=query) |
            Q(workTitle__icontains=query) |
            Q(workTitleKorean__icontains=query) |
            Q(translator__icontains=query) |
            Q(sourceTitle__icontains=query) |
            Q(publisher__icontains=query) |
            Q(year__icontains=query) |
            Q(genre__icontains=query)
            # Add more fields as needed
        )
    else:
        results = Record.objects.all()  # If no query, return all results

        

    return render(request, 'search.html', {'results': results})
