from django.shortcuts import render


# Create your views here.

def page_home(request):
    return render(request, 'page/page_home.html')


def page_about(request):
    return render(request, 'page/page_about.html')