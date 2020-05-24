from django.shortcuts import render, redirect
from .models import Location, Image, Category
from django.http import Http404

def index(request):
    '''
    view function to display landing page
    '''
    images = Image.objects.all()

    return render(request, 'index.html', {'images': images})
