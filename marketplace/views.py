from django.shortcuts import render
from django.http import HttpResponse


def marketplace(request):
    return HttpResponse('<h1>Marketplace</h1>')
