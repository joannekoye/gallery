from django.shortcuts import render, redirect
from .models import Location, Image, Category
from django.http import Http404

def index(request):
    '''
    view function to display landing page
    '''
    images = Image.objects.all()

    return render(request, 'index.html', {'images': images})

def search_page(request):
    '''
    view function to open search page and display searched images
    '''

    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        images = Image.search_image(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message':message, 'images': images})

    else:
        message = 'Please enter a term to be sought for'
        return render(request, 'search.html', {'message': message})
