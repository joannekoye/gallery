from django.shortcuts import render

def index(request):
    '''
    view function to display landing page
    '''

    return render(request, 'index.html')
