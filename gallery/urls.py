from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_page, name='search_page'),
    path('locations/sorted/', views.sort_by_locations, name='sort_by_locations')
]