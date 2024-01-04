from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home),
    path('search/',views.search, name="search"),
    path('populatedatabase/',views.populateDatabase),
    path('delete/',views.deleteDatabase),
    path('populateYear/',views.updateYear),
    path('populateAlternames/',views.populateAlternateNames),
    path('updateRec/',views.changeAnything),
    path('admin/', views.adminLogin)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)