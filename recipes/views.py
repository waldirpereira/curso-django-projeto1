from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Waldir'
    })


def about(request):
    return render(request, 'delete-me/temp.html')


def contact(request):
    return HttpResponse('CONTACT')
