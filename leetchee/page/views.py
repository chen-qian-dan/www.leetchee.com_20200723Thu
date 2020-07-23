from django.shortcuts import render


# Create your views here.

def page_home(request):
    context = {
        'title': '首页'
    }
    return render(request, 'page/page_home.html', context)


def page_about(request):
    context = {
        'title': '关于'
    }
    return render(request, 'page/page_about.html', context)