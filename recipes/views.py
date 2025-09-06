# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Pedro Baumgarten Botafogo',
    })


def govbr(request):
    return render(request, 'recipes/pages/govbr.html', context={
        'name': 'Pedro Baumgarten Botafogo',
    })
