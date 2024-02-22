from django.urls import path
from . import views
from .views import export_selected_to_excel

urlpatterns = [
    path('',views.home),
    path('search/',views.search, name="search"),
    path('populatedatabase/',views.populateDatabase),
    path('delete/',views.deleteDatabase),
    path('populateYear/',views.updateYear),
    path('populateAlternames/',views.populateAlternateNames),
    path('updateRec/',views.changeAnything),
    path('admin/', views.adminLogin),
    path('export_selected_to_excel/', export_selected_to_excel, name='export_selected_to_excel')
]