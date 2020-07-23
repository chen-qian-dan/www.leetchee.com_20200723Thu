from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def page_home(request):
    return HttpResponse('<h1>page-home</h1>')


def page_about(request):
    return HttpResponse('<h1>page-about</h1>')