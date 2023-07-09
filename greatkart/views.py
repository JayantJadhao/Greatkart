from django.http import HttpResponse
from django.shortcuts import render


def home_1(request):
    return HttpResponse('Homepage')


def home(request):
    return render(request, 'home.html')
