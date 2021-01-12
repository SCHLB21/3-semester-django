from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Кто я?</h1>")
