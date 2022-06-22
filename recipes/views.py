from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Waldir'
    })


def about(request):
    return render(request, 'recipes/about.html')


def contact(request):
    return render(request, 'recipes/contact.html')
